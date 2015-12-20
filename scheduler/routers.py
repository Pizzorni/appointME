#stolen from scalica
NUM_LOGICAL_SHARDS = 16
NUM_PHYSICAL_SHARDS = 2

LOGICAL_TO_PHYSICAL = (
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
  'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
)

# returns a dictionary mapping a shard to all the users in that shard
# from user_ids.
def bucket_users_into_shards(user_ids):
  d = {}
  for id in user_ids:
    shard = logical_shard_for_user(id)
    if not shard in d:
      d[shard] = []
    d[shard].append(id)
  return d
    
  
  return [str(x) for x in range(NUM_LOGICAL_SHARDS)]

def logical_to_physical(logical):
  if logical >= NUM_LOGICAL_SHARDS or logical < 0:
    raise Exception("shard out of bounds %d" % logical)
  return LOGICAL_TO_PHYSICAL[logical] 
 
def logical_shard_for_user(user_id):
  print "Looking for shard for user %d" % user_id
  return user_id % NUM_LOGICAL_SHARDS

class UserRouter(object):

  def _database_of(self, user_id):
    return logical_to_physical(logical_shard_for_user(user_id))

  def _db_for_read_write(self, model, **hints):
    """ """
    # Auth reads always go to the auth sub-system
    if model._meta.app_label == 'auth':
      return 'default'
    # For now, sessions are stored on the auth sub-system, too.
    if model._meta.app_label == 'sessions':
      return 'default'
    db = None    
    try:
      instance = hints['instance']
      db = self._database_of(instance.user_id)
    except AttributeError:
      # For the user model the key is id.
      db = self._database_of(instance.id)
    except KeyError:
      try:
        db = self._database_of(int(hints['user_id']))
      except KeyError:
        print "No instance in hints"
    print "Returning", db
    return db
  
  def db_for_read(self, model, **hints):
    """ """
    return self._db_for_read_write(model, **hints)
  
  def db_for_write(self, model, **hints):
    """ """
    return self._db_for_read_write(model, **hints)

  def allow_relation(self, obj1, obj2, **hints):
    if (obj1._meta.app_label == 'auth' and obj2._meta.app_label != 'auth') or \
      (obj1._meta.app_label != 'auth' and obj2._meta.app_label == 'auth'):
      print "Rejecting cross-table relationship", obj1._meta.app_label, \
        obj2._meta.app_label
      return False
    return True

  def allow_migrate(self, db, app_label, model=None, **hints):
    return True
