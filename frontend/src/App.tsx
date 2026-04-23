import type { JSX } from 'react'
import PlaylistImport from '@/components/PlaylistImport'
import TrackList from '@/components/TrackList'
import TrackEditor from '@/components/TrackEditor'
import MixTimeline from '@/components/MixTimeline'
import { GlobalStyle, Shell, Topbar, Sidebar, Editor, Timeline } from './App.styled'

export default function App(): JSX.Element {
  return (
    <>
      <GlobalStyle />
      <Shell>
        <Topbar>
          <PlaylistImport />
        </Topbar>
        <Sidebar>
          <TrackList />
        </Sidebar>
        <Editor>
          <TrackEditor />
        </Editor>
        <Timeline>
          <MixTimeline />
        </Timeline>
      </Shell>
    </>
  )
}
