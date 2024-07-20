def submit_pipeline(pipeline_name, steps, pipeline_definition_config, config, role, parameters):
    import logging
    # This stops SageMaker from reporting in this cell.
    logging.getLogger('sagemaker.config').disabled = True
    from sagemaker.workflow.pipeline import Pipeline

    pipeline = Pipeline(
        name=pipeline_name,
        parameters=parameters,
        steps=steps,
        pipeline_definition_config=pipeline_definition_config,
        sagemaker_session=config["session"],
    )

    pipeline.upsert(role_arn=role)
    return pipeline