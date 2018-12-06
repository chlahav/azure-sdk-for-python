# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class OSType(str, Enum):

    linux = "linux"  #: The Linux operating system.
    windows = "windows"  #: The Windows operating system.


class AccessScope(str, Enum):

    job = "job"  #: Grants access to perform all operations on the job containing the task.


class CertificateState(str, Enum):

    active = "active"  #: The certificate is available for use in pools.
    deleting = "deleting"  #: The user has requested that the certificate be deleted, but the delete operation has not yet completed. You may not reference the certificate when creating or updating pools.
    delete_failed = "deletefailed"  #: The user requested that the certificate be deleted, but there are pools that still have references to the certificate, or it is still installed on one or more compute nodes. (The latter can occur if the certificate has been removed from the pool, but the node has not yet restarted. Nodes refresh their certificates only when they restart.) You may use the cancel certificate delete operation to cancel the delete, or the delete certificate operation to retry the delete.


class CertificateFormat(str, Enum):

    pfx = "pfx"  #: The certificate is a PFX (PKCS#12) formatted certificate or certificate chain.
    cer = "cer"  #: The certificate is a base64-encoded X.509 certificate.


class JobAction(str, Enum):

    none = "none"  #: Take no action.
    disable = "disable"  #: Disable the job. This is equivalent to calling the disable job API, with a disableTasks value of requeue.
    terminate = "terminate"  #: Terminate the job. The terminateReason in the job's executionInfo is set to "TaskFailed".


class DependencyAction(str, Enum):

    satisfy = "satisfy"  #: Satisfy the task's dependencies.
    block = "block"  #: Block the task's dependencies.


class AutoUserScope(str, Enum):

    task = "task"  #: Specifies that the service should create a new user for the task.
    pool = "pool"  #: Specifies that the task runs as the common auto user account which is created on every node in a pool.


class ElevationLevel(str, Enum):

    non_admin = "nonadmin"  #: The user is a standard user without elevated access.
    admin = "admin"  #: The user is a user with elevated access and operates with full Administrator permissions.


class LoginMode(str, Enum):

    batch = "batch"  #: The LOGON32_LOGON_BATCH Win32 login mode. The batch login mode is recommended for long running parallel processes.
    interactive = "interactive"  #: The LOGON32_LOGON_INTERACTIVE Win32 login mode. UAC is enabled on VirtualMachineConfiguration pools. If this option is used with an elevated user in a VirtualMachineConfiguration pool, the user session will not be elevated unless the application executed by the task command line is configured to always require administrative privilege or to always require maximum privilege.


class OutputFileUploadCondition(str, Enum):

    task_success = "tasksuccess"  #: Upload the file(s) only after the task process exits with an exit code of 0.
    task_failure = "taskfailure"  #: Upload the file(s) only after the task process exits with a nonzero exit code.
    task_completion = "taskcompletion"  #: Upload the file(s) after the task process exits, no matter what the exit code was.


class ComputeNodeFillType(str, Enum):

    spread = "spread"  #: Tasks should be assigned evenly across all nodes in the pool.
    pack = "pack"  #: As many tasks as possible (maxTasksPerNode) should be assigned to each node in the pool before any tasks are assigned to the next node in the pool.


class CertificateStoreLocation(str, Enum):

    current_user = "currentuser"  #: Certificates should be installed to the CurrentUser certificate store.
    local_machine = "localmachine"  #: Certificates should be installed to the LocalMachine certificate store.


class CertificateVisibility(str, Enum):

    start_task = "starttask"  #: The certificate should be visible to the user account under which the start task is run.
    task = "task"  #: The certificate should be visible to the user accounts under which job tasks are run.
    remote_user = "remoteuser"  #: The certificate should be visible to the user accounts under which users remotely access the node.


class CachingType(str, Enum):

    none = "none"  #: The caching mode for the disk is not enabled.
    read_only = "readonly"  #: The caching mode for the disk is read only.
    read_write = "readwrite"  #: The caching mode for the disk is read and write.


class StorageAccountType(str, Enum):

    standard_lrs = "standard_lrs"  #: The data disk should use standard locally redundant storage.
    premium_lrs = "premium_lrs"  #: The data disk should use premium locally redundant storage.


class DynamicVNetAssignmentScope(str, Enum):

    none = "none"  #: No dynamic VNet assignment is enabled.
    job = "job"  #: Dynamic VNet assignment is done per-job.


class InboundEndpointProtocol(str, Enum):

    tcp = "tcp"  #: Use TCP for the endpoint.
    udp = "udp"  #: Use UDP for the endpoint.


class NetworkSecurityGroupRuleAccess(str, Enum):

    allow = "allow"  #: Allow access.
    deny = "deny"  #: Deny access.


class PoolLifetimeOption(str, Enum):

    job_schedule = "jobschedule"  #: The pool exists for the lifetime of the job schedule. The Batch Service creates the pool when it creates the first job on the schedule. You may apply this option only to job schedules, not to jobs.
    job = "job"  #: The pool exists for the lifetime of the job to which it is dedicated. The Batch service creates the pool when it creates the job. If the 'job' option is applied to a job schedule, the Batch service creates a new auto pool for every job created on the schedule.


