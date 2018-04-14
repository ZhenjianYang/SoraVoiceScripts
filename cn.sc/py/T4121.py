from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4121_1 ._SN',
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
        '艾南',                                 # 9
        '雪拉扎德',                             # 10
        '阿加特',                               # 11
        '奥利维尔',                             # 12
        '科洛丝',                               # 13
        '提妲',                                 # 14
        '金',                                   # 15
        '希德中校',                             # 16
        '亚妮拉丝',                             # 17
        '嘉瑟',                                 # 18
        '诺娜',                                 # 19
        '伯登',                                 # 20
        '拉塔娜',                               # 21
        '托朗老人',                             # 22
        '蒂库',                                 # 23
        '拉尔斯',                               # 24
        '托伊',                                 # 25
        '钓鱼人',                               # 26
        '罗伊德',                               # 27
        '拜舍尔',                               # 28
        '塞森',                                 # 29
        '多姆',                                 # 30
        '史帕德',                               # 31
        '夏伊',                                 # 32
        '科蕾蒂',                               # 33
        '彭萨',                                 # 34
        '拜舍尔',                               # 35
        '比尔爷爷',                             # 36
        '伊鲁妮婆婆',                           # 37
        '迪克斯',                               # 38
        '塔巴莎',                               # 39
        '萨米',                                 # 40
        '吉恩',                                 # 41
        '钓鱼人',                               # 42
        '巴拉尔',                               # 43
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00073 ._CH',             # 08
        'ED6_DT27/CH03590 ._CH',             # 09
        'ED6_DT07/CH01200 ._CH',             # 0A
        'ED6_DT07/CH01630 ._CH',             # 0B
        'ED6_DT07/CH01020 ._CH',             # 0C
        'ED6_DT07/CH01463 ._CH',             # 0D
        'ED6_DT07/CH01270 ._CH',             # 0E
        'ED6_DT07/CH01050 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01160 ._CH',             # 12
        'ED6_DT07/CH01470 ._CH',             # 13
        'ED6_DT07/CH01060 ._CH',             # 14
        'ED6_DT07/CH01140 ._CH',             # 15
        'ED6_DT07/CH01040 ._CH',             # 16
        'ED6_DT07/CH01680 ._CH',             # 17
        'ED6_DT07/CH01690 ._CH',             # 18
        'ED6_DT07/CH01150 ._CH',             # 19
        'ED6_DT07/CH01140 ._CH',             # 1A
        'ED6_DT07/CH01460 ._CH',             # 1B
        'ED6_DT07/CH01490 ._CH',             # 1C
        'ED6_DT07/CH01180 ._CH',             # 1D
        'ED6_DT07/CH01120 ._CH',             # 1E
        'ED6_DT07/CH01130 ._CH',             # 1F
        'ED6_DT07/CH00023 ._CH',             # 20
        'ED6_DT07/CH00053 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00073P._CP',             # 08
        'ED6_DT27/CH03590P._CP',             # 09
        'ED6_DT07/CH01200P._CP',             # 0A
        'ED6_DT07/CH01630P._CP',             # 0B
        'ED6_DT07/CH01020P._CP',             # 0C
        'ED6_DT07/CH01463P._CP',             # 0D
        'ED6_DT07/CH01270P._CP',             # 0E
        'ED6_DT07/CH01050P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01160P._CP',             # 12
        'ED6_DT07/CH01470P._CP',             # 13
        'ED6_DT07/CH01060P._CP',             # 14
        'ED6_DT07/CH01140P._CP',             # 15
        'ED6_DT07/CH01040P._CP',             # 16
        'ED6_DT07/CH01680P._CP',             # 17
        'ED6_DT07/CH01690P._CP',             # 18
        'ED6_DT07/CH01150P._CP',             # 19
        'ED6_DT07/CH01140P._CP',             # 1A
        'ED6_DT07/CH01460P._CP',             # 1B
        'ED6_DT07/CH01490P._CP',             # 1C
        'ED6_DT07/CH01180P._CP',             # 1D
        'ED6_DT07/CH01120P._CP',             # 1E
        'ED6_DT07/CH01130P._CP',             # 1F
        'ED6_DT07/CH00023P._CP',             # 20
        'ED6_DT07/CH00053P._CP',             # 21
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53970,
        Z                   = 0,
        Y                   = 1360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 57050,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 63570,
        Z                   = 0,
        Y                   = -2300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 66490,
        Z                   = 0,
        Y                   = -2200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 62300,
        Z                   = 0,
        Y                   = -3120,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 120580,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 121660,
        Z                   = 0,
        Y                   = -1200,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 120400,
        Z                   = 0,
        Y                   = -990,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 27820,
        Z                   = 0,
        Y                   = 62520,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 84510,
        Z                   = 0,
        Y                   = 56870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 92000,
        Z                   = 300,
        Y                   = 61850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 117070,
        Z                   = 0,
        Y                   = -1300,
        Direction           = 132,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 118280,
        Z                   = 0,
        Y                   = -2510,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 114540,
        Z                   = 0,
        Y                   = -500,
        Direction           = 228,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 113510,
        Z                   = 0,
        Y                   = -1480,
        Direction           = 273,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 57640,
        Z                   = 0,
        Y                   = -910,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 58990,
        Z                   = 0,
        Y                   = -920,
        Direction           = 275,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 117510,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 342,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -870,
        Z                   = 0,
        Y                   = 2340,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 540,
        Z                   = 0,
        Y                   = 2330,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = -2600,
        Z                   = 0,
        Y                   = -1720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 3340,
        Z                   = 0,
        Y                   = -3440,
        Direction           = 289,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 1560,
        Z                   = 0,
        Y                   = -1380,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 1550,
        Z                   = 0,
        Y                   = -180,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 117540,
        Z                   = 0,
        Y                   = 3500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 125600,
        Z                   = 0,
        Y                   = -3380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 36,
    )


    DeclActor(
        TriggerX            = -2600,
        TriggerZ            = 0,
        TriggerY            = 820,
        TriggerRange        = 800,
        ActorX              = -4460,
        ActorZ              = 1500,
        ActorY              = 960,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28140,
        TriggerZ            = 0,
        TriggerY            = 61240,
        TriggerRange        = 800,
        ActorX              = 27820,
        ActorZ              = 1500,
        ActorY              = 62520,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25070,
        TriggerZ            = 0,
        TriggerY            = 56080,
        TriggerRange        = 800,
        ActorX              = 24330,
        ActorZ              = 3000,
        ActorY              = 55900,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24870,
        TriggerZ            = 0,
        TriggerY            = 57940,
        TriggerRange        = 800,
        ActorX              = 23860,
        ActorZ              = 2500,
        ActorY              = 58100,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24860,
        TriggerZ            = 0,
        TriggerY            = 59860,
        TriggerRange        = 800,
        ActorX              = 23870,
        ActorZ              = 2800,
        ActorY              = 59950,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6F2",          # 00, 0
        "Function_1_B26",          # 01, 1
        "Function_2_B99",          # 02, 2
        "Function_3_C91",          # 03, 3
        "Function_4_D27",          # 04, 4
        "Function_5_EA3",          # 05, 5
        "Function_6_10F2",         # 06, 6
        "Function_7_2FAC",         # 07, 7
        "Function_8_42BC",         # 08, 8
        "Function_9_6BF8",         # 09, 9
        "Function_10_6C47",        # 0A, 10
        "Function_11_6C96",        # 0B, 11
        "Function_12_6CE5",        # 0C, 12
        "Function_13_6D34",        # 0D, 13
        "Function_14_6D83",        # 0E, 14
        "Function_15_6DFF",        # 0F, 15
        "Function_16_6E7A",        # 10, 16
        "Function_17_6EE2",        # 11, 17
        "Function_18_6F49",        # 12, 18
        "Function_19_6F9A",        # 13, 19
        "Function_20_6FEB",        # 14, 20
        "Function_21_7007",        # 15, 21
        "Function_22_7023",        # 16, 22
        "Function_23_703F",        # 17, 23
        "Function_24_705B",        # 18, 24
        "Function_25_8C3A",        # 19, 25
        "Function_26_8C82",        # 1A, 26
        "Function_27_8CCA",        # 1B, 27
        "Function_28_8D12",        # 1C, 28
        "Function_29_8D5A",        # 1D, 29
        "Function_30_8DEF",        # 1E, 30
        "Function_31_9FCA",        # 1F, 31
        "Function_32_9FE6",        # 20, 32
        "Function_33_A002",        # 21, 33
        "Function_34_A01E",        # 22, 34
        "Function_35_A03A",        # 23, 35
        "Function_36_A060",        # 24, 36
        "Function_37_A084",        # 25, 37
        "Function_38_A562",        # 26, 38
        "Function_39_A5E9",        # 27, 39
        "Function_40_A66A",        # 28, 40
        "Function_41_A6E3",        # 29, 41
    )


    def Function_0_6F2(): pass

    label("Function_0_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_709")
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_709")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_746")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 60680, 200, -3460, 270)

    label("loc_777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_79A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_7C7")

    Jump("loc_9E1")

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_8D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_802")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_833")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 55450, 200, -2270, 180)

    label("loc_833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_860")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_860")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_883")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8A6")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_8A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D3")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_8D3")

    Jump("loc_9E1")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_935")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_905")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_932")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_932")

    Jump("loc_9E1")

    label("loc_935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96E")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_96E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_991")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9B4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_9B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9E1")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_9E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_A6D")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_A88")

    label("loc_A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A7C")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_A88")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A88")
    SetChrFlags(0x1B, 0x80)

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_A9E")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_B25")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_ABD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 37)
    Jump("loc_B25")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD1")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_B25")

    label("loc_AD1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_ADD"),
        (SWITCH_DEFAULT, "loc_B25"),
    )


    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF5")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_B22")

    label("loc_AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0D")
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_B22")

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B22")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_B22")

    Jump("loc_B25")

    label("loc_B25")

    Return()

    # Function_0_6F2 end

    def Function_1_B26(): pass

    label("Function_1_B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B42")
    OP_B1("t4121_y")
    Jump("loc_B4B")

    label("loc_B42")

    OP_B1("t4121_n")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_B61")
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_B83")

    label("loc_B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_B77")
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jump("loc_B83")

    label("loc_B77")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 2)), scpexpr(EXPR_END)), "loc_B98")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_B98")

    Return()

    # Function_1_B26 end

    def Function_2_B99(): pass

    label("Function_2_B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BB8")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_BCD")

    label("loc_BB8")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_BCD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1C")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_C1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C3F")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C62")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C8F")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_C8F")

    OP_0D()
    Return()

    # Function_2_B99 end

    def Function_3_C91(): pass

    label("Function_3_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CAC")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_CBD")

    label("loc_CAC")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_CBD")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_CF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D25")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_D25")

    OP_0D()
    Return()

    # Function_3_C91 end

    def Function_4_D27(): pass

    label("Function_4_D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D48")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_D5F")

    label("loc_D48")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_D5F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DC1")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)

    label("loc_DC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF7")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 55450, 200, -2270, 180)

    label("loc_DF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E29")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 7)
    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, 57160, 200, -5120, 270)

    label("loc_E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E4C")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60960, 0, 2280, 0)

    label("loc_E4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E6F")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA1")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xE, 0)
    SetChrPos(0xE, 54780, 0, -5080, 90)

    label("loc_EA1")

    OP_0D()
    Return()

    # Function_4_D27 end

    def Function_5_EA3(): pass

    label("Function_5_EA3")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_A3(0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F49")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 32)
    SetChrSubChip(0x9, 0)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, 60680, 200, -3460, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2E")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F49")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FB5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 33)
    SetChrSubChip(0xA, 0)
    OP_44(0xA, 0x0)
    SetChrPos(0xA, 55450, 200, -2270, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9A")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB5")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_100E")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 58950, 0, 2510, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF3")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100E")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_100E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1076")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xE, 0)
    SetChrPos(0xE, 54780, 0, -5080, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105B")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_105B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1076")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x4)

    label("loc_1076")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10F1")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05※要待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　回收后加入队伍的携带品。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_10F1")

    Return()

    # Function_5_EA3 end

    def Function_6_10F2(): pass

    label("Function_6_10F2")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0x10A, -2600, 0, 1150, 270)
    SetChrPos(0x101, -2600, 0, 300, 270)
    SetChrPos(0x9, -500, -130, -7700, 354)
    SetChrPos(0xA, 500, -130, -7700, 354)
    OP_6D(1280, 0, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_1191():
        OP_6D(-4090, 0, 1200, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1191)

    def lambda_11A9():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11A9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_28(0x80, 0x1, 0x1000)

    ChrTalk(    #1
        0x8,
        (
            "#760F#5P是吗……\x01",
            "你们两个辛苦了。\x02\x03",

            "那么配合训练的评价\x01",
            "把报酬付给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1004F#6P咦？训练\x01",
            "还能得到报酬？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#760F#5P嗯，这也是\x01",
            "工作的一环。\x02\x03",

            "当然，也希望你们\x01",
            "能够努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1016F#6P哈哈……我们会的。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x7E, 0x4, 0x10)
    OP_AF(0xCD, 0x7E)
    Sleep(100)
    OP_28(0x7F, 0x4, 0x10)
    OP_28(0x7F, 0x4, 0x20)
    OP_28(0x80, 0x4, 0x10)
    OP_28(0x80, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #5
        0x8,
        (
            "#761F#5P看来你们在\x01",
            "训练期间挺充实的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1006F#6P嗯！\x01",
            "真是受益匪浅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#1310F如果再有机会的话\x01",
            "我还想去训练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#761F#5P呵呵，这真是太好了。\x02\x03",

            "#760F说起来克鲁茨先生他们\x01",
            "还在训练场吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015F#6P嗯，和卡露娜小姐她们\x01",
            "一起接受高级训练。\x02\x03",

            "暂时应该回不来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        (
            "#1316F不过三个正游击士\x01",
            "都去了国外。\x02\x03",

            "接下来有够忙的了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)
    Sleep(400)

    ChrTalk(    #11
        0x10A,
        (
            "#810F#2P卡西乌斯先生也正式\x01",
            "在王国军工作了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #12
        0x101,
        (
            "#1011F#6P啊，嗯。\x02\x03",

            "听说是要去雷斯顿要塞\x01",
            "赴任……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#760F#5P卡西乌斯先生以准将的身份\x01",
            "就任军队作战指挥部长了。\x02\x03",

            "也可以说是现在\x01",
            "王国军的总指挥。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(900)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)
    Sleep(400)

    ChrTalk(    #14
        0x101,
        (
            "#1004F#6P军、军队的总指挥！？\x02\x03",

            "就是说现在\x01",
            "不是摩尔根将军了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#760F#5P当初担任总指挥的本来是摩尔根将军，\x01",
            "但将军自愿将\x01",
            "权力交给了卡西乌斯先生。\x02\x03",

            "#761F将军一定是想把未来托付给\x01",
            "年轻的卡西乌斯先生吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1019F#6P呼……\x01",
            "我怎么对老爸没这种感觉呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#819F哈哈，这也是卡西乌斯先生的\x01",
            "作风使然吧。\x02\x03",

            "#1314F不过这样一来协会的\x01",
            "作战能力更加降低了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#764F#5P嗯，虽然比以前\x01",
            "更便于和军队合作了……\x02\x03",

            "#762F但是现在我们\x01",
            "需要警惕的事更多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#814F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1002F#6P那指的是……\x01",
            "『结社』吧。\x02\x03",

            "难道他们有什么动向？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#764F#5P不，现在还没。\x02\x03",

            "#765F不过最近一个月\x01",
            "发生了一些奇怪的事。\x02\x03",

            "比如……\x01",
            "生活在各地的魔兽变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1026F#6P魔兽的变化……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        "#812F具体是怎样的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#762F#5P首先是以前从未见过的\x01",
            "新型魔兽在各地出现了。\x02\x03",

            "而且已知的魔兽也比之前\x01",
            "难对付多了。\x02\x03",

            "现在原因还不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        (
            "#1317F还、还有这种事啊……\x02\x03",

            "#815F就是说是那个『结社』\x01",
            "捣的鬼！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#764F#5P不，现在作结论\x01",
            "还为时过早。\x02\x03",

            "#762F不过自从女王的诞辰庆典之后\x01",
            "就开始发生一些事情……\x02\x03",

            "这一点是可以确定的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        "#813F怎么会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1003F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#760F#5P其实我们对这件事\x01",
            "已经做好了对策。\x02\x03",

            "希望艾丝蒂尔小姐和\x01",
            "亚妮拉丝小姐也能配合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    SetChrName("女性的声音")

    NpcTalk(    #31
        0x9,
        "女性的声音",
        "#2P什么啊，你们已经到了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_1A59():
        OP_6D(-340, 0, -2920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A59)

    def lambda_1A71():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A71)

    def lambda_1A89():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A89)
    Sleep(100)

    def lambda_1A9C():
        TurnDirection(0x10A, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1A9C)
    Sleep(100)

    def lambda_1AAF():
        TurnDirection(0x8, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AAF)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1AE2():
        OP_8E(0x9, 0xFFFFFE0C, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1AE2)

    def lambda_1AFD():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1AFD)
    Sleep(300)

    def lambda_1B14():
        OP_8E(0xA, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1B14)

    def lambda_1B2F():
        OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1B2F)

    def lambda_1B41():
        TurnDirection(0x101, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B41)

    def lambda_1B4F():
        TurnDirection(0x10A, 0x9, 0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1B4F)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #32
        0x10A,
        "#814F#4P啊，雪拉前辈！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1004F#6P雪拉姐！？\x01",
            "还有阿加特也……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BBE():
        OP_6D(-2940, 0, 920, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BBE)

    def lambda_1BD6():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BD6)

    def lambda_1BEE():
        OP_8F(0x9, 0xFFFFF5EC, 0x0, 0xFFFFFB96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1BEE)
    Sleep(300)

    def lambda_1C0E():
        OP_8F(0xA, 0xFFFFFA06, 0x0, 0xFFFFFACE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1C0E)

    def lambda_1C29():

        label("loc_1C29")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_1C29")

    QueueWorkItem2(0x101, 2, lambda_1C29)
    Sleep(1000)

    def lambda_1C3F():
        OP_8E(0x10A, 0xFFFFF952, 0x0, 0x15E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1C3F)
    WaitChrThread(0x10A, 0x2)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x9, 0x0)
    TurnDirection(0x9, 0x101, 400)
    WaitChrThread(0xA, 0x0)
    TurnDirection(0xA, 0x10A, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)

    ChrTalk(    #34
        0x9,
        "#021F欢迎回来，艾丝蒂尔、亚妮拉丝。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "#051F#6P哟，没想到你们\x01",
            "这么快就回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1001F#5P雪拉姐，我回来了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)
    Sleep(400)

    ChrTalk(    #37
        0x101,
        "#1017F#5P阿加特也好久没见了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#053F#6P嗯，诞辰庆典之后就没见了。\x02\x03",

            "#552F……约修亚的事\x01",
            "我听大叔说了。\x02\x03",

            "#051F你好像消沉了一阵子……\x01",
            "不过看来已经\x01",
            "打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1016F#5P嘿嘿，算是吧。\x02\x03",

            "#1008F不过话说回来……\x01",
            "你们两个怎么在一起？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10A,
        (
            "#1310F#2P唔～我也想问。\x01",
            "真是少见的搭配。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#023F咦，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#053F#6P嗯，我的确\x01",
            "很少和她一起工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#760F其实我们是让雪拉扎德小姐\x01",
            "和阿加特先生去\x01",
            "执行特别的任务。\x02\x03",

            "所以才让他们来了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)

    ChrTalk(    #44
        0x101,
        "#1004F#6P特别的任务？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #45
        0x8,
        (
            "#762F嗯……\x01",
            "『噬身之蛇』的调查。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#1005F#6P『结社』的调查！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        "#1317F#4P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#020F虽说是调查，不过\x01",
            "还没有具体方向。\x02\x03",

            "因为这组织的存在本身\x01",
            "还是一个谜。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #49
        0xA,
        (
            "#053F#6P一边工作一边遍访各地，\x01",
            "关注『结社』的动向……\x02\x03",

            "#051F总之是既无聊又困难的任务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1015F#5P原，原来如此……\x02\x03",

            "#1007F不过现在也\x01",
            "只能这么做。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x10A, 0x8, 400)

    ChrTalk(    #51
        0x101,
        (
            "#1011F#6P那么要我们协助\x01",
            "指的是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#760F嗯，要你们两个帮忙。\x02\x03",

            "为了在王国各地收集信息，\x01",
            "我们让阿加特先生和\x01",
            "雪拉扎德小姐分开行动……\x02\x03",

            "因为单独调查不明身份的\x01",
            "『结社』可能非常危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        (
            "#818F#4P就是说我们的其中一个\x01",
            "帮雪拉前辈……\x02\x03",

            "另一个帮阿加特\x01",
            "前辈是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#760F就是这么回事。\x02\x03",

            "怎么样？\x01",
            "愿意协助参加调查吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1018F#6P我当然没问题！\x02\x03",

            "我本来就想调查『结社』的动向，\x01",
            "正好能搭顺风船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#1310F#4P也请让我一起帮忙。\x02\x03",

            "我绝不能对那些在幕后\x01",
            "活动的可疑分子放任不管！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        "#761F谢谢，这真是太好了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    TurnDirection(0x10A, 0xA, 400)
    Sleep(400)

    ChrTalk(    #58
        0x9,
        (
            "#020F那么问题就是\x01",
            "如何分组了。\x02\x03",

            "我们倒觉得怎么样\x01",
            "都可以接受。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#051F#6P大家也都认识。\x02\x03",

            "根据自己的适应情况\x01",
            "你们俩自己商量着决定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1007F#5P呼……\x01",
            "这还真是个难题呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #61
        0x101,
        "#1015F#5P亚妮拉丝你觉得呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #62
        0x10A,
        (
            "#817F#4P嗯，我想想。\x02\x03",

            "这么说可能有点不负责任……\x02\x03",

            "#810F不过还是让艾丝蒂尔\x01",
            "来决定才最好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1004F#5P哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#810F#4P毕竟艾丝蒂尔才刚\x01",
            "成为了正游击士。\x02\x03",

            "作为游击士应该还没\x01",
            "完全给自己定型。\x02\x03",

            "#811F所以以此为契机，\x01",
            "来考虑一下自己将来的风格\x01",
            "怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1011F#5P亚妮拉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#027F呵呵，亚妮拉丝。\x02\x03",

            "什么时候你也\x01",
            "变得这么伶牙俐齿了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #67
        0x10A,
        "#811F#2P嘿嘿，承蒙夸奖⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#053F#6P不过这话也有道理。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #69
        0xA,
        (
            "#050F#6P比如我和雪拉扎德\x01",
            "游击士的排位差不多，\x01",
            "可是战斗风格相当不同。\x02\x03",

            "我是以魔法为辅，\x01",
            "以重剑的攻击为主……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "#020F我是靠灵活性和长距离鞭攻击，\x01",
            "并且灵活运用魔法的类型。\x02\x03",

            "这些应该能作为\x01",
            "选择的基准。\x02\x03",

            "#021F不过要说到游击士的工作，\x01",
            "也不只是战斗。\x02\x03",

            "你最好自己想想再选。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #71
        0x101,
        (
            "#1007F#5P嗯、嗯。\x02\x03",

            "#1008F那么，就……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_B7(0x9)
    OP_31(0x5, 0x0, 0x2A)
    OP_31(0x5, 0xFE, 0x0)
    OP_41(0x5, 0x9E, 0xFF)
    OP_41(0x5, 0xFF, 0xFF)
    OP_41(0x5, 0x120, 0xFF)
    OP_41(0x5, 0x283, 0x0)
    OP_41(0x5, 0x270, 0x1)
    OP_41(0x5, 0x267, 0x2)
    OP_41(0x5, 0x25E, 0x5)
    OP_35(0x5, 0x8C)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x100)
    OP_31(0x2, 0x0, 0x2A)
    OP_31(0x2, 0xFE, 0x0)
    OP_41(0x2, 0x44, 0xFF)
    OP_41(0x2, 0xFF, 0xFF)
    OP_41(0x2, 0x120, 0xFF)
    OP_41(0x2, 0x280, 0x0)
    OP_41(0x2, 0x2C8, 0x1)
    OP_41(0x2, 0x264, 0x2)
    OP_41(0x2, 0x26D, 0x4)
    OP_35(0x2, 0x8C)
    OP_35(0x2, 0x0)
    OP_BB(0x2, 0x6, 0xF0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x18\x07\x05选哪个？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【雪拉扎德】\x01",      # 0
            "【阿加特】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2773"),
        (1, "loc_2779"),
        (SWITCH_DEFAULT, "loc_277F"),
    )


    label("loc_2773")

    OP_A2(0x1200)
    Jump("loc_277F")

    label("loc_2779")

    OP_A2(0x1201)
    Jump("loc_277F")

    label("loc_277F")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2B9B")

    ChrTalk(    #73
        0x9,
        (
            "#020F这样啊，那就合作愉快。\x02\x03",

            "#021F呵呵，期待你作为\x01",
            "正游击士的表现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1007F#5P呼……我会努力的。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #75
        0x10A,
        (
            "#1310F#2P那么我就和\x01",
            "阿加特前辈一起。\x02\x03",

            "#811F合作愉快。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "#051F#6P嗯，彼此彼此。\x02\x03",

            "#053F好，那么这个问题\x01",
            "总算是解决了……\x02\x03",

            "不过还有一个问题是，\x01",
            "访问各地的顺序怎么排？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #77
        0x9,
        (
            "#020F艾南先生。\x01",
            "我想听听你的意见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    def lambda_28E4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_28E4)

    def lambda_28F2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28F2)

    def lambda_2900():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2900)
    Sleep(400)

    ChrTalk(    #78
        0x8,
        (
            "#764F嗯……\x02\x03",

            "#760F现在先去支援\x01",
            "忙碌的地方支部比较好吧。\x02\x03",

            "其实，从柏斯支部和卢安支部\x01",
            "都发来了支援请求……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#026F嗯，库拉茨和卡露娜\x01",
            "都不在，也难怪。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10A, 400)

    ChrTalk(    #80
        0xA,
        (
            "#050F#6P亚妮拉丝。\x01",
            "你比较熟悉柏斯吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0xA, 400)

    ChrTalk(    #81
        0x10A,
        (
            "#816F#2P那当然。\x01",
            "我可是土生土长的柏斯孩子。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A19():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A19)

    def lambda_2A27():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A27)

    ChrTalk(    #82
        0xA,
        (
            "#050F#6P那我们去\x01",
            "柏斯支部吧。\x02\x03",

            "我也有点事要去那边办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1011F#5P啊，阿加特的故乡应该是\x01",
            "在拉文努村吧。\x02\x03",

            "难道是荣归故里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        "#053F#6P嗯，也差不多吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #85
        0x9,
        (
            "#021F那我们就\x01",
            "去卢安支部吧。\x02\x03",

            "#020F艾丝蒂尔没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #86
        0x101,
        (
            "#1006F#5P嗯，当然。\x02\x03",

            "#1012F卢安地区啊……\x01",
            "不知道大家过的怎么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#760F我来负责联络\x01",
            "各支部。\x02\x03",

            "那么各位。\x01",
            "路上请小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F97")

    label("loc_2B9B")


    ChrTalk(    #88
        0xA,
        (
            "#053F#6P是吗？明白了。\x02\x03",

            "#050F既然成了正游击士，\x01",
            "你就得更加努力了。\x02\x03",

            "要有心理准备啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #89
        0x101,
        (
            "#1006F#5P是是，我知道了啦。\x02\x03",

            "#1016F真是的，就知道\x01",
            "你会说让人讨厌的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        "#055F#6P唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "#027F好了好了，禁止斗嘴。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 400)

    ChrTalk(    #92
        0x9,
        (
            "#021F那么我就和\x01",
            "亚妮拉丝配合吧。\x02\x03",

            "#020F我要看看你的训练成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10A,
        (
            "#816F#2P嗯！\x02\x03",

            "#811F呵呵，好久没和前辈配合了，\x01",
            "真开心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "#053F#6P好，那么这个问题\x01",
            "总算是解决了……\x02\x03",

            "#050F不过还有一个问题是，\x01",
            "访问各地的顺序怎么排？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #95
        0x9,
        (
            "#020F艾南先生。\x01",
            "我想听听你的意见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    def lambda_2DA0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2DA0)

    def lambda_2DAE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DAE)

    def lambda_2DBC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2DBC)
    Sleep(400)

    ChrTalk(    #96
        0x8,
        (
            "#764F嗯……\x02\x03",

            "#760F现在先去支援\x01",
            "忙碌的地方支部比较好吧。\x02\x03",

            "其实，从洛连特支部和卢安支部\x01",
            "都来了支援请求……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "#025F哎呀，洛连特看来\x01",
            "太缺人手了。\x02\x03",

            "#020F就算是为了帮爱娜，\x01",
            "也是我去比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10A,
        (
            "#810F#2P是啊，我也赞成。\x02\x03",

            "#811F唔～好久没见到\x01",
            "爱娜小姐了～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #99
        0xA,
        (
            "#051F#6P那我们就去\x01",
            "卢安支部吧。\x02\x03",

            "艾丝蒂尔，没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #100
        0x101,
        (
            "#1006F#5P嗯，当然。\x02\x03",

            "#1012F卢安地区啊……\x01",
            "不知道大家过的怎么样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#760F我来负责联络\x01",
            "各支部。\x02\x03",

            "那么各位。\x01",
            "你们请小心上路。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F97")

    FadeToDark(1500, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_10F2 end

    def Function_7_2FAC(): pass

    label("Function_7_2FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FBD")
    Call(0, 38)

    label("loc_2FBD")

    EventBegin(0x0)
    SetChrPos(0x101, -2600, 0, 1230, 270)
    SetChrPos(0xF7, -2600, 0, 190, 270)
    SetChrPos(0xD, -2020, 0, -990, 270)
    SetChrPos(0xC, -1560, 0, -30, 270)
    SetChrPos(0xB, -1600, 0, 1080, 270)
    SetChrPos(0xE, -1910, 0, 2020, 270)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6D(-7190, 0, 1580, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_3090():
        OP_6D(-3380, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3090)

    def lambda_30A8():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30A8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #102
        0x8,
        (
            "#761F#5P各位来的正好。\x02\x03",

            "#760F我已经读过你们\x01",
            "在卢安和蔡斯做的报告了。\x02\x03",

            "真是有劳你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1007F#4P唔～以『结社』的势力来看，\x01",
            "只能算是小试牛刀……\x02\x03",

            "面具男和墨镜男\x01",
            "也都没有拿出真正实力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#760F#5P不过即便如此，我们也\x01",
            "已经可以确定『结社』有动作了，\x01",
            "应该说是个不小的收获吧。\x02\x03",

            "我想，今后跟王国军的合作\x01",
            "也会进行得比较顺利吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3266")

    ChrTalk(    #105
        0x106,
        (
            "#050F#6P那么，那个军队的委托\x01",
            "究竟是什么？\x02\x03",

            "果然是和『结社』有关？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32AD")

    label("loc_3266")


    ChrTalk(    #106
        0x103,
        (
            "#020F#6P那么，那个军队的委托\x01",
            "究竟是什么？\x02\x03",

            "果然是和『结社』有关？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AD")


    ChrTalk(    #107
        0x8,
        (
            "#764F#5P好像是的……\x02\x03",

            "#762F不过电话里\x01",
            "似乎说不清。\x02\x03",

            "所以军队会直接派人\x01",
            "过来说明情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#035F唔……\x01",
            "电话里说不清的内容啊。\x02\x03",

            "#030F说不定是想要\x01",
            "防止窃听。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1020F#5P窃、窃听！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#762F#5P这很有可能。\x02\x03",

            "导力通讯虽然方便，\x01",
            "不过也有被偷听的危险。\x02\x03",

            "#764F协会之间的通讯\x01",
            "倒是设有防止窃听用的\x01",
            "周波变更功能……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1015F#4P这防窃听功能\x01",
            "不能在和军队通讯时使用？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#765F#5P军队有军队的通讯格式，\x01",
            "所以没办法。\x02\x03",

            "只能互相使用一般通讯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1007F#4P这样啊……\x02\x03",

            "#1019F唔～索性用\x01",
            "同样的规格不就行了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#070F#2P呵呵，虽说是在合作，不过毕竟是\x01",
            "一国的军队和国际民间组织之间的关系。\x02\x03",

            "不能避免地要有情报安全措施。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_358A")

    ChrTalk(    #115
        0x106,
        (
            "#053F#6P可是艾南。\x02\x03",

            "#051F你好像对军队的委托是什么\x01",
            "已经心中有数了。\x02\x03",

            "不然你也不会特意\x01",
            "把我们叫来蔡斯。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F5")

    label("loc_358A")


    ChrTalk(    #116
        0x103,
        (
            "#026F#6P可是艾南先生，\x02\x03",

            "#020F你好像对军队的委托是什么\x01",
            "已经心中有数了。\x02\x03",

            "还特别把我们从蔡斯\x01",
            "叫来这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F5")


    ChrTalk(    #117
        0x8,
        (
            "#761F#5P哎呀，被你们看穿了。\x02\x03",

            "#760F虽然这只是我的推测……\x01",
            "不过很可能和\x01",
            "『互不侵犯条约』有关呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1004F#4P互不侵犯条约……\x02\x03",

            "#1015F最近倒是经常\x01",
            "听说这个……\x02\x03",

            "这条约具体内容是什么？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #119
        0xC,
        (
            "#040F#6P是女王陛下提倡，\x01",
            "由利贝尔、埃雷波尼亚、卡尔瓦德\x01",
            "三国之间签订的条约。\x02\x03",

            "核心思想是不用武力，而是\x01",
            "通过协商解决国家间的纠纷。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 400)

    def lambda_3769():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3769)
    Sleep(50)

    def lambda_377C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_377C)
    Sleep(50)

    def lambda_378F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_378F)
    Sleep(50)

    def lambda_37A2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_37A2)
    Sleep(300)

    ChrTalk(    #120
        0x101,
        (
            "#1004F#5P啊……！\x02\x03",

            "这样一来不是就\x01",
            "不再有战争了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "#047F#6P不，因为没有强制约束力，\x01",
            "所以这看来很难……\x02\x03",

            "#040F不过还是有一定的影响力的，\x01",
            "祖母大人是希望这能推动\x01",
            "各国国民之间的友好氛围。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1011F#5P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xE,
        (
            "#071F#2P不愧是艾莉茜雅陛下,\x01",
            "着眼之处很厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#061F#6P如果能成为促使三国友好\x01",
            "相处的契机就太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#760F#5P这互不侵犯条约将于下周末\x01",
            "在『艾尔贝离宫』签订。\x02\x03",

            "外国的要人也会云集，\x01",
            "媒体也将给予关注。\x02\x03",

            "#764F在这种情况下，如果『结社』\x01",
            "有什么企图的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    def lambda_3998():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3998)
    Sleep(50)

    def lambda_39AB():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_39AB)
    Sleep(50)

    def lambda_39BE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_39BE)
    Sleep(50)

    def lambda_39D1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_39D1)
    Sleep(50)

    def lambda_39E4():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_39E4)
    Sleep(300)

    ChrTalk(    #126
        0x101,
        (
            "#1002F#4P不错……\x01",
            "这可不是闹着玩的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A82")

    ChrTalk(    #127
        0x106,
        (
            "#053F#6P呼……\x01",
            "这看来是个严峻的问题。\x02\x03",

            "#051F那在那个负责人来之前，\x01",
            "我们在这里等就行了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ADD")

    label("loc_3A82")


    ChrTalk(    #128
        0x103,
        (
            "#026F#6P唔……\x01",
            "这看来是个严峻的问题啊。\x02\x03",

            "#020F那在负责人来之前，\x01",
            "我们在这里等就行了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ADD")


    ChrTalk(    #129
        0x8,
        (
            "#760F#5P我想想。\x02\x03",

            "离约定的时间的还早，\x01",
            "你们也可以自由行动……\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #130
        0x8,
        "#763F#5P哎呀，失敬。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    def lambda_3BB6():
        OP_6D(-4530, 0, 870, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BB6)
    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 270, 400)
    Sleep(400)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #131
        0x8,
        (
            "#760F#5P这儿是游击士协会。\x01",
            "格兰赛尔支部。\x02\x03",

            "嗯……嗯……\x02\x03",

            "#763F……………………………\x02\x03",

            "#765F原来如此……是这样啊。\x02\x03",

            "嗯，这确实\x01",
            "不好办了呢。\x02\x03",

            "#764F请稍等……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #132
        0x101,
        "#1015F莫非是王国军打来的？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #133
        0x8,
        (
            "#760F#5P不，是艾尔贝离宫。\x02\x03",

            "他们说保护了一个\x01",
            "迷路的孩子……\x02\x03",

            "可是却找不到监护人，\x01",
            "感到很为难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1004F啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "#043F#6P这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#760F#5P他们委托我们去\x01",
            "寻找监护人……\x02\x03",

            "离军队的负责人来还有些时间，\x01",
            "可以配合我们做一个调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E6B")

    ChrTalk(    #137
        0x101,
        (
            "#1006F那是自然，\x01",
            "我们接下来了。\x02\x03",

            "阿加特也没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x106,
        (
            "#051F#6P真没办法。\x01",
            "赶快去离宫吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC9")

    label("loc_3E6B")


    ChrTalk(    #139
        0x101,
        (
            "#1006F那是自然，\x01",
            "我们接下来了。\x02\x03",

            "雪拉姐也没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x103,
        (
            "#021F#6P当然了。\x01",
            "赶快去离宫吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC9")


    ChrTalk(    #141
        0x8,
        "#760F#5P那太好了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #142
        0x8,
        (
            "#761F#5P嗯，我们正好有\x01",
            "有空的游击士在，\x01",
            "我让他们去你们那里。\x02\x03",

            "#760F请问您的大名是……\x01",
            "嗯……明白了。\x02\x03",

            "那么请耐心等候。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(800)
    OP_8C(0x8, 90, 400)

    def lambda_3F88():
        OP_6D(-3380, 0, 980, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F88)

    def lambda_3FA0():
        OP_8E(0xFE, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3FA0)
    Sleep(500)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #143
        0x8,
        (
            "#760F#5P对方是在艾尔贝离宫工作的\x01",
            "管家雷蒙德先生，\x01",
            "他在照顾那个迷路的孩子。\x02\x03",

            "你们到了离宫请去找他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1006F#4P嗯，明白了。\x02\x03",

            "#1015F……雷蒙德先生，\x01",
            "好像在哪儿听说过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xE,
        (
            "#073F#2P嗯～不就是那个年轻的管家吗？\x02\x03",

            "在解救离宫的时候\x01",
            "躲在柜台下面的那位。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #146
        0x101,
        (
            "#1006F#6P哦，就是那个自称是\x01",
            "奈尔朋友的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "#761F#5P你们认识的话就\x01",
            "更好办了。\x02\x03",

            "#760F那就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #148
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4203")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_4218")

    label("loc_4203")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_4218")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x0, -140, 0, 90, 180)
    SetChrPos(0x1, -140, 0, 90, 180)
    SetChrPos(0x2, -140, 0, 90, 180)
    SetChrPos(0x3, -140, 0, 90, 180)
    OP_6D(-140, 0, 90, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_A2(0x160B)
    OP_4B(0x8, 255)
    OP_28(0x89, 0x4, 0x2)
    OP_28(0x89, 0x4, 0x8)
    OP_28(0x89, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_7_2FAC end

    def Function_8_42BC(): pass

    label("Function_8_42BC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D7")
    Call(0, 38)
    Call(0, 39)
    AddParty(0x2E, 0xFF, 0xFF)

    label("loc_42D7")

    SetChrPos(0xF, -2310, 0, 2150, 180)
    ClearChrFlags(0xF, 0x80)
    OP_4A(0x8, 255)
    Call(0, 29)
    SetChrPos(0xFA, -2600, 0, 500, 360)
    SetChrPos(0xFB, -1500, 0, 480, 360)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x12F, 0x80)
    OP_6D(-110, -250, -5770, 0)
    OP_67(0, 7440, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xC)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x12F, 0x1, 0x0, 0xA)
    Sleep(800)

    ChrTalk(    #149
        0x101,
        (
            "#1006F#6P我们回来了，艾南先生……\x02\x03",

            "#1004F……啊！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43EF():
        OP_6D(-2890, 0, 1460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43EF)

    def lambda_4407():
        OP_67(0, 7350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4407)

    def lambda_441F():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_441F)

    def lambda_442F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_442F)
    Sleep(100)

    def lambda_4442():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4442)
    Sleep(200)

    def lambda_4455():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_4455)
    Sleep(100)

    def lambda_4468():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_4468)
    WaitChrThread(0xFB, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_44B4")

    ChrTalk(    #150
        0x107,
        "#560F#5P啊，艾丝蒂尔姐姐！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4511")

    label("loc_44B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_44E6")

    ChrTalk(    #151
        0x108,
        "#070F#5P艾丝蒂尔你回来了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4511")

    label("loc_44E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4511")

    ChrTalk(    #152
        0x104,
        "#030F#5P呼，你回来了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_4511")

    Sleep(300)

    def lambda_451C():
        OP_8E(0xFE, 0xFFFFF5D8, 0x0, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_451C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xFA)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4554")
    OP_43(0xFB, 0x0, 0x0, 0x14)
    Sleep(400)
    OP_43(0xFA, 0x0, 0x0, 0x15)
    Jump("loc_4567")

    label("loc_4554")

    OP_43(0xFB, 0x0, 0x0, 0x16)
    Sleep(400)
    OP_43(0xFA, 0x0, 0x0, 0x17)

    label("loc_4567")


    def lambda_456D():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0x1E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_456D)
    Sleep(200)

    def lambda_458D():
        OP_8E(0xFE, 0xFFFFF678, 0x0, 0xFFFFFD58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_458D)
    Sleep(300)

    def lambda_45AD():
        OP_8E(0xFE, 0xFFFFFB14, 0x0, 0xFFFFFDC6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_45AD)
    Sleep(300)

    def lambda_45CD():
        OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFF984, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_45CD)
    WaitChrThread(0x101, 0x0)
    OP_8C(0xF, 180, 400)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0xF8, 0x0)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #153
        0xF,
        (
            "#701F哟，艾丝蒂尔。\x01",
            "好几天没见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1018F#6P咦……\x01",
            "这不是希德中校吗！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x12F, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46AD")

    ChrTalk(    #155
        0x106,
        (
            "#051F哦，原来军队说的负责人\x01",
            "就是你啊。\x02\x03",

            "是从雷斯顿要塞来的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F7")

    label("loc_46AD")


    ChrTalk(    #156
        0x103,
        (
            "#027F原来如此，原来军队说的负责人\x01",
            "就是你啊。\x02\x03",

            "你是从雷斯顿要塞来的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46F7")


    ChrTalk(    #157
        0xF,
        (
            "#701F嗯，没错。\x02\x03",

            "我是刚坐警备艇\x01",
            "过来王都的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1011F#6P这样啊……\x02\x03",

            "正好我们也\x01",
            "工作完回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)

    ChrTalk(    #159
        0x8,
        (
            "#763F#5P哟……？\x02\x03",

            "那个小姑娘\x01",
            "难道就是那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #160
        0x101,
        (
            "#1015F#6P啊，嗯，是的。\x02\x03",

            "因为一些原因\x01",
            "就把她带回来了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #161
        0x101,
        (
            "#1011F#5P那个，小玲。\x02\x03",

            "姐姐们有些事要谈，\x01",
            "你能不能上２楼等着？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_482B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_482B)

    def lambda_4839():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4839)
    Sleep(200)

    def lambda_484C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_484C)

    def lambda_485A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_485A)
    Sleep(200)

    def lambda_486D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_486D)

    def lambda_487B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_487B)
    Sleep(500)

    ChrTalk(    #162
        0x12F,
        (
            "#264F#6P哎呀……\x01",
            "难道是工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1025F#5P嗯、嗯……对不起啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x12F,
        (
            "#266F#6P没关系的……\x02\x03",

            "工作、工作，\x01",
            "就像我爸爸那样。\x02\x03",

            "玲不太喜欢\x01",
            "这种感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1013F#5P唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4996")

    ChrTalk(    #166
        0x107,
        (
            "#560F#5P我、我说，小玲。\x02\x03",

            "和我一起\x01",
            "聊聊天吧？\x02\x03",

            "#061F我很想\x01",
            "了解小玲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49EC")

    label("loc_4996")


    ChrTalk(    #167
        0x107,
        (
            "#560F#2P我、我说……\x01",
            "你是叫小玲吧？\x02\x03",

            "和我一起\x01",
            "聊聊天吧？\x02\x03",

            "#061F我很想\x01",
            "了解小玲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49EC")

    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #168
        0x12F,
        (
            "#264F#6P和你？\x02\x03",

            "#263F嗯，也好。\x01",
            "就和你聊聊吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A84")

    ChrTalk(    #169
        0x107,
        "#067F#5P嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #170
        0x107,
        (
            "#560F#6P那么姐姐，\x01",
            "我们就在２楼等着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ABB")

    label("loc_4A84")


    ChrTalk(    #171
        0x107,
        (
            "#067F#2P嘿嘿。\x02\x03",

            "#560F那么姐姐，\x01",
            "我们就在2楼等着。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ABB")

    Sleep(100)

    def lambda_4AC6():

        label("loc_4AC6")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4AC6")

    QueueWorkItem2(0x101, 2, lambda_4AC6)

    def lambda_4AD7():

        label("loc_4AD7")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4AD7")

    QueueWorkItem2(0xF7, 2, lambda_4AD7)

    def lambda_4AE8():

        label("loc_4AE8")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4AE8")

    QueueWorkItem2(0xF, 2, lambda_4AE8)

    def lambda_4AF9():

        label("loc_4AF9")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4AF9")

    QueueWorkItem2(0x8, 2, lambda_4AF9)

    def lambda_4B0A():

        label("loc_4B0A")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4B0A")

    QueueWorkItem2(0x104, 2, lambda_4B0A)

    def lambda_4B1B():

        label("loc_4B1B")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4B1B")

    QueueWorkItem2(0x105, 2, lambda_4B1B)

    def lambda_4B2C():

        label("loc_4B2C")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4B2C")

    QueueWorkItem2(0x108, 2, lambda_4B2C)

    def lambda_4B3D():
        OP_6D(-680, 2000, 1510, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4B3D)

    def lambda_4B55():
        OP_67(0, 7350, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_4B55)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B85")
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x12F, 0x1, 0x0, 0x11)
    Jump("loc_4BBE")

    label("loc_4B85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA3")
    OP_43(0x107, 0x1, 0x0, 0xE)
    OP_43(0x12F, 0x1, 0x0, 0xF)
    Jump("loc_4BBE")

    label("loc_4BA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4BBE")
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x12F, 0x1, 0x0, 0x11)

    label("loc_4BBE")

    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF, 0x2)
    OP_44(0x8, 0x2)
    OP_44(0x104, 0x2)
    OP_44(0x105, 0x2)
    OP_44(0x108, 0x2)

    def lambda_4BEF():
        OP_6D(-2800, 0, 1820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4BEF)

    def lambda_4C07():
        OP_67(0, 7350, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_4C07)

    def lambda_4C1F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C1F)

    def lambda_4C2D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4C2D)
    Sleep(50)

    def lambda_4C40():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4C40)

    def lambda_4C4E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4C4E)
    Sleep(50)

    def lambda_4C61():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4C61)

    def lambda_4C6F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_4C6F)
    Sleep(50)

    def lambda_4C82():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_4C82)

    def lambda_4C90():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C90)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF, 0x3)
    Sleep(200)

    ChrTalk(    #172
        0x101,
        (
            "#1016F#6P呼……\x01",
            "帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#760F嗯，具体情况\x01",
            "等会儿再问吧。\x02\x03",

            "先听听希德中校\x01",
            "是怎么说的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1006F#6P啊，嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D5C")

    ChrTalk(    #175
        0x106,
        (
            "#051F那就快让我们\x01",
            "听一听吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D7D")

    label("loc_4D5C")


    ChrTalk(    #176
        0x103,
        "#020F那就快让我们听一听吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4D7D")


    ChrTalk(    #177
        0xF,
        (
            "#703F不好意思。\x01",
            "我们这边也很急。\x02\x03",

            "#700F首先你们可以把这\x01",
            "认为是王国军的正式请求。\x02\x03",

            "需要你们调查一件事情\x01",
            "以及搜集信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1004F#6P调查一件事情……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xF,
        (
            "#700F你们知道『互不侵犯条约』吧？\x02\x03",

            "其实，很多地方都收到了\x01",
            "欲图妨碍条约\x01",
            "签订的恐吓信。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #180
        0x101,
        "#1020F#6P恐、恐吓信！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#043F#6P这……\x01",
            "还真不能掉以轻心呢。\x02\x03",

            "到底是什么样的内容？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xF,
        "#703F……你们请看这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #183
        (
            "\x07\x05参加『互不侵犯条约』缔结的人们啊，\x01",
            "你们要立即停止这\x01",
            "充满欺骗和妥协的协议。\x01",
            "万一还有不予停止的人，\x01",
            "就会有大灾降临在他头上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1000)

    ChrTalk(    #184
        0x101,
        "#1019F#6P哇……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50AA")

    ChrTalk(    #185
        0x106,
        (
            "#053F#6P原来如此，确实是恐吓信。\x02\x03",

            "#552F就这点内容？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50E3")

    label("loc_50AA")


    ChrTalk(    #186
        0x103,
        (
            "#026F#6P原来如此，确实是恐吓信。\x02\x03",

            "#022F就这点内容？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E3")


    ChrTalk(    #187
        0xF,
        (
            "#700F嗯，就这点。\x02\x03",

            "而且似乎还刻意隐去了\x01",
            "寄信人的名字。\x02\x03",

            "老实说，虽然让人感觉恶作剧的\x01",
            "可能性最大……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x104,
        (
            "#035F#6P却也有着不像是单纯的\x01",
            "恶作剧的特征──\x02\x03",

            "#030F是不是这样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xF,
        (
            "#702F嗯……\x01",
            "就是收到恐吓信的单位。\x02\x03",

            "#703F首先是雷斯顿要塞司令部。\x02\x03",

            "然后是飞船公社、格兰赛尔大圣堂、\x01",
            "罗恩鲍姆酒店和利贝尔通讯社。\x02\x03",

            "#700F还有帝国大使馆、共和国大使馆、\x01",
            "格兰赛尔城堡和艾尔贝离宫。\x02\x03",

            "总共9处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1020F#6P这、这么多！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x108,
        (
            "#072F#6P原来如此……\x01",
            "如果只是恶作剧，规模也太大了点。\x02\x03",

            "也难怪军队会有所在意。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5350")

    ChrTalk(    #192
        0x106,
        (
            "#050F#6P不过飞船公社和七耀教会，\x01",
            "还有酒店和利贝尔通讯啊……\x02\x03",

            "表面上看都是和条约缔结\x01",
            "没什么关系的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53BC")

    label("loc_5350")


    ChrTalk(    #193
        0x103,
        (
            "#022F#6P不过飞船公社和七耀教会，\x01",
            "还有酒店和利贝尔通讯啊……\x02\x03",

            "表面上看都是和条约缔结\x01",
            "没什么关系的地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53BC")


    ChrTalk(    #194
        0xF,
        (
            "#700F不过从严格意义上来说，\x01",
            "也并非完全没有关系。\x02\x03",

            "#703F首先飞船公社\x01",
            "是接送帝国、共和国有关人员的\x01",
            "航班提供者。\x02\x03",

            "同样，酒店房间也已经有\x01",
            "有关人员在预定了。\x02\x03",

            "#700F另外大圣堂的卡兰大主教\x01",
            "也受女王陛下委托\x01",
            "负责监督和观察条约缔结……\x02\x03",

            "利贝尔通讯关于互不侵犯条约的特辑\x01",
            "报导在几期之前就开始连载了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1015F#6P唔～哪边都和条约\x01",
            "有着某种联系。\x02\x03",

            "到底是什么人的把戏呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x104,
        (
            "#032F#6P呼……\x01",
            "这个不能用普通的思维模式来分析。\x02\x03",

            "既然是国际条约，\x01",
            "那么打算妨碍它的嫌疑人\x01",
            "人选就有多种可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x108,
        (
            "#074F#6P没错。\x01",
            "共和国或者帝国的主战派……\x02\x03",

            "或不欢迎三国合作的\x01",
            "别国所为……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x105,
        (
            "#042F#6P……当然在王国内\x01",
            "也是有嫌疑人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1007F#6P另外……\x01",
            "最坏的可能性还有『结社』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5686")

    ChrTalk(    #200
        0x106,
        (
            "#050F#6P那么军方希望我们\x01",
            "调查什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B1")

    label("loc_5686")


    ChrTalk(    #201
        0x103,
        (
            "#022F#6P那么军方希望我们\x01",
            "调查什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B1")


    ChrTalk(    #202
        0xF,
        (
            "#701F希望你们调查的\x01",
            "不是别的事情……\x02\x03",

            "就是对收到恐吓信的\x01",
            "各单位进行调查询问。\x02\x03",

            "具体是──除去艾尔贝离宫\x01",
            "和雷斯顿要塞的７个地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x8,
        (
            "#764F飞船公社、格兰赛尔大圣堂、\x01",
            "罗恩鲍姆酒店和利贝尔通讯社。\x02\x03",

            "#762F帝国大使馆、共和国大使馆、\x01",
            "还有格兰赛尔城堡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x104,
        (
            "#030F#6P呼，都不是穿着制服的军人\x01",
            "方便随便出入的地方。\x02\x03",

            "在已经失去了情报部的现在，\x01",
            "也难怪会委托给协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xF,
        (
            "#701F惭愧，你说得一点都没错。\x02\x03",

            "并且新的司令官殿下的方针是\x01",
            "能交给协会的工作都要\x01",
            "一股脑地交给协会。\x02\x03",

            "我正在对此进行实践。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1019F#6P真是的……\x01",
            "老爸还真得意忘形了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5904")

    ChrTalk(    #207
        0x106,
        (
            "#551F#6P切，一听就是大叔\x01",
            "会说出来的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5939")

    label("loc_5904")


    ChrTalk(    #208
        0x103,
        (
            "#021F#6P好了好了。\x01",
            "这也是老师他信赖我们的证据。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5939")


    ChrTalk(    #209
        0xF,
        (
            "#701F呵呵，说到底委托你们\x01",
            "还是我个人的意见。\x02\x03",

            "前不久我被任命负责王都\x01",
            "周围的所有警戒工作。\x02\x03",

            "为了准备警戒体制，\x01",
            "就需要尽量多的信息。\x02\x03",

            "能不能请你们帮这个忙？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1015F#6P嗯、嗯……\x01",
            "我们虽然很愿意接下来，\x02\x03",

            "不过还有一件必须\x01",
            "解决的案子已经发生了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x8,
        (
            "#760F就是刚才那个小姑娘的事吧。\x02\x03",

            "能不能简单扼要地\x01",
            "说明一下情况？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05把在艾尔贝离宫玲的父母\x01",
            "丢下玲离开的事说了一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #213
        0xF,
        (
            "#702F原来如此……\x01",
            "这确实不能放下不管。\x02\x03",

            "可是，竟然会丢下那么小的\x01",
            "孩子不管……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1002F#6P之前和她的双亲\x01",
            "有聊过……\x02\x03",

            "看起来是很认真又\x01",
            "很为女儿着想的父母。\x02\x03",

            "可能是有什么\x01",
            "难言之隐吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        (
            "#764F嗯，是啊。\x02\x03",

            "可能是不希望\x01",
            "把女儿卷进\x01",
            "什么事件里吧。\x02\x03",

            "#760F可是，这样的话\x01",
            "说不定能一箭双雕？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1004F#6P哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "#760F玲小姐的双亲\x01",
            "是外国人呢？\x02\x03",

            "那去问问大使馆和\x01",
            "酒店岂不很好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1006F#6P啊，对！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CC6")

    ChrTalk(    #219
        0x106,
        (
            "#051F#6P这些地方\x01",
            "都收到恐吓信了。\x02\x03",

            "还有，飞船公社也\x01",
            "应该有乘船记录。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D0A")

    label("loc_5CC6")


    ChrTalk(    #220
        0x103,
        (
            "#027F#6P这些地方\x01",
            "都收到恐吓信了。\x02\x03",

            "飞船公社也\x01",
            "应该有乘船记录。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D0A")


    ChrTalk(    #221
        0xF,
        (
            "#701F王国军也会向各地命令\x01",
            "协助找寻她的父母。\x02\x03",

            "如果通过了哨所就应该会有消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1008F#6P谢谢你，希德中校！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "#761F看来接下来的问题就\x01",
            "好商量了。\x02\x03",

            "#760F具体的调查方法和任务分配\x01",
            "就交给我们……\x02\x03",

            "调查结果的报告\x01",
            "用文件和口头形式可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xF,
        (
            "#701F嗯，为了避免窃听\x01",
            "还是请别使用导力器了。\x02\x03",

            "其实从今天开始，艾尔贝离宫\x01",
            "将设置警戒本部。\x02\x03",

            "能不能有劳你们\x01",
            "去那边做报告？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1006F#6P嗯，明白了。\x02\x03",

            "那么我们就把调查结果\x01",
            "直接送去艾尔贝离宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xF,
        "#701F拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD5")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05送走希德中校之后\x01",
            "艾丝蒂尔她们讨论了调查方法和任务分配。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #228
        (
            "\x07\x05结果是由艾丝蒂尔、金、奥利维尔、科洛丝\x01",
            "去两国的大使馆和格兰赛尔城堡、利贝尔通讯社……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #229
        (
            "\x07\x05阿加特一个人去调查\x01",
            "去调查其他的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_60BA")

    label("loc_5FD5")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    SetChrName("")

    AnonymousTalk(    #230
        (
            "\x07\x05送走希德中校之后\x01",
            "艾丝蒂尔她们讨论了调查方法和任务分配。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #231
        (
            "\x07\x05结果是由艾丝蒂尔、金、奥利维尔、科洛丝\x01",
            "去两国的大使馆和格兰赛尔城堡、利贝尔通讯社……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #232
        (
            "\x07\x05雪拉扎德一个人去调查\x01",
            "去调查其他的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_60BA")

    ClearChrFlags(0x12F, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, -570, 0, 970, 90)
    SetChrPos(0xF7, -940, 0, -70, 90)
    SetChrPos(0x104, -2280, 0, 810, 90)
    SetChrPos(0x108, -2280, 0, 1980, 90)
    SetChrPos(0x105, -1080, 0, 2040, 90)
    SetChrPos(0x107, 1570, 0, 170, 270)
    SetChrPos(0x12F, 1710, 0, 1240, 270)
    OP_9F(0x12F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6D(-160, 0, 1660, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #233
        0x101,
        (
            "#1006F#5P那我们就\x01",
            "先出去一下。\x02\x03",

            "提妲、玲。\x01",
            "抱歉，你们就呆在家里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x12F,
        (
            "#265F#4P关于这个……\x02\x03",

            "#261F玲准备和提妲\x01",
            "一起去购物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x101,
        "#1004F#5P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x107,
        (
            "#560F对、对不起，姐姐。\x02\x03",

            "小玲非常想去\x01",
            "百货商店……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x12F,
        (
            "#264F#2P哎呀，真出人意料。\x02\x03",

            "#263F提妲你不是也说\x01",
            "想看看布偶吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x107,
        (
            "#067F啊……\x01",
            "小玲你真是的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1025F#5P唔、唔……\x02\x03",

            "不知道什么时候会得到\x01",
            "小玲爸爸妈妈的消息，\x01",
            "我本来是希望你等在这里的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x12F,
        "#267F#4P（盯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x107,
        "#063F（盯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#1019F#5P唔……\x01",
            "两个人联合起来这么看着我真狡猾。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63E2")

    ChrTalk(    #243
        0x106,
        (
            "#051F#5P没什么关系吧？\x02\x03",

            "有提妲跟着，\x01",
            "买买东西应该没问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6421")

    label("loc_63E2")


    ChrTalk(    #244
        0x103,
        (
            "#021F#5P没什么关系吧？\x02\x03",

            "有提妲跟着，\x01",
            "买买东西应该没问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6421")


    ChrTalk(    #245
        0x101,
        (
            "#1007F#5P嗯……也对。\x02\x03",

            "#1006F提妲、小玲。\x02\x03",

            "我们傍晚会回来的，\x01",
            "你们可要在此之前回来哦？\x02\x03",

            "而且王都很大，\x01",
            "可别迷路啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x107,
        "#061F嗯，你就放心吧⊙\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x12F, 400)

    ChrTalk(    #247
        0x107,
        (
            "#560F那么小玲，\x01",
            "我们出发吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x107, 400)

    ChrTalk(    #248
        0x12F,
        "#265F#2P嗯，当然了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #249
        0x12F,
        "#261F#4P姐姐，一会儿见⊙\x02",
    )

    CloseMessageWindow()

    def lambda_652A():
        OP_6D(-230, 0, -3670, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_652A)
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)

    def lambda_654E():

        label("loc_654E")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_654E")

    QueueWorkItem2(0x101, 1, lambda_654E)

    def lambda_655F():

        label("loc_655F")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_655F")

    QueueWorkItem2(0x8, 1, lambda_655F)

    def lambda_6570():

        label("loc_6570")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6570")

    QueueWorkItem2(0xF7, 1, lambda_6570)

    def lambda_6581():

        label("loc_6581")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_6581")

    QueueWorkItem2(0x108, 1, lambda_6581)

    def lambda_6592():

        label("loc_6592")

        TurnDirection(0xFE, 0x12F, 0)
        OP_48()
        Jump("loc_6592")

    QueueWorkItem2(0x104, 1, lambda_6592)

    def lambda_65A3():

        label("loc_65A3")

        TurnDirection(0xFE, 0x12F, 0)
        OP_48()
        Jump("loc_65A3")

    QueueWorkItem2(0x105, 1, lambda_65A3)
    Sleep(200)
    OP_43(0x12F, 0x1, 0x0, 0x13)
    WaitChrThread(0x12F, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x108, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x8, 0x1)
    Sleep(500)
    OP_6D(-2590, 0, 1610, 2000)

    ChrTalk(    #250
        0x105,
        (
            "#048F#2P呵呵，她们很快\x01",
            "就交上朋友了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#1016F#5P嗯，果然是\x01",
            "同龄人啊。\x02\x03",

            "#1015F不过，小玲和\x01",
            "提妲的组合啊。\x02\x03",

            "有种说不清的不安。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #252
        0x105,
        "#044F#2P咦？为什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #253
        0x101,
        (
            "#1025F#6P不是，你想……\x01",
            "提妲不善于推辞。\x02\x03",

            "你不觉得她会被小玲\x01",
            "使唤得团团转吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x105,
        "#045F#2P确实……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x8, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6757")

    ChrTalk(    #255
        0x106,
        (
            "#050F#6P对了，艾南。\x02\x03",

            "你问出那孩子\x01",
            "父母的名字了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6790")

    label("loc_6757")


    ChrTalk(    #256
        0x103,
        (
            "#020F#6P对了，艾南。\x02\x03",

            "你问出那孩子\x01",
            "父母的名字了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6790")


    def lambda_6796():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6796)
    Sleep(50)

    def lambda_67A9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67A9)
    Sleep(50)

    def lambda_67BC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67BC)
    Sleep(50)

    def lambda_67CF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_67CF)
    Sleep(50)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #257
        0x8,
        (
            "#764F嗯，好不容易。\x02\x03",

            "#762F看来他们夫妇是\x01",
            "住在克洛斯贝尔自治州的贸易商。\x02\x03",

            "名字是哈罗德·海瓦斯，\x01",
            "以及索菲亚·海瓦斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1015F克洛斯贝尔自治州的贸易商，\x01",
            "哈罗德和索菲亚夫妇……\x02\x03",

            "#1006F嗯，我已经记下了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6907")

    ChrTalk(    #259
        0x106,
        (
            "#051F我这边也好了。\x02\x03",

            "结合恐吓信的调查，\x01",
            "我们开始询问情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6949")

    label("loc_6907")


    ChrTalk(    #260
        0x103,
        (
            "#021F我这边也好了。\x02\x03",

            "结合恐吓信的调查，\x01",
            "我们开始询问情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6949")


    ChrTalk(    #261
        0x8,
        (
            "#760F按之前说好的，请艾丝蒂尔小姐\x01",
            "去帝国、共和国大使馆和格兰赛尔城和\x01",
            "利贝尔通讯社。\x02\x03",

            "关于各大使馆，就拜托金先生和\x01",
            "奥利维尔先生帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x104,
        "#035F#6P嘿～交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x108,
        (
            "#070F就是说向大使们\x01",
            "做引见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x8,
        (
            "#760F关于格兰赛尔城堡，\x01",
            "就拜托殿下您了。\x02\x03",

            "请把艾丝蒂尔小姐引见\x01",
            "给合适的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x105,
        "#040F嗯，我明白。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x8,
        (
            "#761F利贝尔通讯方面自不必说，\x01",
            "艾丝蒂尔小姐自己是最合适的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1006F嗯，我会去问奈尔。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B57")

    ChrTalk(    #268
        0x8,
        (
            "#760F剩下的是大圣堂、飞船公社和\x01",
            "罗恩鲍姆酒店……\x02\x03",

            "都交给阿加特\x01",
            "来调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x106,
        (
            "#051F啊啊。\x01",
            "这样比较有效率。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BCA")

    label("loc_6B57")


    ChrTalk(    #270
        0x8,
        (
            "#760F剩下的是大圣堂、飞船公社和\x01",
            "罗恩鲍姆酒店……\x02\x03",

            "都交给雪拉扎德小姐\x01",
            "来调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x103,
        (
            "#020F嗯。\x01",
            "这样比较有效率。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BCA")


    ChrTalk(    #272
        0x101,
        "#1018F好，开工！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_8_42BC end

    def Function_9_6BF8(): pass

    label("Function_9_6BF8")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -320, -500, -7250, 0)

    def lambda_6C1F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C1F)
    OP_8E(0xFE, 0xFFFFFCEA, 0xFFFFFF06, 0xFFFFED54, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_9_6BF8 end

    def Function_10_6C47(): pass

    label("Function_10_6C47")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_6C6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C6E)
    OP_8E(0xFE, 0x140, 0xFFFFFE0C, 0xFFFFE458, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_10_6C47 end

    def Function_11_6C96(): pass

    label("Function_11_6C96")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 560, -500, -7230, 0)

    def lambda_6CBD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CBD)
    OP_8E(0xFE, 0x1B8, 0xFFFFFF06, 0xFFFFEC96, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_11_6C96 end

    def Function_12_6CE5(): pass

    label("Function_12_6CE5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -320, -500, -7250, 0)

    def lambda_6D0C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D0C)
    OP_8E(0xFE, 0xFFFFFE34, 0xFFFFFF06, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_12_6CE5 end

    def Function_13_6D34(): pass

    label("Function_13_6D34")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 560, -500, -7230, 0)

    def lambda_6D5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6D5B)
    OP_8E(0xFE, 0x2D0, 0xFFFFFF06, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_13_6D34 end

    def Function_14_6D83(): pass

    label("Function_14_6D83")

    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFF6C8, 0x0, 0xFFFFF646, 0x9C4, 0x0)
    OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFF61E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFEE8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_6D83 end

    def Function_15_6DFF(): pass

    label("Function_15_6DFF")


    def lambda_6E05():

        label("loc_6E05")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_6E05")

    QueueWorkItem2(0x12F, 2, lambda_6E05)
    Sleep(2300)
    OP_44(0x12F, 0x2)
    OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFF61E, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD7A, 0x0, 0xFFFFFEE8, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_6DFF end

    def Function_16_6E7A(): pass

    label("Function_16_6E7A")

    OP_8C(0xFE, 90, 500)
    OP_8E(0xFE, 0x5BE, 0x0, 0xFFFFFFE2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xDFC, 0x0, 0x708, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE2E, 0x0, 0x1338, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_6E7A end

    def Function_17_6EE2(): pass

    label("Function_17_6EE2")


    def lambda_6EE8():

        label("loc_6EE8")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_6EE8")

    QueueWorkItem2(0x12F, 2, lambda_6EE8)
    Sleep(800)
    OP_44(0x12F, 0x2)
    OP_8E(0xFE, 0xDFC, 0x0, 0x708, 0x9C4, 0x0)
    OP_8E(0xFE, 0xE10, 0x0, 0x12B6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFEF8E, 0xFA0, 0x1432, 0x9C4, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_6EE2 end

    def Function_18_6F49(): pass

    label("Function_18_6F49")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x276, 0xFFFFFF06, 0xFFFFE6CE, 0x7D0, 0x0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_6F74():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6F74)
    OP_8E(0xFE, 0x1E0, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_6F49 end

    def Function_19_6F9A(): pass

    label("Function_19_6F9A")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x276, 0xFFFFFF06, 0xFFFFE6CE, 0x7D0, 0x0)

    def lambda_6FBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6FBB)
    OP_8E(0xFE, 0x1E0, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_19_6F9A end

    def Function_20_6FEB(): pass

    label("Function_20_6FEB")

    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x668, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_6FEB end

    def Function_21_7007(): pass

    label("Function_21_7007")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x230, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_21_7007 end

    def Function_22_7023(): pass

    label("Function_22_7023")

    OP_8E(0xFE, 0xFFFFFF4C, 0x0, 0x668, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_22_7023 end

    def Function_23_703F(): pass

    label("Function_23_703F")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x230, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_23_703F end

    def Function_24_705B(): pass

    label("Function_24_705B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_707E")
    Call(0, 38)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)

    label("loc_707E")

    ClearMapFlags(0x1)
    OP_6D(-40, -250, -5780, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_70F4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -1780, 0, 1670, 270)
    Jump("loc_710A")

    label("loc_70F4")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1780, 0, 1670, 270)

    label("loc_710A")

    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x19)
    Sleep(400)
    OP_43(0x105, 0x0, 0x0, 0x1A)
    Sleep(400)
    OP_43(0x108, 0x0, 0x0, 0x1C)
    Sleep(400)
    OP_43(0x104, 0x0, 0x0, 0x1B)
    OP_0D()
    WaitChrThread(0x104, 0x0)

    ChrTalk(    #273
        0x101,
        "#1011F#5P我们回来了～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7183")

    def lambda_7178():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7178)
    Jump("loc_7191")

    label("loc_7183")


    def lambda_7189():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7189)

    label("loc_7191")


    def lambda_7197():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7197)

    def lambda_71A5():
        OP_6D(-2910, 0, 830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_71A5)

    def lambda_71BD():
        OP_67(0, 6310, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71BD)

    def lambda_71D5():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_71D5)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7215")

    ChrTalk(    #274
        0xA,
        (
            "#051F#2P哟，\x01",
            "回来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_7215")


    ChrTalk(    #275
        0x9,
        "#021F#2P哟，回来了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_7231")


    def lambda_7237():
        OP_8E(0xFE, 0xFFFFF880, 0x0, 0x3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7237)
    Sleep(200)

    def lambda_7257():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7257)
    Sleep(500)

    def lambda_7277():
        OP_8E(0xFE, 0xFFFFF5F6, 0x0, 0xFFFFFC36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7277)
    Sleep(500)

    def lambda_7297():
        OP_8E(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7297)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #276
        0x101,
        (
            "#1016F抱歉抱歉。\x01",
            "稍微晚了点。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #277
        0x101,
        (
            "#1011F嗯……\x01",
            "提妲和小玲呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x8,
        (
            "#761F#5P刚才已经\x01",
            "回来了。\x02\x03",

            "现在在楼上互相展示\x01",
            "购物的战果呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #279
        0x101,
        (
            "#1016F这样啊。\x01",
            "看来她们玩得挺高兴。\x02\x03",

            "#1006F那么，现在\x01",
            "我们也报告一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x8,
        (
            "#760F#5P嗯。\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_8C(0x101, 0, 400)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7531")

    ChrTalk(    #281
        0xA,
        (
            "#051F#2P原来如此……\x02\x03",

            "你们也搜集到\x01",
            "不少信息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1007F不过也还是没掌握什么\x01",
            "决定性的情报。\x02\x03",

            "#1015F阿加特你怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xA,
        (
            "#053F#2P老实说，哪边都没收获。\x02\x03",

            "大圣堂、酒店、飞船公社……\x02\x03",

            "都对寄来恐吓信的\x01",
            "罪犯没什么线索。\x02\x03",

            "#050F飞船公社虽然做好了\x01",
            "像上次空贼事件一样\x01",
            "接下来会受到金钱敲诈的准备……\x02\x03",

            "不过现在还没有那种要求出现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7679")

    label("loc_7531")


    ChrTalk(    #284
        0x9,
        (
            "#027F#2P原来如此……\x02\x03",

            "你们也搜集到\x01",
            "不少信息呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        (
            "#1007F不过也还是没掌握什么\x01",
            "决定性的情报。\x02\x03",

            "#1015F雪拉姐你怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x9,
        (
            "#025F#2P老实说，哪边都没收获。\x02\x03",

            "大圣堂、酒店、飞船公社……\x02\x03",

            "都对寄来恐吓信的\x01",
            "罪犯没什么线索。\x02\x03",

            "#022F飞船公社虽然做好了\x01",
            "像上次空贼事件一样\x01",
            "接下来会受到金钱敲诈的准备……\x02\x03",

            "不过现在还没有那种要求出现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7679")


    ChrTalk(    #287
        0x101,
        (
            "#1007F是吗……\x02\x03",

            "#1002F到头来，罪犯的人选\x01",
            "还是有很多种可能性……\x02\x03",

            "是『结社』所为的\x01",
            "可能性有多少？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x8,
        (
            "#764F#5P……很难说啊。\x02\x03",

            "#762F根据迄今为止的案件来看，\x01",
            "他们现在除了『福音』的\x01",
            "实验以外没什么动作。\x02\x03",

            "并且已知『福音』会引发\x01",
            "一般情况下不会发生的\x01",
            "现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x104,
        (
            "#032F#6P呼，从这一点上来看，\x01",
            "这次的恐吓事件确实有所不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x108,
        (
            "#072F现在还看不出和结社\x01",
            "有关的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015F嗯……\x01",
            "是不是有点草木皆兵了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x8,
        (
            "#764F#5P不，谨慎小心\x01",
            "是没错的。\x02\x03",

            "#760F总之我们现在已经把\x01",
            "该做的调查都做了。\x02\x03",

            "我会整理好\x01",
            "各位的报告的。\x02\x03",

            "明天可以请你们送去艾尔贝离宫\x01",
            "给希德中校吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7DA5")

    ChrTalk(    #293
        0x101,
        (
            "#1025F嗯……\x02\x03",

            "到头来还是没查出罪犯的身份，\x01",
            "虽然感觉很抱歉，不过也没办法。\x02\x03",

            "#1004F对了，阿加特。\x01",
            "小玲的事怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xA,
        (
            "#050F#2P那个倒是搞清楚一些事了。\x02\x03",

            "首先是酒店……\x01",
            "那孩子和父母只在王都\x01",
            "呆了两个星期。\x02\x03",

            "那段时间都一直\x01",
            "住在酒店的同一个房间。\x02\x03",

            "然后终于在今早\x01",
            "办理了退房手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        "#1002F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xA,
        (
            "#555F#2P接下来是大圣堂……\x02\x03",

            "他们在逗留期间好几次\x01",
            "去大圣堂做了礼拜。\x02\x03",

            "而招待他们的牧师觉得\x01",
            "夫妇二人的样子有点古怪。\x02\x03",

            "说是礼拜时好像心不在焉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x105,
        "#043F和希尔丹夫人的说法一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x101,
        "#1015F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "#053F#2P最后是飞船公社……\x02\x03",

            "#552F……实际上。\x01",
            "没找到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#1004F咦……什么没找到？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xA,
        (
            "#555F#2P克洛斯贝尔出身的\x01",
            "海瓦斯夫妇和玲……\x02\x03",

            "在半年时间内的乘客名单上\x01",
            "都没有相符的记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x101,
        "#1020F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x104,
        (
            "#032F#6P呼……真神秘。\x02\x03",

            "那么他们是不是通过\x01",
            "地面交通来的利贝尔？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #304
        "\x18\x07\x05玲是通过地面交通来的利贝尔？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【嗯、嗯……】\x01",      # 0
            "【这不可能】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7C59"),
        (1, "loc_7D03"),
        (SWITCH_DEFAULT, "loc_7DA2"),
    )


    label("loc_7C59")


    ChrTalk(    #305
        0x101,
        (
            "#1015F嗯、嗯……\x02\x03",

            "那要不要直接\x01",
            "问问玲？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "#552F#2P不……\x02\x03",

            "第一次在艾尔·雷登\x01",
            "遇见她时她不是说了？\x02\x03",

            "乘飞船到达的时候\x01",
            "看见了很大的湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x101,
        "#1002F啊，确实如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DA2")

    label("loc_7D03")

    OP_2B(0x89, 0x2)

    ChrTalk(    #308
        0x101,
        (
            "#1020F这、这不可能。\x02\x03",

            "因为第一次遇见她的时候，\x01",
            "我记得她说过\x01",
            "乘飞船到达什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xA,
        (
            "#552F#2P嗯，是在艾尔·雷登吧？\x02\x03",

            "我记得她说过\x01",
            "看见了很大的湖。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DA2")

    label("loc_7DA2")

    Jump("loc_82CA")

    label("loc_7DA5")


    ChrTalk(    #310
        0x101,
        (
            "#1025F嗯……\x02\x03",

            "到头来还是没查出罪犯的身份，\x01",
            "虽然感觉很抱歉，不过也没办法。\x02\x03",

            "#1004F对了，雪拉姐。\x01",
            "小玲的事怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x9,
        (
            "#020F#2P那个倒是\x01",
            "搞清楚一些事了。\x02\x03",

            "首先是酒店……\x01",
            "那孩子和父母在王都\x01",
            "呆了两星期左右。\x02\x03",

            "那段时间都一直\x01",
            "都住在同一间房间里。\x02\x03",

            "然后终于今天早上\x01",
            "办理了退房手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        "#1002F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#022F#2P接下来是大圣堂……\x02\x03",

            "他们在逗留期间好几次\x01",
            "去大圣堂做了礼拜。\x02\x03",

            "那么……\x01",
            "根据接待他们的牧师所说，\x01",
            "夫妇的样子有点古怪。\x02\x03",

            "好像礼拜时心不在焉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x105,
        "#043F和希尔丹夫人的说法一样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x101,
        "#1015F嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x9,
        (
            "#522F#2P最后是飞船公社……\x02\x03",

            "调查完乘客名单\x01",
            "发现了一件奇怪的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        "#1004F咦……奇怪的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        (
            "#026F#2P克洛斯贝尔出身的\x01",
            "海瓦斯夫妇和玲……\x02\x03",

            "#022F在半年时间内的乘客名单上\x01",
            "都没有相符的记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        "#1020F哎哎！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x104,
        (
            "#032F#6P呼……真神秘。\x02\x03",

            "那么他们是不是通过\x01",
            "地面交通来的利贝尔？\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #321
        "\x18\x07\x05玲是通过地面交通来的利贝尔？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【嗯、嗯……】\x01",      # 0
            "【这不可能】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8171"),
        (1, "loc_8225"),
        (SWITCH_DEFAULT, "loc_82CA"),
    )


    label("loc_8171")


    ChrTalk(    #322
        0x101,
        (
            "#1015F嗯、嗯……\x02\x03",

            "那要不要直接\x01",
            "问问玲？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x9,
        (
            "#522F#2P我说，艾丝蒂尔。\x02\x03",

            "第一次在艾尔·雷登\x01",
            "遇见她时她不是说了？\x02\x03",

            "乘飞船到达的时候\x01",
            "看见了很大的湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x101,
        "#1002F啊，确实如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_82CA")

    label("loc_8225")

    OP_2B(0x89, 0x2)

    ChrTalk(    #325
        0x101,
        (
            "#1020F这、这不可能。\x02\x03",

            "因为第一次遇见她的时候，\x01",
            "我记得她说过\x01",
            "乘飞船到达什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x9,
        (
            "#022F#2P是那次在艾尔·雷登的时候吧。\x02\x03",

            "我记得她说过\x01",
            "看见了很大的湖。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82CA")

    label("loc_82CA")


    ChrTalk(    #327
        0x8,
        (
            "#764F#5P嗯，原来如此。\x02\x03",

            "#762F那么他们夫妇有可能\x01",
            "是用了假名。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #328
        0x101,
        "#1020F假、假名……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x108,
        (
            "#072F可能有什么事不便示人\x01",
            "或者害怕引来麻烦……\x02\x03",

            "无论如何，他们似乎\x01",
            "在出行前就预测到危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        "#1003F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x8,
        (
            "#764F#5P关于玲小姐父母的事，\x01",
            "我已经联络了各地的协会。\x02\x03",

            "现在还是先别着急，\x01",
            "等着消息比较好。\x02\x03",

            "#760F总之玲小姐……\x02\x03",

            "还是暂时让他住在\x01",
            "协会比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x101,
        (
            "#1007F嗯……毕竟她也有\x01",
            "被卷入麻烦的危险。\x02\x03",

            "#1006F那个，方便的话就\x01",
            "交给我吧？\x02\x03",

            "毕竟这也是我接下的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x8,
        (
            "#761F#5P你能这么说真是帮了我大忙了。\x02\x03",

            "各位在王都期间的住宿\x01",
            "就由协会负责安排。\x02\x03",

            "玲小姐的住宿费用\x01",
            "也由我们出，请放心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x101,
        (
            "#1016F真是太谢谢你了。\x02\x03",

            "#1004F啊，说起来的话，\x01",
            "希尔丹夫人说……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_871A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #335
        (
            "\x07\x05艾丝蒂尔对阿加特\x01",
            "说了希尔丹夫人邀请他们\x01",
            "住在王城的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #336
        0x8,
        "#763F#5P哟，还有这种事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        (
            "#053F#2P……我就算了。\x02\x03",

            "#050F住了那么多次，\x01",
            "感觉还是太拘谨了。\x02\x03",

            "住酒店的话，万一有什么事\x01",
            "也方便联络协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1015F确实也有道理……\x02\x03",

            "没准玲的父母还会\x01",
            "联系我们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #339
        0x101,
        (
            "#1025F#5P科洛丝。\x01",
            "不好意思……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #340
        0x105,
        (
            "#048F呵呵，不用介意。\x02\x03",

            "我会去跟\x01",
            "希尔丹夫人解释。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88BA")

    label("loc_871A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #341
        (
            "\x07\x05艾丝蒂尔对雪拉扎德\x01",
            "说了希尔丹夫人邀请他们\x01",
            "住在王城的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #342
        0x8,
        "#763F#5P哟，还有这种事啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x9,
        (
            "#025F#2P唔，说实话这是个\x01",
            "令人感激的提议……\x02\x03",

            "#020F不过这次\x01",
            "就算了吧。\x02\x03",

            "万一有什么事，住酒店的话\x01",
            "也方便联络协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x101,
        (
            "#1015F确实也有道理……\x02\x03",

            "没准玲的父母还会\x01",
            "联系我们。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #345
        0x101,
        (
            "#1025F#5P科洛丝。\x01",
            "不好意思……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #346
        0x105,
        (
            "#048F呵呵，不用介意。\x02\x03",

            "我会去跟\x01",
            "希尔丹夫人解释。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88BA")


    ChrTalk(    #347
        0x104,
        (
            "#030F#6P我和金先生\x01",
            "住在各自的大使馆。\x02\x03",

            "公主殿下则住在格兰赛尔城城堡。\x02\x03",

            "你们两个和童子军\x01",
            "是准备要住酒店。\x02\x03",

            "#031F在此之前，怎么样？\x02\x03",

            "难得一聚，要不要一起\x01",
            "去酒馆吃个饭？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    def lambda_8973():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8973)

    def lambda_8981():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_8981)
    Sleep(500)

    ChrTalk(    #348
        0x101,
        (
            "#1006F#2P啊，好啊。\x02\x03",

            "也好久没听\x01",
            "奥利维尔弹钢琴了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #349
        0x104,
        (
            "#035F#6P呵呵，荣幸之至\x01",
            "让我高兴啊。\x02\x03",

            "#037F艾丝蒂尔你也终于\x01",
            "能品味成年人的情趣了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1019F#2P别说这种\x01",
            "不正经的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x108,
        (
            "#070F#5P不过这样的话，\x01",
            "我们就立即动身吧。\x02\x03",

            "这么一大群人，\x01",
            "也有可能找不到座位。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8AEB")

    ChrTalk(    #352
        0xA,
        (
            "#051F好，叫上小家伙们，\x01",
            "赶紧出发去酒店吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B1B")

    label("loc_8AEB")


    ChrTalk(    #353
        0x9,
        (
            "#021F呵呵，叫上那两个孩子，\x01",
            "一起去酒店吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B1B")

    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #354
        (
            "\x07\x05当晚，艾丝蒂尔一行人和玲一起\x01",
            "在『阳光铃铛酒廊』吃了晚饭。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #355
        (
            "\x07\x05当然，也伴随着畅饮和\x01",
            "奥利维尔的钢琴演奏……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #356
        (
            "\x07\x05最后连奈尔和穆拉都被\x01",
            "叫来酒馆参与到其中……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #357
        "\x07\x05王都的傍晚就这样快乐地过去了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    RemoveParty(0x4, 0xFF)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8C29")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_8C2D")

    label("loc_8C29")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_8C2D")

    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4153   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_705B end

    def Function_25_8C3A(): pass

    label("Function_25_8C3A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -150, -500, -7230, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8C61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C61)
    OP_8E(0xFE, 0xFFFFFEDE, 0xFFFFFF06, 0xFFFFEC82, 0x7D0, 0x0)
    Return()

    # Function_25_8C3A end

    def Function_26_8C82(): pass

    label("Function_26_8C82")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 590, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8CA9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CA9)
    OP_8E(0xFE, 0x38E, 0xFFFFFF06, 0xFFFFE8F4, 0x7D0, 0x0)
    Return()

    # Function_26_8C82 end

    def Function_27_8CCA(): pass

    label("Function_27_8CCA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 190, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8CF1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CF1)
    OP_8E(0xFE, 0xFFFFFFCE, 0xFFFFFF06, 0xFFFFE796, 0x7D0, 0x0)
    Return()

    # Function_27_8CCA end

    def Function_28_8D12(): pass

    label("Function_28_8D12")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, -500, -7250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8D39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8D39)
    OP_8E(0xFE, 0xFFFFFC22, 0xFFFFFF06, 0xFFFFE886, 0x7D0, 0x0)
    Return()

    # Function_28_8D12 end

    def Function_29_8D5A(): pass

    label("Function_29_8D5A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D7F")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DA9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9B")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_8D9F")

    label("loc_8D9B")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_8D9F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8DA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DD3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DC5")
    AddParty(0x6, 0xFA, 0xFF)
    Jump("loc_8DC9")

    label("loc_8DC5")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_8DC9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DEE")
    AddParty(0x7, 0xFB, 0xFF)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_8DEE")

    Return()

    # Function_29_8D5A end

    def Function_30_8DEF(): pass

    label("Function_30_8DEF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E14")
    Call(0, 38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8E10")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_8E14")

    label("loc_8E10")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_8E14")

    OP_4A(0xC, 255)
    OP_4A(0x8, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 90, -500, -7250, 0)
    SetChrPos(0xF7, 90, -500, -7250, 0)
    SetChrPos(0x107, 90, -500, -7250, 0)
    SetChrPos(0x12F, 90, -500, -7250, 0)
    SetChrPos(0xC, -2130, 0, -50, 270)
    SetChrPos(0xE, -2170, 0, 1060, 270)
    OP_6D(-4300, 0, 1620, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #358
        0x101,
        "#2P我们回来了～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_8C(0x8, 135, 400)
    OP_8C(0xE, 180, 400)

    def lambda_8F05():

        label("loc_8F05")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8F05")

    QueueWorkItem2(0x8, 1, lambda_8F05)

    ChrTalk(    #359
        0xE,
        "#070F#2P哟，回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xC,
        "#041F#5P各位，欢迎回来。\x02",
    )

    CloseMessageWindow()

    def lambda_8F50():
        OP_6D(-3840, 0, 950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F50)

    def lambda_8F68():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F68)
    OP_43(0x101, 0x0, 0x0, 0x1F)
    Sleep(600)
    OP_8C(0xE, 90, 400)

    def lambda_8F93():
        OP_8E(0xFE, 0xFFFFF93E, 0x0, 0x5FA, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8F93)
    Sleep(200)
    OP_8C(0xC, 90, 400)

    def lambda_8FBA():
        OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0x230, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8FBA)
    WaitChrThread(0xE, 0x0)

    def lambda_8FDA():

        label("loc_8FDA")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8FDA")

    QueueWorkItem2(0xE, 1, lambda_8FDA)
    OP_43(0xF7, 0x1, 0x0, 0x20)
    Sleep(400)
    WaitChrThread(0xC, 0x0)

    def lambda_8FFC():

        label("loc_8FFC")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8FFC")

    QueueWorkItem2(0xC, 1, lambda_8FFC)
    OP_43(0x107, 0x1, 0x0, 0x21)
    Sleep(600)
    OP_43(0x12F, 0x1, 0x0, 0x22)
    WaitChrThread(0x12F, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0xE, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0x8, 0x1)
    OP_8C(0xC, 270, 400)
    OP_8C(0xE, 270, 400)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #361
        0x8,
        (
            "#760F#5P辛苦了。\x01",
            "报告书已经交了吧、\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x101,
        "#1000F嗯，那个搞定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x8,
        (
            "#760F#5P刚才王国军汇来了\x01",
            "报酬。\x02\x03",

            "你们赶紧\x01",
            "拿好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x4, 0x10)
    OP_AF(0xCD, 0x8B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #364
        0x101,
        (
            "#1001F#4P不愧是希德中校。\x01",
            "工作真有效率。\x02\x03",

            "#1015F不过……\x01",
            "我听说柏斯地区\x01",
            "出现了特务兵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x8,
        (
            "#762F#5P离宫那边也收到\x01",
            "消息了吧。\x02\x03",

            "我正准备和你们\x01",
            "谈谈这个。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_94AE")

    ChrTalk(    #366
        0x106,
        (
            "#050F#6P是协会的人\x01",
            "发现的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x8,
        (
            "#764F#5P嗯……\x01",
            "是雪拉扎德小姐她们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #368
        0x101,
        "#1004F#4P雪拉姐她们！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x8,
        (
            "#762F#5P说是在拉文努的废坑\x01",
            "内部发现了他们的基地。\x02\x03",

            "不巧的是他们\x01",
            "已经离开了那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1002F#4P拉文努废坑的内部……\x01",
            "和空贼战斗过的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x106,
        (
            "#555F#6P切，真是个盲点……\x02\x03",

            "离开了就意味着\x01",
            "转去别的地方了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x8,
        (
            "#765F#5P关于这点，据说在柏斯\x01",
            "各地都有人目击到特务兵……\x02\x03",

            "现在，国境师团正在倾巢\x01",
            "出动进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x101,
        (
            "#1015F#4P这、这样啊……\x02\x03",

            "我们是不是也该去\x01",
            "柏斯帮忙呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x8,
        (
            "#762F#5P不，敌人有可能是声东击西。\x02\x03",

            "在了解当地情况之前\x01",
            "还是不要擅自行动为好。\x02\x03",

            "而且看来……\x01",
            "『结社』也有动向了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x101,
        "#1020F#4P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x106,
        "#054F#6P你说什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x8,
        (
            "#764F#5P雪拉扎德小姐她们\x01",
            "在废坑碰见了。\x02\x03",

            "#762F『小丑』肯帕雷拉──\x01",
            "似乎是『执行者』中的一个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x106,
        "#555F#6P呼，又是一张新面孔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_97BB")

    label("loc_94AE")


    ChrTalk(    #379
        0x103,
        (
            "#020F#6P是协会的人\x01",
            "发现的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        (
            "#764F#5P嗯……\x01",
            "是阿加特他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #381
        0x101,
        "#1004F#4P阿加特！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x8,
        (
            "#762F#5P说是在拉文努的废坑\x01",
            "内部发现了他们的基地。\x02\x03",

            "不巧的是他们\x01",
            "已经离开了那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x101,
        (
            "#1002F#4P拉文努废坑的内部……\x01",
            "是和空贼战斗过的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x103,
        (
            "#026F#6P原来如此，果然是个盲点。\x02\x03",

            "#022F离开了就意味着\x01",
            "转去别的地方了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x8,
        (
            "#765F#5P关于这点，据说在柏斯\x01",
            "各地都有人目击到特务兵……\x02\x03",

            "现在，国境师团正在倾巢\x01",
            "出动进行调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1015F#4P这、这样啊……\x02\x03",

            "我们是不是也该去\x01",
            "柏斯帮忙呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x8,
        (
            "#762F#5P不，在了解当地情况之前\x01",
            "还是不要擅自行动为好。\x02\x03",

            "而且看来……\x01",
            "『结社』也有动向了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x101,
        "#1020F#4P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x103,
        "#024F#6P你说什么……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#764F#5P阿加特他们\x01",
            "在废坑碰见了。\x02\x03",

            "#762F『小丑』肯帕雷拉──\x01",
            "似乎是『执行者』中的一个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x103,
        "#022F#6P呼，又是一张新面孔……\x02",
    )

    CloseMessageWindow()

    label("loc_97BB")


    ChrTalk(    #392
        0x8,
        (
            "#762F#5P而且在那个基地还\x01",
            "发现了奇怪的东西。\x02\x03",

            "首先是名叫『奥尔杰尤』的\x01",
            "导力驱动的交通工具的设计图……\x02\x03",

            "还有就是代号为『茶会』的\x01",
            "神秘计划记录。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1015F#4P『奥尔杰尤』『茶会』……\x02\x03",

            "#1007F唔，真不知所云。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x107,
        (
            "#065F#6P导力驱动的交通工具\x01",
            "是什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xC,
        (
            "#049F茶会这个说法\x01",
            "令人比较在意……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_43(0x12F, 0x1, 0x0, 0x23)
    Sleep(2000)
    OP_63(0x101)
    OP_63(0x107)
    OP_63(0xC)
    OP_63(0xE)
    OP_63(0x8)
    OP_63(0xF7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_999D")

    ChrTalk(    #396
        0x106,
        (
            "#552F#6P切，真是不让人\x01",
            "清净啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99C2")

    label("loc_999D")


    ChrTalk(    #397
        0x103,
        (
            "#025F#6P呼，真是不让人\x01",
            "清净啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C2")

    OP_8C(0xE, 180, 400)

    ChrTalk(    #398
        0xE,
        (
            "#070F#2P不过也别着急。\x02\x03",

            "因为当地的军队和\x01",
            "协会都在努力。\x02\x03",

            "很快就能了解到情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x8,
        (
            "#760F#5P嗯，虽然令人着急，\x01",
            "不过还是请先留在王都。\x02\x03",

            "现在你们可以各自\x01",
            "自由活动。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xE, 270, 400)

    ChrTalk(    #400
        0x101,
        "#1007F#4P唔，虽然这么说……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    OP_8C(0x101, 135, 400)
    Sleep(500)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #401
        0x101,
        (
            "#1004F#4P咦？说起来\x01",
            "奥利维尔去哪儿了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x8,
        (
            "#760F#5P关于他，帝国大使馆\x01",
            "刚才联系了我们……\x02\x03",

            "他说有点私事，\x01",
            "就出去了。\x02\x03",

            "还说很快会\x01",
            "回到协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x101,
        (
            "#1015F#4P哦～？\x01",
            "是什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_9BA5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9BA5)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #404
        0x101,
        "#1004F#5P……咦？\x02",
    )

    CloseMessageWindow()

    def lambda_9BCF():
        OP_6D(-2510, 0, -500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BCF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #405
        0x101,
        "#1026F#5P玲呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x107,
        "#064F#6P啊……？\x02",
    )

    CloseMessageWindow()

    def lambda_9C17():
        OP_8C(0xC, 180, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_9C17)

    def lambda_9C25():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_9C25)
    Sleep(100)

    def lambda_9C38():
        OP_8C(0x8, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_9C38)

    def lambda_9C46():
        OP_8C(0xE, 180, 400)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_9C46)
    Sleep(100)
    OP_43(0x107, 0x1, 0x0, 0x24)
    OP_8C(0x107, 180, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 180, 300)
    OP_44(0x107, 0x1)

    ChrTalk(    #407
        0x107,
        (
            "#065F#5P咦、咦咦……\x02\x03",

            "刚才\x01",
            "还在的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9CAC():
        OP_6D(-3840, 0, 950, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9CAC)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #408
        0x101,
        (
            "#1015F#5P难道是……\x02\x03",

            "听我们说话太无聊\x01",
            "就出去了？？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_9D08():
        OP_8C(0x8, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9D08)

    def lambda_9D16():
        OP_8C(0xC, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9D16)

    def lambda_9D24():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9D24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9D4C")

    ChrTalk(    #409
        0x106,
        "#051F#6P有可能。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D68")

    label("loc_9D4C")


    ChrTalk(    #410
        0x103,
        "#524F#6P唔～很有可能。\x02",
    )

    CloseMessageWindow()

    label("loc_9D68")


    ChrTalk(    #411
        0x101,
        (
            "#1007F#5P真是的～拿她没办法。\x02\x03",

            "#1015F可她万一离开了王都\x01",
            "也不能丢下她不管……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)
    Sleep(500)

    ChrTalk(    #412
        0x101,
        (
            "#1006F#5P……我去找找\x01",
            "那孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x107,
        (
            "#560F#6P啊，我也去！\x02\x03",

            "我有可能知道\x01",
            "小玲会去哪儿……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #414
        0x101,
        "#1006F#5P是吗？那就太好了。\x02",
    )

    CloseMessageWindow()

    def lambda_9E51():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E51)
    Sleep(50)

    def lambda_9E64():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9E64)
    OP_8C(0x107, 315, 400)
    OP_8C(0xE, 270, 400)

    ChrTalk(    #415
        0x101,
        (
            "#1015F#4P艾南先生。\x01",
            "你看这事儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x8,
        (
            "#760F#5P嗯，拜托了。\x02\x03",

            "我去和各地支部\x01",
            "就余党的去向\x01",
            "交换一下信息。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    RemoveParty(0x2E, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-5650, 0, -18030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6E(262, 0)
    SetChrName("")

    AnonymousTalk(    #417
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择固定队员外的一名同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9FA3")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_9FB4")

    label("loc_9FA3")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_9FB4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_30_8DEF end

    def Function_31_9FCA(): pass

    label("Function_31_9FCA")

    OP_8E(0xFE, 0xFFFFF600, 0x0, 0x1F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_31_9FCA end

    def Function_32_9FE6(): pass

    label("Function_32_9FE6")

    OP_8E(0xFE, 0xFFFFF952, 0x0, 0xFFFFFCFE, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_32_9FE6 end

    def Function_33_A002(): pass

    label("Function_33_A002")

    OP_8E(0xFE, 0xFFFFF646, 0x0, 0xFFFFF9B6, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_33_A002 end

    def Function_34_A01E(): pass

    label("Function_34_A01E")

    OP_8E(0xFE, 0xFFFFFA88, 0x0, 0xFFFFF70E, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_A01E end

    def Function_35_A03A(): pass

    label("Function_35_A03A")

    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFFFB0, 0xFFFFFE0C, 0xFFFFE3B8, 0x7D0, 0x0)
    SetChrFlags(0x12F, 0x80)
    Return()

    # Function_35_A03A end

    def Function_36_A060(): pass

    label("Function_36_A060")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A083")
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_36_A060")

    label("loc_A083")

    Return()

    # Function_36_A060 end

    def Function_37_A084(): pass

    label("Function_37_A084")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A0A4")
    Call(0, 38)
    Call(0, 40)
    FadeToBright(0, 0)

    label("loc_A0A4")

    Fade(1000)
    SetChrPos(0x101, 26120, 0, 58670, 270)
    SetChrPos(0x107, 26210, 0, 57560, 270)
    SetChrPos(0xF7, 27510, 0, 57390, 270)
    SetChrPos(0xF9, 27360, 0, 58520, 270)
    OP_8C(0x19, 180, 0)
    OP_6D(25020, 0, 58400, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #418
        0x101,
        (
            "#1018F#6P没有颜色的鱼……\x01",
            "是这个啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A1A2")

    ChrTalk(    #419
        0x106,
        "#051F#6P原来是鱼的拓本啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1C2")

    label("loc_A1A2")


    ChrTalk(    #420
        0x103,
        "#021F#6P原来是鱼的拓本啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A1C2")

    OP_4A(0x19, 255)
    OP_6D(26740, 0, 61110, 1200)

    ChrTalk(    #421
        0x19,
        (
            "哟，你们对这副鱼的拓本\x01",
            "感兴趣吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x19,
        (
            "这是在下赢得\x01",
            "闪耀的荣光之证啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x19,
        (
            "方便的话，我可以给你们讲讲\x01",
            "那个勇敢者的故事。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C2")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_A300")

    label("loc_A2C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E9")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_A300")

    label("loc_A2E9")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_A300")

    Sleep(1000)

    def lambda_A30B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A30B)
    Sleep(100)

    def lambda_A31E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A31E)
    Sleep(100)

    def lambda_A331():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A331)
    Sleep(100)

    def lambda_A344():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A344)
    Sleep(500)

    ChrTalk(    #424
        0x101,
        (
            "#1016F#5P嗯，这还是\x01",
            "留待下次吧……\x02\x03",

            "#1006F有没有一个穿着白色\x01",
            "礼服的女孩子来过？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x19,
        "哦，来过啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x19,
        (
            "问了在下一个奇怪的问题，\x01",
            "然后就走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x101,
        "#1007F#5P果然是这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x107,
        (
            "#065F#6P请问请问，\x01",
            "那是个什么样的问题？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x19,
        "嗯，如果我没记错的话，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x19,
        (
            "是『你知道又辣又苦又美味\x01",
            "的店在哪里吗？』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4AB")

    ChrTalk(    #431
        0x108,
        "#070F#6P真是谜团重重啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A4C9")

    label("loc_A4AB")


    ChrTalk(    #432
        0x105,
        "#045F#6P真是谜团重重啊。\x02",
    )

    CloseMessageWindow()

    label("loc_A4C9")


    ChrTalk(    #433
        0x101,
        "#1006F#5P『又辣又苦又美味的店』。\x02",
    )

    CloseMessageWindow()

    def lambda_A4F6():
        OP_6D(26150, 0, 59560, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4F6)
    OP_8C(0x101, 135, 400)
    OP_8C(0xF7, 315, 400)
    OP_8C(0xF9, 270, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #434
        0x101,
        (
            "#1006F#5P那就去找找\x01",
            "那家店吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1632)
    OP_28(0x8C, 0x1, 0x40)
    OP_4B(0x19, 255)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    EventEnd(0x0)
    Return()

    # Function_37_A084 end

    def Function_38_A562(): pass

    label("Function_38_A562")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A5DC"),
        (1, "loc_A5E2"),
        (SWITCH_DEFAULT, "loc_A5E8"),
    )


    label("loc_A5DC")

    OP_A2(0x1200)
    Jump("loc_A5E8")

    label("loc_A5E2")

    OP_A2(0x1201)
    Jump("loc_A5E8")

    label("loc_A5E8")

    Return()

    # Function_38_A562 end

    def Function_39_A5E9(): pass

    label("Function_39_A5E9")

    ClearMapFlags(0x1)
    OP_6D(-5650, 0, -18030, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A62C")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_A64A")

    label("loc_A62C")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_A64A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_39_A5E9 end

    def Function_40_A66A(): pass

    label("Function_40_A66A")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A6A9")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_A6C3")

    label("loc_A6A9")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_A6C3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_40_A66A end

    def Function_41_A6E3(): pass

    label("Function_41_A6E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A6F4")
    OP_2A(0xBD, 0xBE, 0xFFFF)
    Jump("loc_A741")

    label("loc_A6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A70B")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xA9, 0xFFFF)
    Jump("loc_A741")

    label("loc_A70B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_A720")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xFFFF)
    Jump("loc_A741")

    label("loc_A720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A733")
    OP_2A(0xAA, 0xAC, 0xC4, 0xFFFF)
    Jump("loc_A741")

    label("loc_A733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_A741")
    OP_2A(0xAA, 0xAC, 0xFFFF)

    label("loc_A741")

    TalkEnd(0xFF)
    Return()

    # Function_41_A6E3 end

    SaveToFile()

Try(main)
