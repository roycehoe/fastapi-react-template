import { createFileRoute } from "@tanstack/react-router";
import { useGetArtists } from "@/api/getArtists";
import { CardArtist } from "@/components/CardArtist";

export const Route = createFileRoute("/")({
  component: App,
});

function App() {
  const { isPending, isError, data, error } = useGetArtists();
  if (error) {
    console.log(error);
  }
  if (isPending) {
    return <div>Pending</div>;
  }
  if (isError) {
    return <div>Error</div>;
  }
  if (data) {
    return (
      <div>
        {data.data.map((artist) => {
          return <CardArtist artist={artist}></CardArtist>;
        })}
      </div>
    );
  }
}