class OnAllTasksComplete(str, Enum):

    no_action = "noaction"  #: Do nothing. The job remains active unless terminated or disabled by some other means.
    terminate_job = "terminatejob"  #: Terminate the job. The job's terminateReason is set to 'AllTasksComplete'.


class OnTaskFailure(str, Enum):

    no_action = "noaction"  #: Do nothing. The job remains active unless terminated or disabled by some other means.
    perform_exit_options_job_action = "performexitoptionsjobaction"  #: Take the action associated with the task exit condition in the task's exitConditions collection. (This may still result in no action being taken, if that is what the task specifies.)


class JobScheduleState(str, Enum):

    active = "active"  #: The job schedule is active and will create jobs as per its schedule.
    completed = "completed"  #: The schedule has terminated, either by reaching its end time or by the user terminating it explicitly.
    disabled = "disabled"  #: The user has disabled the schedule. The scheduler will not initiate any new jobs will on this schedule, but any existing active job will continue to run.
    terminating = "terminating"  #: The schedule has no more work to do, or has been explicitly terminated by the user, but the termination operation is still in progress. The scheduler will not initiate any new jobs for this schedule, nor is any existing job active.
    deleting = "deleting"  #: The user has requested that the schedule be deleted, but the delete operation is still in progress. The scheduler will not initiate any new jobs for this schedule, and will delete any existing jobs and tasks under the schedule, including any active job. The schedule will be deleted when all jobs and tasks under the schedule have been deleted.


class ErrorCategory(str, Enum):

    user_error = "usererror"  #: The error is due to a user issue, such as misconfiguration.
    server_error = "servererror"  #: The error is due to an internal server issue.


class JobState(str, Enum):

    active = "active"  #: The job is available to have tasks scheduled.
    disabling = "disabling"  #: A user has requested that the job be disabled, but the disable operation is still in progress (for example, waiting for tasks to terminate).
    disabled = "disabled"  #: A user has disabled the job. No tasks are running, and no new tasks will be scheduled.
    enabling = "enabling"  #: A user has requested that the job be enabled, but the enable operation is still in progress.
    terminating = "terminating"  #: The job is about to complete, either because a Job Manager task has completed or because the user has terminated the job, but the terminate operation is still in progress (for example, because Job Release tasks are running).
    completed = "completed"  #: All tasks have terminated, and the system will not accept any more tasks or any further changes to the job.
    deleting = "deleting"  #: A user has requested that the job be deleted, but the delete operation is still in progress (for example, because the system is still terminating running tasks).


class JobPreparationTaskState(str, Enum):

    running = "running"  #: The task is currently running (including retrying).
    completed = "completed"  #: The task has exited with exit code 0, or the task has exhausted its retry limit, or the Batch service was unable to start the task due to task preparation errors (such as resource file download failures).


class TaskExecutionResult(str, Enum):

    success = "success"  #: The task ran successfully.
    failure = "failure"  #: There was an error during processing of the task. The failure may have occurred before the task process was launched, while the task process was executing, or after the task process exited.


class JobReleaseTaskState(str, Enum):

    running = "running"  #: The task is currently running (including retrying).
    completed = "completed"  #: The task has exited with exit code 0, or the task has exhausted its retry limit, or the Batch service was unable to start the task due to task preparation errors (such as resource file download failures).


class PoolState(str, Enum):

    active = "active"  #: The pool is available to run tasks subject to the availability of compute nodes.
    deleting = "deleting"  #: The user has requested that the pool be deleted, but the delete operation has not yet completed.


class AllocationState(str, Enum):

    steady = "steady"  #: The pool is not resizing. There are no changes to the number of nodes in the pool in progress. A pool enters this state when it is created and when no operations are being performed on the pool to change the number of nodes.
    resizing = "resizing"  #: The pool is resizing; that is, compute nodes are being added to or removed from the pool.
    stopping = "stopping"  #: The pool was resizing, but the user has requested that the resize be stopped, but the stop request has not yet been completed.


class TaskState(str, Enum):

    active = "active"  #: The task is queued and able to run, but is not currently assigned to a compute node. A task enters this state when it is created, when it is enabled after being disabled, or when it is awaiting a retry after a failed run.
    preparing = "preparing"  #: The task has been assigned to a compute node, but is waiting for a required Job Preparation task to complete on the node. If the Job Preparation task succeeds, the task will move to running. If the Job Preparation task fails, the task will return to active and will be eligible to be assigned to a different node.
    running = "running"  #: The task is running on a compute node. This includes task-level preparation such as downloading resource files or deploying application packages specified on the task - it does not necessarily mean that the task command line has started executing.
    completed = "completed"  #: The task is no longer eligible to run, usually because the task has finished successfully, or the task has finished unsuccessfully and has exhausted its retry limit. A task is also marked as completed if an error occurred launching the task, or when the task has been terminated.


