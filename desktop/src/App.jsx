import { Theme } from '@astryxdesign/core';
import { neutralTheme } from '@astryxdesign/theme-neutral';
import { AppShell } from '@astryxdesign/core/AppShell'
import { TopNav, TopNavHeading } from '@astryxdesign/core/TopNav'
import { IconButton } from '@astryxdesign/core/IconButton'
import { Minus, Maximize, X, Settings, CirclePlus } from 'lucide-react'
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
                  icon={<Minus/>}
                  label="Minimize"
                />

                <IconButton
                  icon={<Maximize/>}
                  label="Maximize"
                />

                <IconButton
                  icon={<X/>}
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
                icon={<Settings/>}
                label="Settings"
              />
            }
          >
            <SideNavSection title="Main" isHeaderHidden>
              <SideNavItem
                icon={<CirclePlus/>}
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
