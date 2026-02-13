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
export type UIContainerStatus = "running" | "stopped" | "paused" ;



export const DOCKER_TO_UI_STATUS: Record<ContainerStatusEnum, UIContainerStatus> = {
    created: "stopped",
    exited: "stopped",
    dead: "stopped",
    running: "running",
    paused: "paused"
}