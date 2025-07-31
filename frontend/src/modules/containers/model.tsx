export enum ContainerStatusEnum{
    CREATED = "created",
    RESTARTING = "restarting",
    RUNNING = "running",
    REMOVING = "removing",
    PAUSED = "paused",
    EXITED = "exited",
    DEAD = "dead"
}
export interface ContainerSchema {
    containerId: string;
    name: string;
    status: ContainerStatusEnum;
    createdAt?: string;
    startedAt?: string;
    finishedAt?: string;
}