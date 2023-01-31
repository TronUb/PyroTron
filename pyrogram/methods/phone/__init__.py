from .create_group_call import CreateGroupCall
from .get_group_call import GetGroupCall
from .join_group_call import JoinGroupCall
from .leave_group_call import LeaveGroupCall
from .edit_group_call_participant import EditGroupCallParticipant
from .invite_to_group_call import InviteToGroupCall



class Phone(
    CreateGroupCall,
    GetGroupCall,
    JoinGroupCall,
    LeaveGroupCall,
    EditGroupCallParticipant,
    InviteToGroupCall
):
    pass
