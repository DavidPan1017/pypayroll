# -*- coding: utf-8 -*-


class Posn:
    """
    Desc: 岗位信息
    Author: David
    Date: 2020/12/23
    """

    def __init__(self, **kwargs):
        self.tenant_id = kwargs.get('tenant_id', 0)
        self.posn_code = kwargs.get('hhr_posn_code', '')
        self.efft_date = kwargs.get('hhr_efft_date', None)
        self.efft_end_date = kwargs.get('hhr_efft_end_date', None)
        self.status = kwargs.get('hhr_status', '')
        self.posn_name = kwargs.get('hhr_posn_name', '')
        self.posn_short_name = kwargs.get('hhr_posn_short_name', '')
        self.sort_num = kwargs.get('hhr_sort_num', 0)
        self.dept_code = kwargs.get('hhr_dept_code', '')
        self.bu_code = kwargs.get('hhr_bu_code', '')
        self.job_code = kwargs.get('hhr_job_code', '')
        self.rank_min = kwargs.get('hhr_rank_min', '')
        self.rank_max = kwargs.get('hhr_rank_max', '')
        self.group_code = kwargs.get('hhr_group_code', '')
        self.sequence_code = kwargs.get('hhr_sequence_code', '')
        self.direct_report_posn = kwargs.get('hhr_direct_report_posn', '')
        self.direct_report_person = kwargs.get('hhr_direct_report_person', '')
        self.dashed_report_posn = kwargs.get('hhr_dashed_report_posn', '')
        self.dashed_report_person = kwargs.get('hhr_dashed_report_person', '')
        self.location = kwargs.get('hhr_location', '')
        self.posn_desc = kwargs.get('hhr_posn_desc', '')
        self.change_type = kwargs.get('hhr_change_type', '')
        self.posn_require = kwargs.get('hhr_posn_require', '')
        self.org_posn_attr01 = '' if kwargs.get('hhr_org_posn_attr01', '') is None else kwargs.get('hhr_org_posn_attr01')
        self.org_posn_attr02 = '' if kwargs.get('hhr_org_posn_attr02', '') is None else kwargs.get('hhr_org_posn_attr02')
        self.org_posn_attr03 = '' if kwargs.get('hhr_org_posn_attr03', '') is None else kwargs.get('hhr_org_posn_attr03')
        self.org_posn_attr04 = '' if kwargs.get('hhr_org_posn_attr04', '') is None else kwargs.get('hhr_org_posn_attr04')
        self.org_posn_attr05 = '' if kwargs.get('hhr_org_posn_attr05', '') is None else kwargs.get('hhr_org_posn_attr05')
        self.org_posn_attr06 = '' if kwargs.get('hhr_org_posn_attr06', '') is None else kwargs.get('hhr_org_posn_attr06')
        self.org_posn_attr07 = '' if kwargs.get('hhr_org_posn_attr07', '') is None else kwargs.get('hhr_org_posn_attr07')
        self.org_posn_attr08 = '' if kwargs.get('hhr_org_posn_attr08', '') is None else kwargs.get('hhr_org_posn_attr08')
        self.org_posn_attr09 = '' if kwargs.get('hhr_org_posn_attr09', '') is None else kwargs.get('hhr_org_posn_attr09')
        self.org_posn_attr10 = '' if kwargs.get('hhr_org_posn_attr10', '') is None else kwargs.get('hhr_org_posn_attr10')
        self.org_posn_attr11 = '' if kwargs.get('hhr_org_posn_attr11', '') is None else kwargs.get('hhr_org_posn_attr11')
        self.org_posn_attr12 = '' if kwargs.get('hhr_org_posn_attr12', '') is None else kwargs.get('hhr_org_posn_attr12')
        self.org_posn_attr13 = '' if kwargs.get('hhr_org_posn_attr13', '') is None else kwargs.get('hhr_org_posn_attr13')
        self.org_posn_attr14 = '' if kwargs.get('hhr_org_posn_attr14', '') is None else kwargs.get('hhr_org_posn_attr14')
        self.org_posn_attr15 = '' if kwargs.get('hhr_org_posn_attr15', '') is None else kwargs.get('hhr_org_posn_attr15')
        self.org_posn_attr16 = '' if kwargs.get('hhr_org_posn_attr16', '') is None else kwargs.get('hhr_org_posn_attr16')
        self.org_posn_attr17 = '' if kwargs.get('hhr_org_posn_attr17', '') is None else kwargs.get('hhr_org_posn_attr17')
        self.org_posn_attr18 = '' if kwargs.get('hhr_org_posn_attr18', '') is None else kwargs.get('hhr_org_posn_attr18')
        self.org_posn_attr19 = '' if kwargs.get('hhr_org_posn_attr19', '') is None else kwargs.get('hhr_org_posn_attr19')
        self.org_posn_attr20 = '' if kwargs.get('hhr_org_posn_attr20', '') is None else kwargs.get('hhr_org_posn_attr20')
        self.org_posn_attr21 = '' if kwargs.get('hhr_org_posn_attr21', '') is None else kwargs.get('hhr_org_posn_attr21')
        self.org_posn_attr22 = '' if kwargs.get('hhr_org_posn_attr22', '') is None else kwargs.get('hhr_org_posn_attr22')
        self.org_posn_attr23 = '' if kwargs.get('hhr_org_posn_attr23', '') is None else kwargs.get('hhr_org_posn_attr23')
        self.org_posn_attr24 = '' if kwargs.get('hhr_org_posn_attr24', '') is None else kwargs.get('hhr_org_posn_attr24')
        self.org_posn_attr25 = '' if kwargs.get('hhr_org_posn_attr25', '') is None else kwargs.get('hhr_org_posn_attr25')
        self.org_posn_attr26 = '' if kwargs.get('hhr_org_posn_attr26', '') is None else kwargs.get('hhr_org_posn_attr26')
        self.org_posn_attr27 = '' if kwargs.get('hhr_org_posn_attr27', '') is None else kwargs.get('hhr_org_posn_attr27')
        self.org_posn_attr28 = '' if kwargs.get('hhr_org_posn_attr28', '') is None else kwargs.get('hhr_org_posn_attr28')
        self.org_posn_attr29 = '' if kwargs.get('hhr_org_posn_attr29', '') is None else kwargs.get('hhr_org_posn_attr29')
        self.org_posn_attr30 = '' if kwargs.get('hhr_org_posn_attr30', '') is None else kwargs.get('hhr_org_posn_attr30')