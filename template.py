
def GenerateConfig(context):

  resources = []
# [START use_basic_template]
  resources.append({
      'name': 'deployment-vm',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': 'us-central1-a',
          'machineType': 'zones/us-central1-a/machineTypes/n1-standard-1',
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage':
                      'projects/ubuntu-os-cloud/global/images/family/ubuntu-1804-lts'
              }
          }],
          'networkInterfaces': [{
              'network': 'global/networks/default'
          }]
      }
  })
# [END use_basic_template]
  return {'resources': resources}
