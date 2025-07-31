import { ContainerSchema } from "@/modules/containers/model";
import { StatusBadge } from "./StatusBadge";

export function ContainerCard({container}: {container: ContainerSchema}){
    return (
    <div className="p-4 border rounded flex justify-between items-center shadow-sm bg-white">
        <div>
          <h2 className="text-lg font-bold">{container.name}</h2>
          <p className="text-sm text-gray-500">{container.status}</p>
        </div>
        <StatusBadge status={container.status} />
      </div>
    );
}