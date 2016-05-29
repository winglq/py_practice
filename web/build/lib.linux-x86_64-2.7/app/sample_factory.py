from sample_app import application
def app_factory(global_config, **local_conf):
    return application
