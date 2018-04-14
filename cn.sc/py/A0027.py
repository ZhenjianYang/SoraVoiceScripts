from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0027   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '04610强化猎兵Ａ待机',                  # 9
        '04611强化猎兵Ａ移动',                  # 10
        '04612强化猎兵Ａ攻击',                  # 11
        '04613强化猎兵Ａ被弹开',                # 12
        '04614强化猎兵Ａ倒下',                  # 13
        '04615强化猎兵Ａ魔法咏唱',              # 14
        '04616强化猎兵Ａ魔法发射',              # 15
        '04620强化猎兵Ｂ待机',                  # 16
        '04621强化猎兵Ｂ移动',                  # 17
        '04622强化猎兵Ｂ攻击',                  # 18
        '04623强化猎兵Ｂ被弹开',                # 19
        '04624强化猎兵Ｂ倒下',                  # 20
        '04625强化猎兵Ｂ魔法咏唱',              # 21
        '04626强化猎兵Ｂ魔法发射',              # 22
        '04630强化猎兵克鲁茨待机',              # 23
        '04631强化猎兵克鲁茨移动',              # 24
        '04632强化猎兵克鲁茨攻击',              # 25
        '04633强化猎兵克鲁茨被弹开',            # 26
        '04634强化猎兵克鲁茨倒下',              # 27
        '04635强化猎兵克鲁茨魔法咏唱',          # 28
        '04636强化猎兵克鲁茨魔法发射',          # 29
        '04640强化猎兵卡露娜待机',              # 30
        '04641强化猎兵卡露娜移动',              # 31
        '04642强化猎兵卡露娜攻击',              # 32
        '04643强化猎兵卡露娜被弹开',            # 33
        '04644强化猎兵卡露娜倒下',              # 34
        '04645强化猎兵卡露娜魔法咏唱',          # 35
        '04646强化猎兵卡露娜魔法发射',          # 36
        '04750强化猎兵基尔巴特待机',            # 37
        '04751强化猎兵基尔巴特移动',            # 38
        '04752强化猎兵基尔巴特攻击',            # 39
        '04753强化猎兵基尔巴特被弹开',          # 40
        '04754强化猎兵基尔巴特倒下',            # 41
        '04755强化猎兵基尔巴特魔法咏唱',        # 42
        '04756强化猎兵基尔巴特魔法发射',        # 43
        '04820强化猎兵库拉茨待机',              # 44
        '04821强化猎兵库拉茨移动',              # 45
        '04822强化猎兵库拉茨攻击',              # 46
        '04823强化猎兵库拉茨被弹开',            # 47
        '04824强化猎兵库拉茨倒下',              # 48
        '04825强化猎兵库拉茨魔法咏唱',          # 49
        '04826强化猎兵库拉茨魔法发射',          # 50
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH04610 ._CH',             # 00
        'ED6_DT27/CH04611 ._CH',             # 01
        'ED6_DT27/CH04612 ._CH',             # 02
        'ED6_DT27/CH04613 ._CH',             # 03
        'ED6_DT27/CH04614 ._CH',             # 04
        'ED6_DT27/CH04615 ._CH',             # 05
        'ED6_DT27/CH04616 ._CH',             # 06
        'ED6_DT27/CH04613 ._CH',             # 07
        'ED6_DT27/CH04613 ._CH',             # 08
        'ED6_DT27/CH04613 ._CH',             # 09
        'ED6_DT27/CH04620 ._CH',             # 0A
        'ED6_DT27/CH04621 ._CH',             # 0B
        'ED6_DT27/CH04622 ._CH',             # 0C
        'ED6_DT27/CH04623 ._CH',             # 0D
        'ED6_DT27/CH04624 ._CH',             # 0E
        'ED6_DT27/CH04625 ._CH',             # 0F
        'ED6_DT27/CH04626 ._CH',             # 10
        'ED6_DT27/CH04623 ._CH',             # 11
        'ED6_DT27/CH04623 ._CH',             # 12
        'ED6_DT27/CH04623 ._CH',             # 13
        'ED6_DT27/CH04630 ._CH',             # 14
        'ED6_DT27/CH04631 ._CH',             # 15
        'ED6_DT27/CH04632 ._CH',             # 16
        'ED6_DT27/CH04633 ._CH',             # 17
        'ED6_DT27/CH04634 ._CH',             # 18
        'ED6_DT27/CH04635 ._CH',             # 19
        'ED6_DT27/CH04636 ._CH',             # 1A
        'ED6_DT27/CH04633 ._CH',             # 1B
        'ED6_DT27/CH04633 ._CH',             # 1C
        'ED6_DT27/CH04633 ._CH',             # 1D
        'ED6_DT27/CH04640 ._CH',             # 1E
        'ED6_DT27/CH04641 ._CH',             # 1F
        'ED6_DT27/CH04642 ._CH',             # 20
        'ED6_DT27/CH04643 ._CH',             # 21
        'ED6_DT27/CH04644 ._CH',             # 22
        'ED6_DT27/CH04645 ._CH',             # 23
        'ED6_DT27/CH04646 ._CH',             # 24
        'ED6_DT27/CH04643 ._CH',             # 25
        'ED6_DT27/CH04643 ._CH',             # 26
        'ED6_DT27/CH04643 ._CH',             # 27
        'ED6_DT27/CH04750 ._CH',             # 28
        'ED6_DT27/CH04751 ._CH',             # 29
        'ED6_DT27/CH04752 ._CH',             # 2A
        'ED6_DT27/CH04753 ._CH',             # 2B
        'ED6_DT27/CH04754 ._CH',             # 2C
        'ED6_DT27/CH04755 ._CH',             # 2D
        'ED6_DT27/CH04756 ._CH',             # 2E
        'ED6_DT27/CH04753 ._CH',             # 2F
        'ED6_DT27/CH04753 ._CH',             # 30
        'ED6_DT27/CH04753 ._CH',             # 31
        'ED6_DT27/CH04820 ._CH',             # 32
        'ED6_DT27/CH04821 ._CH',             # 33
        'ED6_DT27/CH04822 ._CH',             # 34
        'ED6_DT27/CH04823 ._CH',             # 35
        'ED6_DT27/CH04824 ._CH',             # 36
        'ED6_DT27/CH04825 ._CH',             # 37
        'ED6_DT27/CH04826 ._CH',             # 38
        'ED6_DT27/CH04823 ._CH',             # 39
        'ED6_DT27/CH04823 ._CH',             # 3A
        'ED6_DT27/CH04823 ._CH',             # 3B
    )

    AddCharChipPat(
        'ED6_DT27/CH04610P._CP',             # 00
        'ED6_DT27/CH04611P._CP',             # 01
        'ED6_DT27/CH04612P._CP',             # 02
        'ED6_DT27/CH04613P._CP',             # 03
        'ED6_DT27/CH04614P._CP',             # 04
        'ED6_DT27/CH04615P._CP',             # 05
        'ED6_DT27/CH04616P._CP',             # 06
        'ED6_DT27/CH04613P._CP',             # 07
        'ED6_DT27/CH04613P._CP',             # 08
        'ED6_DT27/CH04613P._CP',             # 09
        'ED6_DT27/CH04620P._CP',             # 0A
        'ED6_DT27/CH04621P._CP',             # 0B
        'ED6_DT27/CH04622P._CP',             # 0C
        'ED6_DT27/CH04623P._CP',             # 0D
        'ED6_DT27/CH04624P._CP',             # 0E
        'ED6_DT27/CH04625P._CP',             # 0F
        'ED6_DT27/CH04626P._CP',             # 10
        'ED6_DT27/CH04623P._CP',             # 11
        'ED6_DT27/CH04623P._CP',             # 12
        'ED6_DT27/CH04623P._CP',             # 13
        'ED6_DT27/CH04630P._CP',             # 14
        'ED6_DT27/CH04631P._CP',             # 15
        'ED6_DT27/CH04632P._CP',             # 16
        'ED6_DT27/CH04633P._CP',             # 17
        'ED6_DT27/CH04634P._CP',             # 18
        'ED6_DT27/CH04635P._CP',             # 19
        'ED6_DT27/CH04636P._CP',             # 1A
        'ED6_DT27/CH04633P._CP',             # 1B
        'ED6_DT27/CH04633P._CP',             # 1C
        'ED6_DT27/CH04633P._CP',             # 1D
        'ED6_DT27/CH04640P._CP',             # 1E
        'ED6_DT27/CH04641P._CP',             # 1F
        'ED6_DT27/CH04642P._CP',             # 20
        'ED6_DT27/CH04643P._CP',             # 21
        'ED6_DT27/CH04644P._CP',             # 22
        'ED6_DT27/CH04645P._CP',             # 23
        'ED6_DT27/CH04646P._CP',             # 24
        'ED6_DT27/CH04643P._CP',             # 25
        'ED6_DT27/CH04643P._CP',             # 26
        'ED6_DT27/CH04643P._CP',             # 27
        'ED6_DT27/CH04750P._CP',             # 28
        'ED6_DT27/CH04751P._CP',             # 29
        'ED6_DT27/CH04752P._CP',             # 2A
        'ED6_DT27/CH04753P._CP',             # 2B
        'ED6_DT27/CH04754P._CP',             # 2C
        'ED6_DT27/CH04755P._CP',             # 2D
        'ED6_DT27/CH04756P._CP',             # 2E
        'ED6_DT27/CH04753P._CP',             # 2F
        'ED6_DT27/CH04753P._CP',             # 30
        'ED6_DT27/CH04753P._CP',             # 31
        'ED6_DT27/CH04820P._CP',             # 32
        'ED6_DT27/CH04821P._CP',             # 33
        'ED6_DT27/CH04822P._CP',             # 34
        'ED6_DT27/CH04823P._CP',             # 35
        'ED6_DT27/CH04824P._CP',             # 36
        'ED6_DT27/CH04825P._CP',             # 37
        'ED6_DT27/CH04826P._CP',             # 38
        'ED6_DT27/CH04823P._CP',             # 39
        'ED6_DT27/CH04823P._CP',             # 3A
        'ED6_DT27/CH04823P._CP',             # 3B
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 11,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 12,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 14,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 15,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 16,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 17,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 53,
        ChipIndex           = 0x35,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 54,
        ChipIndex           = 0x36,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 55,
        ChipIndex           = 0x37,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 56,
        ChipIndex           = 0x38,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 18,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )


    ScpFunction(
        "Function_0_7CA",          # 00, 0
        "Function_1_7CB",          # 01, 1
        "Function_2_7CC",          # 02, 2
        "Function_3_842",          # 03, 3
        "Function_4_85C",          # 04, 4
        "Function_5_87B",          # 05, 5
        "Function_6_896",          # 06, 6
        "Function_7_8E3",          # 07, 7
        "Function_8_8FD",          # 08, 8
        "Function_9_9BD",          # 09, 9
        "Function_10_9D7",         # 0A, 10
        "Function_11_A97",         # 0B, 11
        "Function_12_AB1",         # 0C, 12
        "Function_13_B71",         # 0D, 13
        "Function_14_B8B",         # 0E, 14
        "Function_15_C47",         # 0F, 15
        "Function_16_C61",         # 10, 16
        "Function_17_D1D",         # 11, 17
        "Function_18_D37",         # 12, 18
        "Function_19_DF3",         # 13, 19
    )


    def Function_0_7CA(): pass

    label("Function_0_7CA")

    Return()

    # Function_0_7CA end

    def Function_1_7CB(): pass

    label("Function_1_7CB")

    Return()

    # Function_1_7CB end

    def Function_2_7CC(): pass

    label("Function_2_7CC")

    RunExpression(0x65, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x65), scpexpr(EXPR_END)),
        (0, "loc_801"),
        (1, "loc_809"),
        (2, "loc_811"),
        (3, "loc_819"),
        (4, "loc_821"),
        (5, "loc_829"),
        (6, "loc_831"),
        (7, "loc_839"),
        (SWITCH_DEFAULT, "loc_841"),
    )


    label("loc_801")

    Sleep(100)
    Jump("loc_841")

    label("loc_809")

    Sleep(121)
    Jump("loc_841")

    label("loc_811")

    Sleep(132)
    Jump("loc_841")

    label("loc_819")

    Sleep(153)
    Jump("loc_841")

    label("loc_821")

    Sleep(164)
    Jump("loc_841")

    label("loc_829")

    Sleep(175)
    Jump("loc_841")

    label("loc_831")

    Sleep(186)
    Jump("loc_841")

    label("loc_839")

    Sleep(197)
    Jump("loc_841")

    label("loc_841")

    Return()

    # Function_2_7CC end

    def Function_3_842(): pass

    label("Function_3_842")

    Call(0, 2)

    label("loc_846")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85B")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("loc_846")

    label("loc_85B")

    Return()

    # Function_3_842 end

    def Function_4_85C(): pass

    label("Function_4_85C")

    Call(0, 2)

    label("loc_860")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87A")
    OP_99(0xFE, 0x0, 0x0, 0x5DC)
    Sleep(500)
    Jump("loc_860")

    label("loc_87A")

    Return()

    # Function_4_85C end

    def Function_5_87B(): pass

    label("Function_5_87B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_895")
    OP_99(0xFE, 0x0, 0x3, 0x3E8)
    Sleep(500)
    Jump("Function_5_87B")

    label("loc_895")

    Return()

    # Function_5_87B end

    def Function_6_896(): pass

    label("Function_6_896")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E2")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_6_896")

    label("loc_8E2")

    Return()

    # Function_6_896 end

    def Function_7_8E3(): pass

    label("Function_7_8E3")

    Call(0, 2)

    label("loc_8E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FC")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_8E7")

    label("loc_8FC")

    Return()

    # Function_7_8E3 end

    def Function_8_8FD(): pass

    label("Function_8_8FD")

    Call(0, 2)

    label("loc_901")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9BC")
    SetChrChipByIndex(0xFE, 5)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 6)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("loc_901")

    label("loc_9BC")

    Return()

    # Function_8_8FD end

    def Function_9_9BD(): pass

    label("Function_9_9BD")

    Call(0, 2)

    label("loc_9C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D6")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_9C1")

    label("loc_9D6")

    Return()

    # Function_9_9BD end

    def Function_10_9D7(): pass

    label("Function_10_9D7")

    Call(0, 2)

    label("loc_9DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A96")
    SetChrChipByIndex(0xFE, 15)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 16)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("loc_9DB")

    label("loc_A96")

    Return()

    # Function_10_9D7 end

    def Function_11_A97(): pass

    label("Function_11_A97")

    Call(0, 2)

    label("loc_A9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB0")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_A9B")

    label("loc_AB0")

    Return()

    # Function_11_A97 end

    def Function_12_AB1(): pass

    label("Function_12_AB1")

    Call(0, 2)

    label("loc_AB5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B70")
    SetChrChipByIndex(0xFE, 25)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 26)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("loc_AB5")

    label("loc_B70")

    Return()

    # Function_12_AB1 end

    def Function_13_B71(): pass

    label("Function_13_B71")

    Call(0, 2)

    label("loc_B75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8A")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_B75")

    label("loc_B8A")

    Return()

    # Function_13_B71 end

    def Function_14_B8B(): pass

    label("Function_14_B8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C46")
    SetChrChipByIndex(0xFE, 35)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 36)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_14_B8B")

    label("loc_C46")

    Return()

    # Function_14_B8B end

    def Function_15_C47(): pass

    label("Function_15_C47")

    Call(0, 2)

    label("loc_C4B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C60")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_C4B")

    label("loc_C60")

    Return()

    # Function_15_C47 end

    def Function_16_C61(): pass

    label("Function_16_C61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D1C")
    SetChrChipByIndex(0xFE, 45)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 46)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_16_C61")

    label("loc_D1C")

    Return()

    # Function_16_C61 end

    def Function_17_D1D(): pass

    label("Function_17_D1D")

    Call(0, 2)

    label("loc_D21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D36")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_D21")

    label("loc_D36")

    Return()

    # Function_17_D1D end

    def Function_18_D37(): pass

    label("Function_18_D37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF2")
    SetChrChipByIndex(0xFE, 55)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    SetChrChipByIndex(0xFE, 56)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)
    Sleep(1000)
    Jump("Function_18_D37")

    label("loc_DF2")

    Return()

    # Function_18_D37 end

    def Function_19_DF3(): pass

    label("Function_19_DF3")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "呜喵。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_DF3 end

    SaveToFile()

Try(main)
