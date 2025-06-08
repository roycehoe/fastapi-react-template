import type { Artist } from "@/api/getArtists";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

export function CardArtist(props: { artist: Artist }) {
  return (
    <Card className="w-full max-w-sm">
      <CardHeader>
        <CardTitle>Artist</CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription>
          <p>Name: {props.artist.name}</p>
        </CardDescription>
        <CardDescription>
          <p>Created at: {props.artist.created_at}</p>
        </CardDescription>
        <CardAction>
          <Button className="my-12">Add Album</Button>
        </CardAction>
      </CardContent>
    </Card>
  );
}