class TaskAddStatus(str, Enum):

    success = "success"  #: The task was added successfully.
    client_error = "clienterror"  #: The task failed to add due to a client error and should not be retried without modifying the request as appropriate.
    server_error = "servererror"  #: Task failed to add due to a server error and can be retried without modification.


class SubtaskState(str, Enum):

    preparing = "preparing"  #: The task has been assigned to a compute node, but is waiting for a required Job Preparation task to complete on the node. If the Job Preparation task succeeds, the task will move to running. If the Job Preparation task fails, the task will return to active and will be eligible to be assigned to a different node.
    running = "running"  #: The task is running on a compute node. This includes task-level preparation such as downloading resource files or deploying application packages specified on the task - it does not necessarily mean that the task command line has started executing.
    completed = "completed"  #: The task is no longer eligible to run, usually because the task has finished successfully, or the task has finished unsuccessfully and has exhausted its retry limit. A task is also marked as completed if an error occurred launching the task, or when the task has been terminated.


class StartTaskState(str, Enum):

    running = "running"  #: The start task is currently running.
    completed = "completed"  #: The start task has exited with exit code 0, or the start task has failed and the retry limit has reached, or the start task process did not run due to task preparation errors (such as resource file download failures).


class ComputeNodeState(str, Enum):

    idle = "idle"  #: The node is not currently running a task.
    rebooting = "rebooting"  #: The node is rebooting.
    reimaging = "reimaging"  #: The node is reimaging.
    running = "running"  #: The node is running one or more tasks (other than a start task).
    unusable = "unusable"  #: The node cannot be used for task execution due to errors.
    creating = "creating"  #: The Batch service has obtained the underlying virtual machine from Azure Compute, but it has not yet started to join the pool.
    starting = "starting"  #: The Batch service is starting on the underlying virtual machine.
    waiting_for_start_task = "waitingforstarttask"  #: The start task has started running on the compute node, but waitForSuccess is set and the start task has not yet completed.
    start_task_failed = "starttaskfailed"  #: The start task has failed on the compute node (and exhausted all retries), and waitForSuccess is set. The node is not usable for running tasks.
    unknown = "unknown"  #: The Batch service has lost contact with the node, and does not know its true state.
    leaving_pool = "leavingpool"  #: The node is leaving the pool, either because the user explicitly removed it or because the pool is resizing or autoscaling down.
    offline = "offline"  #: The node is not currently running a task, and scheduling of new tasks to the node is disabled.
    preempted = "preempted"  #: The low-priority node has been preempted. Tasks which were running on the node when it was pre-empted will be rescheduled when another node becomes available.


class SchedulingState(str, Enum):

    enabled = "enabled"  #: Tasks can be scheduled on the node.
    disabled = "disabled"  #: No new tasks will be scheduled on the node. Tasks already running on the node may still run to completion. All nodes start with scheduling enabled.


class DisableJobOption(str, Enum):

    requeue = "requeue"  #: Terminate running tasks and requeue them. The tasks will run again when the job is enabled.
    terminate = "terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again.
    wait = "wait"  #: Allow currently running tasks to complete.


class ComputeNodeDeallocationOption(str, Enum):

    requeue = "requeue"  #: Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Remove nodes as soon as tasks have been terminated.
    terminate = "terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again. Remove nodes as soon as tasks have been terminated.
    task_completion = "taskcompletion"  #: Allow currently running tasks to complete. Schedule no new tasks while waiting. Remove nodes when all tasks have completed.
    retained_data = "retaineddata"  #: Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Remove nodes when all task retention periods have expired.


class ComputeNodeRebootOption(str, Enum):

    requeue = "requeue"  #: Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Restart the node as soon as tasks have been terminated.
    terminate = "terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again. Restart the node as soon as tasks have been terminated.
    task_completion = "taskcompletion"  #: Allow currently running tasks to complete. Schedule no new tasks while waiting. Restart the node when all tasks have completed.
    retained_data = "retaineddata"  #: Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Restart the node when all task retention periods have expired.


class ComputeNodeReimageOption(str, Enum):

    requeue = "requeue"  #: Terminate running task processes and requeue the tasks. The tasks will run again when a node is available. Reimage the node as soon as tasks have been terminated.
    terminate = "terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again. Reimage the node as soon as tasks have been terminated.
    task_completion = "taskcompletion"  #: Allow currently running tasks to complete. Schedule no new tasks while waiting. Reimage the node when all tasks have completed.
    retained_data = "retaineddata"  #: Allow currently running tasks to complete, then wait for all task data retention periods to expire. Schedule no new tasks while waiting. Reimage the node when all task retention periods have expired.


class DisableComputeNodeSchedulingOption(str, Enum):

    requeue = "requeue"  #: Terminate running task processes and requeue the tasks. The tasks may run again on other compute nodes, or when task scheduling is re-enabled on this node. Enter offline state as soon as tasks have been terminated.
    terminate = "terminate"  #: Terminate running tasks. The tasks will be completed with failureInfo indicating that they were terminated, and will not run again. Enter offline state as soon as tasks have been terminated.
    task_completion = "taskcompletion"  #: Allow currently running tasks to complete. Schedule no new tasks while waiting. Enter offline state when all tasks have completed.
