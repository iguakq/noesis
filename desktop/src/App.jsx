import { Theme } from '@astryxdesign/core';
import { neutralTheme } from '@astryxdesign/theme-neutral';
import { AppShell } from '@astryxdesign/core/AppShell'
import { TopNav, TopNavHeading } from '@astryxdesign/core/TopNav'
import { IconButton } from '@astryxdesign/core/IconButton'
import { SideNav, SideNavItem, SideNavSection } from '@astryxdesign/core/SideNav'

function App() {
  return (
    <Theme theme={neutralTheme}>
      <AppShell contentPadding={6}
        topNav={
          <TopNav
            heading={
              <TopNavHeading
                heading="Noesis"
              />
            }
            endContent={
              <>
                <IconButton
                  label="Minimize"
                />

                <IconButton
                  label="Close"
                />
              </>
            }
          />
        }

        sideNav={
          <SideNav
            footer={
              <SideNavItem
                label="Settings"
              />
            }
          >
            <SideNavSection title="Main" isHeaderHidden>
              <SideNavItem
                label="New Bot"
              />
            </SideNavSection>

            <SideNavSection title="Bots">
            </SideNavSection>

          </SideNav>
        }
      >
        {/* Create or bot component */}
      </AppShell>
    </Theme>
  );
}

export default App;
