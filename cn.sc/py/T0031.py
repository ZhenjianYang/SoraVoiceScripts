from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0031   ._SN',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'CH00000艾丝蒂尔',                      # 9
        'CH00010约修亚',                        # 10
        'CH00020雪拉',                          # 11
        'CH00030奥利维尔',                      # 12
        'CH00040科洛丝',                        # 13
        '表情',                                 # 14
        'CH00050阿加特',                        # 15
        'CH00060提妲',                          # 16
        'CH00070金',                            # 17
        'CH02000卡西乌斯老爸',                  # 18
        'CH02010艾莉茜雅女王',                  # 19
        'CH02020Ｄｒ．拉赛尔',                  # 20
        'CH02030理查德上校',                    # 21
        'CH02040莱维',                          # 22
        'CH02050亚鲁瓦教授（怀斯曼）',          # 23
        'CH02060记者奈尔',                      # 24
        'CH02070摄影师朵洛希',                  # 25
        'CH02080摩尔根将军',                    # 26
        'CH02090亲卫队尤莉亚',                  # 27
        'CH02100原特务兵凯诺娜队长',            # 28
        'CH02110空贼团长男多伦',                # 29
        'CH02120空贼团次男吉尔',                # 30
        'CH02130空贼团妹乔丝特',                # 31
        'CH02140杜南公爵',                      # 32
        'CH02190穆拉',                          # 33
        'CH02200洛伦斯',                        # 34
        'CH02210艾丝蒂尔１１岁',                # 35
        'CH02220约修亚１１岁',                  # 36
        'CH02230女佣艾丝蒂尔',                  # 37
        'CH02240女佣约修亚',                    # 38
        'CH02260骑士艾丝蒂尔',                  # 39
        'CH02270骑士科洛丝',                    # 40
        'CH02280公主约修亚',                    # 41
        'CH02290温泉约修亚',                    # 42
        'CH02300温泉艾丝蒂尔',                  # 43
        'CH02310温泉提妲',                      # 44
        'CH02320基库',                          # 45
        'CH02330学生乔丝特',                    # 46
        'CH02340公主科洛丝',                    # 47
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
        'ED6_DT07/CH00000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT07/CH02000 ._CH',             # 08
        'ED6_DT07/CH02010 ._CH',             # 09
        'ED6_DT07/CH02020 ._CH',             # 0A
        'ED6_DT07/CH02030 ._CH',             # 0B
        'ED6_DT07/CH02040 ._CH',             # 0C
        'ED6_DT07/CH02050 ._CH',             # 0D
        'ED6_DT07/CH02060 ._CH',             # 0E
        'ED6_DT07/CH02070 ._CH',             # 0F
        'ED6_DT07/CH02080 ._CH',             # 10
        'ED6_DT07/CH02090 ._CH',             # 11
        'ED6_DT07/CH02100 ._CH',             # 12
        'ED6_DT07/CH02110 ._CH',             # 13
        'ED6_DT07/CH02120 ._CH',             # 14
        'ED6_DT07/CH02130 ._CH',             # 15
        'ED6_DT07/CH02140 ._CH',             # 16
        'ED6_DT07/CH02190 ._CH',             # 17
        'ED6_DT07/CH02200 ._CH',             # 18
        'ED6_DT07/CH02210 ._CH',             # 19
        'ED6_DT07/CH02220 ._CH',             # 1A
        'ED6_DT07/CH02230 ._CH',             # 1B
        'ED6_DT07/CH02240 ._CH',             # 1C
        'ED6_DT07/CH02250 ._CH',             # 1D
        'ED6_DT07/CH02260 ._CH',             # 1E
        'ED6_DT07/CH02270 ._CH',             # 1F
        'ED6_DT07/CH02280 ._CH',             # 20
        'ED6_DT07/CH02290 ._CH',             # 21
        'ED6_DT07/CH02300 ._CH',             # 22
        'ED6_DT07/CH02310 ._CH',             # 23
        'ED6_DT07/CH02320 ._CH',             # 24
        'ED6_DT07/CH02330 ._CH',             # 25
        'ED6_DT07/CH02340 ._CH',             # 26
    )

    AddCharChipPat(
        'ED6_DT07/CH00000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT07/CH02000P._CP',             # 08
        'ED6_DT07/CH02010P._CP',             # 09
        'ED6_DT07/CH02020P._CP',             # 0A
        'ED6_DT07/CH02030P._CP',             # 0B
        'ED6_DT07/CH02040P._CP',             # 0C
        'ED6_DT07/CH02050P._CP',             # 0D
        'ED6_DT07/CH02060P._CP',             # 0E
        'ED6_DT07/CH02070P._CP',             # 0F
        'ED6_DT07/CH02080P._CP',             # 10
        'ED6_DT07/CH02090P._CP',             # 11
        'ED6_DT07/CH02100P._CP',             # 12
        'ED6_DT07/CH02110P._CP',             # 13
        'ED6_DT07/CH02120P._CP',             # 14
        'ED6_DT07/CH02130P._CP',             # 15
        'ED6_DT07/CH02140P._CP',             # 16
        'ED6_DT07/CH02190P._CP',             # 17
        'ED6_DT07/CH02200P._CP',             # 18
        'ED6_DT07/CH02210P._CP',             # 19
        'ED6_DT07/CH02220P._CP',             # 1A
        'ED6_DT07/CH02230P._CP',             # 1B
        'ED6_DT07/CH02240P._CP',             # 1C
        'ED6_DT07/CH02250P._CP',             # 1D
        'ED6_DT07/CH02260P._CP',             # 1E
        'ED6_DT07/CH02270P._CP',             # 1F
        'ED6_DT07/CH02280P._CP',             # 20
        'ED6_DT07/CH02290P._CP',             # 21
        'ED6_DT07/CH02300P._CP',             # 22
        'ED6_DT07/CH02310P._CP',             # 23
        'ED6_DT07/CH02320P._CP',             # 24
        'ED6_DT07/CH02330P._CP',             # 25
        'ED6_DT07/CH02340P._CP',             # 26
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 15000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 28000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 32000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )


    ScpFunction(
        "Function_0_6C2",          # 00, 0
        "Function_1_6C3",          # 01, 1
        "Function_2_6C4",          # 02, 2
        "Function_3_6DA",          # 03, 3
        "Function_4_6F0",          # 04, 4
        "Function_5_706",          # 05, 5
        "Function_6_72A",          # 06, 6
        "Function_7_74E",          # 07, 7
        "Function_8_761",          # 08, 8
        "Function_9_77E",          # 09, 9
        "Function_10_7D9",         # 0A, 10
        "Function_11_928",         # 0B, 11
        "Function_12_AF3",         # 0C, 12
        "Function_13_BA4",         # 0D, 13
        "Function_14_C47",         # 0E, 14
        "Function_15_CFF",         # 0F, 15
        "Function_16_DCB",         # 10, 16
        "Function_17_E8E",         # 11, 17
        "Function_18_EE0",         # 12, 18
        "Function_19_F50",         # 13, 19
        "Function_20_FA2",         # 14, 20
        "Function_21_1004",        # 15, 21
        "Function_22_1065",        # 16, 22
        "Function_23_116D",        # 17, 23
        "Function_24_11ED",        # 18, 24
        "Function_25_1280",        # 19, 25
        "Function_26_12D2",        # 1A, 26
        "Function_27_1315",        # 1B, 27
        "Function_28_1385",        # 1C, 28
        "Function_29_13C3",        # 1D, 29
        "Function_30_1454",        # 1E, 30
        "Function_31_1479",        # 1F, 31
        "Function_32_153D",        # 20, 32
        "Function_33_158F",        # 21, 33
        "Function_34_160B",        # 22, 34
        "Function_35_1699",        # 23, 35
        "Function_36_16BE",        # 24, 36
        "Function_37_16F2",        # 25, 37
        "Function_38_170E",        # 26, 38
        "Function_39_1798",        # 27, 39
        "Function_40_17EA",        # 28, 40
        "Function_41_1912",        # 29, 41
        "Function_42_1A0B",        # 2A, 42
        "Function_43_1AA3",        # 2B, 43
        "Function_44_1B84",        # 2C, 44
        "Function_45_1C41",        # 2D, 45
        "Function_46_1CB3",        # 2E, 46
        "Function_47_1D0E",        # 2F, 47
        "Function_48_1DA4",        # 30, 48
    )


    def Function_0_6C2(): pass

    label("Function_0_6C2")

    Return()

    # Function_0_6C2 end

    def Function_1_6C3(): pass

    label("Function_1_6C3")

    Return()

    # Function_1_6C3 end

    def Function_2_6C4(): pass

    label("Function_2_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6C4")

    label("loc_6D9")

    Return()

    # Function_2_6C4 end

    def Function_3_6DA(): pass

    label("Function_3_6DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EF")
    OP_99(0xFE, 0x0, 0x7, 0x7D0)
    Jump("Function_3_6DA")

    label("loc_6EF")

    Return()

    # Function_3_6DA end

    def Function_4_6F0(): pass

    label("Function_4_6F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705")
    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("Function_4_6F0")

    label("loc_705")

    Return()

    # Function_4_6F0 end

    def Function_5_706(): pass

    label("Function_5_706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_729")
    OP_8D(0xFE, 4000, 20000, 24000, 30000, 1500)
    Jump("Function_5_706")

    label("loc_729")

    Return()

    # Function_5_706 end

    def Function_6_72A(): pass

    label("Function_6_72A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_8D(0xFE, 22000, 20000, 42000, 30000, 1500)
    Jump("Function_6_72A")

    label("loc_74D")

    Return()

    # Function_6_72A end

    def Function_7_74E(): pass

    label("Function_7_74E")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "呜喵。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_74E end

    def Function_8_761(): pass

    label("Function_8_761")

    TalkBegin(0xFE)
    OP_1D(0x4)

    ChrTalk(    #1
        0xFE,
        "ＢＧＭ改变喵。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_761 end

    def Function_9_77E(): pass

    label("Function_9_77E")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        "ＢＧＭ降低喵。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "ＢＧＭ更降低喵。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "ＢＧＭ回复原状喵。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_77E end

    def Function_10_7D9(): pass

    label("Function_10_7D9")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0xFE,
        "#000F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#001F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#002F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#003F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#004F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "#005F发怒１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#006F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "#007F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "#008F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "#009F发怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "#500F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#501F悠闲\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "#502F哼哼\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "#503F害羞２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "#504F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#505F嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "#506F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "#507F挑拨\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "#508F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "#509F眯缝眼\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_7D9 end

    def Function_11_928(): pass

    label("Function_11_928")

    TalkBegin(0xFE)

    ChrTalk(    #25
        0xFE,
        "#010F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#011F笑容１（有企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "#012F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#013F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "#014F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#015F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "#016F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#017F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "#018F害羞（发牢骚）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#019F笑容２（发怒）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "#510F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#511F真的害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#512F笑容３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#513F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#515F暗示解除后叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "#516F暗示解除后发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#517FED笑容４\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "#518FED通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#519FED低头\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#590FED低头惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "#591F暗示解除后叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#592FED笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_928 end

    def Function_12_AF3(): pass

    label("Function_12_AF3")

    TalkBegin(0xFE)

    ChrTalk(    #49
        0xFE,
        "#020F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "#021F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#022F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#023F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#024F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#025F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#026F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "#027F诱惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#028F喝醉（好心情）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#029F喝醉（不高兴）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_AF3 end

    def Function_13_BA4(): pass

    label("Function_13_BA4")

    TalkBegin(0xFE)
    OP_62(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    ChrTalk(    #59
        0xFE,
        "#030F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "#031F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "#032F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "#033F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#034F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "#035F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "#036F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#037F喝醉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#038F烂醉\x02",
    )

    CloseMessageWindow()
    OP_63(0xB)
    TalkEnd(0xFE)
    Return()

    # Function_13_BA4 end

    def Function_14_C47(): pass

    label("Function_14_C47")

    TalkBegin(0xFE)

    ChrTalk(    #68
        0xFE,
        "#040F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "#041F笑容１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "#042F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#043F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#044F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "#045F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "#046F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#047F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#048F笑容２（小姐ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#049F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_C47 end

    def Function_15_CFF(): pass

    label("Function_15_CFF")

    TalkBegin(0xFE)

    ChrTalk(    #78
        0xFE,
        "#050F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "#051F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "#052F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "#053F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "#054F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "#055F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "#056F痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "#057F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#058F毒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#059F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "#550F可恶～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "#551F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "#552F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_CFF end

    def Function_16_DCB(): pass

    label("Function_16_DCB")

    TalkBegin(0xFE)

    ChrTalk(    #91
        0xFE,
        "#060F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#061F笑容１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#062F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "#063F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "#064F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "#065F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#066F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#067F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#068F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#069F哭泣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "#560F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#561F叹息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_DCB end

    def Function_17_E8E(): pass

    label("Function_17_E8E")

    TalkBegin(0xFE)

    ChrTalk(    #103
        0xFE,
        "#070F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#071F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#072F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#073F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#074F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_E8E end

    def Function_18_EE0(): pass

    label("Function_18_EE0")

    TalkBegin(0xFE)

    ChrTalk(    #108
        0xFE,
        "#080F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "#081F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#082F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#083F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "#084F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#085F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "#086F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_EE0 end

    def Function_19_F50(): pass

    label("Function_19_F50")

    TalkBegin(0xFE)

    ChrTalk(    #115
        0xFE,
        "#090F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "#091F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "#092F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "#093F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "#094F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_F50 end

    def Function_20_FA2(): pass

    label("Function_20_FA2")

    TalkBegin(0xFE)

    ChrTalk(    #120
        0xFE,
        "#100F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "#101F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#102F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "#103F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#104F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#105F笑容2\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_FA2 end

    def Function_21_1004(): pass

    label("Function_21_1004")

    TalkBegin(0xFE)

    ChrTalk(    #126
        0xFE,
        "#110F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#111F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#112F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#113F惊讶\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "#114F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#115F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1004 end

    def Function_22_1065(): pass

    label("Function_22_1065")

    TalkBegin(0xFE)

    ChrTalk(    #132
        0xFE,
        "#120F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#121F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "#122F回头\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "#123F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#124F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "#280F洛伦斯版本通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "#281F洛伦斯版本合口\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "#282F洛伦斯（没见过）通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "#283F洛伦斯（没见过）通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "#284F洛伦斯（没见过）笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "#285F洛伦斯（没见过）闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_1065 end

    def Function_23_116D(): pass

    label("Function_23_116D")

    TalkBegin(0xFE)

    ChrTalk(    #143
        0xFE,
        "#130F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "#131F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "#132F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "#133FED用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "#134FED用笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "#135FED用认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "#136FED用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_116D end

    def Function_24_11ED(): pass

    label("Function_24_11ED")

    TalkBegin(0xFE)

    ChrTalk(    #150
        0xFE,
        "#140F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "#141F笑容１（诡笑）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "#142F怀疑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "#143F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "#144F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "#145F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "#146F喝醉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "#147F笑容２（满面）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_11ED end

    def Function_25_1280(): pass

    label("Function_25_1280")

    TalkBegin(0xFE)

    ChrTalk(    #158
        0xFE,
        "#150F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "#151F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "#152F呜呜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "#153F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "#154F困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_1280 end

    def Function_26_12D2(): pass

    label("Function_26_12D2")

    TalkBegin(0xFE)

    ChrTalk(    #163
        0xFE,
        "#160F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "#161F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "#162F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "#163F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_12D2 end

    def Function_27_1315(): pass

    label("Function_27_1315")

    TalkBegin(0xFE)

    ChrTalk(    #167
        0xFE,
        "#170F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "#171F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "#172F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "#173F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "#174F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#175F忧郁\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "#176F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1315 end

    def Function_28_1385(): pass

    label("Function_28_1385")

    TalkBegin(0xFE)

    ChrTalk(    #174
        0xFE,
        "#180F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "#181F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "#182F通常２（温柔）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_1385 end

    def Function_29_13C3(): pass

    label("Function_29_13C3")

    TalkBegin(0xFE)

    ChrTalk(    #177
        0xFE,
        "#190F通常（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "#191F笑容（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "#192F惊愕（正常）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "#193F通常（发狂）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "#194F笑容（发狂）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "#195F发怒（发狂）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_13C3 end

    def Function_30_1454(): pass

    label("Function_30_1454")

    TalkBegin(0xFE)

    ChrTalk(    #183
        0xFE,
        "#200F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "#201F认真\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_1454 end

    def Function_31_1479(): pass

    label("Function_31_1479")

    TalkBegin(0xFE)

    ChrTalk(    #185
        0xFE,
        "#210F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "#211F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "#212F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "#213F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "#214F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "#215F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "#216F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "#217F变装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "#218F变装笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "#219F变装空贼表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "#410F变装白痴笑容\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_1479 end

    def Function_32_153D(): pass

    label("Function_32_153D")

    TalkBegin(0xFE)

    ChrTalk(    #196
        0xFE,
        "#290F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "#291F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "#292F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "#293F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "#294F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_153D end

    def Function_33_158F(): pass

    label("Function_33_158F")

    TalkBegin(0xFE)

    ChrTalk(    #201
        0xFE,
        "#300F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#301F无表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "#302F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "#303F痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "#304F波澜不惊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "#305F寝颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "#306F寝颜（醒来）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_158F end

    def Function_34_160B(): pass

    label("Function_34_160B")

    TalkBegin(0xFE)

    ChrTalk(    #208
        0xFE,
        "#220F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "#221F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "#222F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#223F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "#224F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "#225F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "#226F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "#227F喝醉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        "#228F气绝\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_160B end

    def Function_35_1699(): pass

    label("Function_35_1699")

    TalkBegin(0xFE)

    ChrTalk(    #217
        0xFE,
        "#310F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "#311F笑容\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1699 end

    def Function_36_16BE(): pass

    label("Function_36_16BE")

    TalkBegin(0xFE)

    ChrTalk(    #219
        0xFE,
        "#270F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "#271F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "#272F瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_16BE end

    def Function_37_16F2(): pass

    label("Function_37_16F2")

    TalkBegin(0xFE)

    ChrTalk(    #222
        0xFE,
        "#280F洛伦斯版本\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_16F2 end

    def Function_38_170E(): pass

    label("Function_38_170E")

    TalkBegin(0xFE)

    ChrTalk(    #223
        0xFE,
        "#320F通常1（优先）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "#321F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "#322F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "#323F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "#324F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        "#325F通常2（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "#326F发怒２（唔）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_170E end

    def Function_39_1798(): pass

    label("Function_39_1798")

    TalkBegin(0xFE)

    ChrTalk(    #230
        0xFE,
        "#330F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "#331F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "#332F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "#333F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "#334F叹息\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_1798 end

    def Function_40_17EA(): pass

    label("Function_40_17EA")

    TalkBegin(0xFE)

    ChrTalk(    #235
        0xFE,
        "#340F通常（悠闲）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "#341F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "#342F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "#343F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "#344F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "#345F发怒１（叫喊）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#346F通常（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "#347F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "#348F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        "#349F发怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "#840F戏剧用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "#841F戏剧用认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#842F戏剧用惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "#843F戏剧用叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "#844F戏剧用瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_17EA end

    def Function_41_1912(): pass

    label("Function_41_1912")

    TalkBegin(0xFE)

    ChrTalk(    #250
        0xFE,
        "#350F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "#351F笑容１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "#352F认真·戏剧用通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "#353F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "#354F惊愕·戏剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "#355F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "#356F发怒·戏剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "#357F瞑目·戏剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "#358F笑容２（小姐ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "#359F悲哀２（深刻）·戏剧用\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#850F戏剧用苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1912 end

    def Function_42_1A0B(): pass

    label("Function_42_1A0B")

    TalkBegin(0xFE)

    ChrTalk(    #261
        0xFE,
        "#360F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "#361F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "#362F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "#363F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "#364F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "#365F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "#366F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "#367F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        "#368F害羞（发牢骚）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1A0B end

    def Function_43_1AA3(): pass

    label("Function_43_1AA3")

    TalkBegin(0xFE)

    ChrTalk(    #270
        0xFE,
        "#370F通常１（悠闲）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "#371F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "#372F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "#373F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "#374F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "#375F发怒１（叫喊）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "#376F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "#377F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "#378F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "#379F发怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "#440F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "#441F赤面\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1AA3 end

    def Function_44_1B84(): pass

    label("Function_44_1B84")

    TalkBegin(0xFE)

    ChrTalk(    #282
        0xFE,
        "#380F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "#381F笑容１（有企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "#382F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "#383F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "#384F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "#385F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "#386F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "#387F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "#388F害羞（发牢骚）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "#389F笑容２（发怒）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_1B84 end

    def Function_45_1C41(): pass

    label("Function_45_1C41")

    TalkBegin(0xFE)

    ChrTalk(    #292
        0xFE,
        "#390F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "#391F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "#392F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#393F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "#394F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "#395F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "#396F通常２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_1C41 end

    def Function_46_1CB3(): pass

    label("Function_46_1CB3")

    TalkBegin(0xFE)

    ChrTalk(    #299
        0xFE,
        "#217F变装通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "#218F变装笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "#219F变装空贼表情\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "#410F变装白痴笑容\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_1CB3 end

    def Function_47_1D0E(): pass

    label("Function_47_1D0E")

    TalkBegin(0xFE)

    ChrTalk(    #303
        0xFE,
        "#400F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "#401F笑容（小姐ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "#402F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "#403F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "#404F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "#405F嘿嘿\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "#406F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "#407F发怒\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_1D0E end

    def Function_48_1DA4(): pass

    label("Function_48_1DA4")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E7")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "表情测试\x01",          # 0
            "假名显示测试\x01",      # 1
            "音量测试\x01",          # 2
            "取消\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E18"),
        (1, "loc_2101"),
        (2, "loc_2280"),
        (SWITCH_DEFAULT, "loc_22D7"),
    )


    label("loc_1E18")

    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)

    AnonymousTalk(    #311
        "\x07\x00#020F？\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(    #312
        "\x07\x00#020F！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(    #313
        "\x07\x00#020F⊙\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    AnonymousTalk(    #314
        "\x07\x00#020F㈱\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #315
        "\x07\x00#020F生气\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #316
        "\x07\x00#020F焦躁\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #317
        "\x07\x00#020F冷汗\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    AnonymousTalk(    #318
        "\x07\x00#020F脸色发青\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    AnonymousTalk(    #319
        "\x07\x00#020F…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)

    AnonymousTalk(    #320
        "\x07\x00#020FＺｚｚ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)

    AnonymousTalk(    #321
        "\x07\x00#020F闪烁\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    AnonymousTalk(    #322
        "\x07\x00#020F哈哈\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    AnonymousTalk(    #323
        "\x07\x00#020F啪\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    AnonymousTalk(    #324
        "\x07\x00#020F汗汗\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)

    AnonymousTalk(    #325
        "\x07\x00#020F哐当！\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)

    AnonymousTalk(    #326
        "\x07\x00#020F气绝\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    AnonymousTalk(    #327
        "\x07\x00#020F闪闪\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 1900, 0x33, 0x35, 0xC8, 0x0)

    AnonymousTalk(    #328
        "\x07\x00#020F咕噜咕噜\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x3B, 0x3C, 0xFA, 0x2)

    AnonymousTalk(    #329
        "\x07\x00#020F搭话\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x3D, 0x3E, 0xFA, 0x2)

    AnonymousTalk(    #330
        "\x07\x00#020F钓鱼点\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_2101")


    ChrTalk(    #331
        0xFE,
        "#040F假名测试。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        (
            "#040F导力器。游击士。\x01",
            "开拓时代的物语。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "#040F导力引擎、导力炮（←文中限定）。\x01",
            "游击士协会、七耀石、噬身之蛇。\x01",
            "七至宝、『七至宝』、七 至 宝（←保留中）。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "#040F『银闪之雪拉扎德』、女神。\x01",
            "养父、王都格兰赛尔（←文中限定）。\x01",
            "导力魔法、結晶回路、翠耀石。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "#040F将文中限定使用在文首就会发生类似以下悲剧。\x01",
            "王都（←文中限定）。\x01",
            "导力炮（←文中限定）。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_2280")


    ChrTalk(    #336
        0xFE,
        "ＢＧＭ降低喵。\x02",
    )

    OP_1F(0x5A, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "ＢＧＭ更降低喵。\x02",
    )

    OP_1F(0x46, 0x7D0)
    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "ＢＧＭ回复原状喵。\x02",
    )

    OP_1F(0x64, 0x7D0)
    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_22D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22E4")

    label("loc_22E4")

    Jump("loc_1DB1")

    label("loc_22E7")

    TalkEnd(0xFE)
    Return()

    # Function_48_1DA4 end

    SaveToFile()

Try(main)
