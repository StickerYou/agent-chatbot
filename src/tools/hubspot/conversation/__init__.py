"""HubSpot Conversation Tools"""

from .conversation_tools import (
    get_actor_details,
    get_actors_batch,
    get_channel_account_details,
    get_channel_details,
    list_channel_accounts,
    list_channels,
    get_inbox_details,
    list_inboxes,
    get_message_details,
    get_original_message_content,
    archive_thread,
    get_thread_details,
    get_thread_messages,
    list_threads,
    send_message_to_thread,
    update_thread,
)

from .dto_requests import (
    BatchReadActorsRequest,
    CreateMessageRequest,
    UpdateThreadRequest,
    DeliveryIdentifier,
    MessageRecipientRequest,
    QuickReplyOption,
    QuickReplyAttachment,
    FileUploadAttachment,
)

from .dto_responses import (
    ThreadDetail,
    ListMessagesResponse,
    ListThreadsResponse,
    ThreadStatus,
    UpdateThreadResponse,
    ActorDetailResponse,
    BatchReadActorsResponse,
    ListInboxesResponse,
    InboxDetailResponse,
    ListChannelsResponse,
    ChannelDetailResponse,
    ListChannelAccountsResponse,
    ChannelAccountDetailResponse,
    MessageDetailResponse,
    OriginalMessageContentResponse,
    CreateMessageResponse,
)

__all__ = [
    # Tools
    "get_actor_details",
    "get_actors_batch",
    "get_channel_account_details",
    "get_channel_details",
    "list_channel_accounts",
    "list_channels",
    "get_inbox_details",
    "list_inboxes",
    "get_message_details",
    "get_original_message_content",
    "archive_thread",
    "get_thread_details",
    "get_thread_messages",
    "list_threads",
    "send_message_to_thread",
    "update_thread",
    # Request DTOs
    "BatchReadActorsRequest",
    "CreateMessageRequest",
    "UpdateThreadRequest",
    "DeliveryIdentifier",
    "MessageRecipientRequest",
    "QuickReplyOption",
    "QuickReplyAttachment",
    "FileUploadAttachment",
    # Response DTOs
    "ThreadDetail",
    "ListMessagesResponse",
    "ListThreadsResponse",
    "ThreadStatus",
    "UpdateThreadResponse",
    "ActorDetailResponse",
    "BatchReadActorsResponse",
    "ListInboxesResponse",
    "InboxDetailResponse",
    "ListChannelsResponse",
    "ChannelDetailResponse",
    "ListChannelAccountsResponse",
    "ChannelAccountDetailResponse",
    "MessageDetailResponse",
    "OriginalMessageContentResponse",
    "CreateMessageResponse",
]
