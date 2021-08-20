import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    boldEx1 = create_key('sub-{subject}/func/sub-{subject}_task-boldEx_run-{item:01d}_bold')
    boldEx2 = create_key('sub-{subject}/func/sub-{subject}_task-boldEx2_run-{item:01d}_bold')
    boldRun1 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun1_run-{item:01d}_bold')
    boldRun2 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun2_run-{item:01d}_bold')
    boldRun3 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun3_run-{item:01d}_bold')
    boldRun4 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun4_run-{item:01d}_bold')
    boldRun5 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun5_run-{item:01d}_bold')
    boldRun6 = create_key('sub-{subject}/func/sub-{subject}_task-boldRun6_run-{item:01d}_bold')
    rest = create_key('sub-{subject}/func/sub-{subject}_task-rest_run-{item:01d}_bold')
    t1 = create_key('sub-{subject}/anat/sub-{subject}_run-{item:01d}_T1w')
    t2 = create_key('sub-{subject}/anat/sub-{subject}_run-{item:01d}_T2w')
    fmap = create_key('sub-{subject}/fmap/sub-{subject}_run-{item:01d}_phasediff')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_run-{item:01d}_dwi')

    info = {
                boldEx1: [],
                boldEx2: [],
                boldRun1: [],
                boldRun2: [],
                boldRun3: [],
                boldRun4: [],
                boldRun5: [],
                boldRun6: [],
                rest: [],
                t1: [],
                t2: [],
                fmap: [],
                dwi: [],
            }

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """
        if s.protocol_name == 't1_mprage_0.9mm':
            info[t1].append(s.series_id)
        if s.protocol_name == 't2w_space_0.9mm':
            info[t2].append(s.series_id)
        if ('Rest' in s.protocol_name):
            info[rest].append(s.series_id)
        if ('exp_1' in s.protocol_name):
            info[boldEx1].append(s.series_id)
        if ('exp_2' in s.protocol_name):
            info[boldEx2].append(s.series_id)
        if ('test_1' in s.protocol_name):
            info[boldRun1].append(s.series_id)
        if ('test_2' in s.protocol_name):
            info[boldRun2].append(s.series_id)
        if ('test_3' in s.protocol_name):
            info[boldRun3].append(s.series_id)
        if ('test_4' in s.protocol_name):
            info[boldRun4].append(s.series_id)
        if ('test_5' in s.protocol_name):
            info[boldRun5].append(s.series_id)
        if ('test_6' in s.protocol_name):
            info[boldRun6].append(s.series_id)
        if ('field' in s.protocol_name):
            info[fmap].append(s.series_id)
        if ('dsi' in s.protocol_name):
            info[dwi].append(s.series_id)



    return info
