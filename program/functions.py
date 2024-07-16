def submit_pipeline(dataset_location, pipeline_name, steps, pipeline_definition_config, config, role):
    from sagemaker.workflow.pipeline import Pipeline
    import logging
    # This stops SageMaker from reporting in this cell.
    logging.getLogger('sagemaker.config').disabled = True

    pipeline = Pipeline(
        name=pipeline_name,
        parameters=[dataset_location],
        steps=steps,
        pipeline_definition_config=pipeline_definition_config,
        sagemaker_session=config["session"],
    )

    pipeline.upsert(role_arn=role)
    return pipeline