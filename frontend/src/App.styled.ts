import styled, { createGlobalStyle } from 'styled-components'

export const GlobalStyle = createGlobalStyle`
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  .material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    vertical-align: middle;
    font-size: 18px;
  }
  ::-webkit-scrollbar { width: 4px; height: 4px; }
  ::-webkit-scrollbar-track { background: ${({ theme }) => theme.colors.background}; }
  ::-webkit-scrollbar-thumb { background: ${({ theme }) => theme.colors.surfaceContainerHighest}; }
  ::-webkit-scrollbar-thumb:hover { background: ${({ theme }) => theme.colors.outlineVariant}; }
  body {
    background: ${({ theme }) => theme.colors.background};
    color: ${({ theme }) => theme.colors.onBackground};
    font-family: ${({ theme }) => theme.typography.bodySm.family};
    font-size: ${({ theme }) => theme.typography.bodySm.size};
    line-height: ${({ theme }) => theme.typography.bodySm.lineHeight};
    overflow: hidden;
    user-select: none;
  }
`

export const Shell = styled.div`
  display: grid;
  grid-template-rows: 48px 1fr 128px;
  grid-template-columns: 256px 1fr;
  grid-template-areas:
    'topbar   topbar'
    'sidebar  editor'
    'timeline timeline';
  height: 100vh;
`

export const Topbar = styled.header`
  grid-area: topbar;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 ${({ theme }) => theme.spacing.lg};
  border-bottom: 1px solid ${({ theme }) => theme.colors.outlineVariant};
  background: ${({ theme }) => theme.colors.topbar};
`

export const Sidebar = styled.aside`
  grid-area: sidebar;
  overflow-y: auto;
  border-right: 1px solid ${({ theme }) => theme.colors.outlineVariant};
  background: ${({ theme }) => theme.colors.topbar};
  display: flex;
  flex-direction: column;
`

export const Editor = styled.main`
  grid-area: editor;
  overflow-y: auto;
  background: ${({ theme }) => theme.colors.surface};
`

export const Timeline = styled.section`
  grid-area: timeline;
  border-top: 1px solid ${({ theme }) => theme.colors.outlineVariant};
  background: ${({ theme }) => theme.colors.topbar};
  display: flex;
  flex-direction: column;
`
