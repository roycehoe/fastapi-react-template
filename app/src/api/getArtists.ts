import { useQuery } from "@tanstack/react-query";

interface Artist {
  artist_id: number;
  name: string;
  created_at: string;
  albums: [];
}

export interface GetArtistsResponse {
  data: Artist[];
}

async function getArtists(): Promise<GetArtistsResponse> {
  const response = await fetch("http://localhost:8000/artists");
  return response.json();
}

export function useGetArtists() {
  return useQuery({ queryKey: ["getArtists"], queryFn: getArtists });
}
