from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2510   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2510.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '罗基克',                               # 9
        '塞尔玛',                               # 10
        '汉斯',                                 # 11
        '巴托姆',                               # 12
        '弗雷',                                 # 13
        '乔儿',                                 # 14
        '罗迪',                                 # 15
        '米克',                                 # 16
        '碧欧拉老师',                           # 17
        '安敦',                                 # 18
        '利库斯',                               # 19
        '罗伊斯',                               # 20
        '莫妮卡',                               # 21
        '克拉拉',                               # 22
        '雷克特',                               # 23
        '雷欧',                                 # 24
        '科林兹校长',                           # 25
        '拉迪奥老师',                           # 26
        '米丽亚老师',                           # 27
        '芙拉瑟',                               # 28
        '蕾娜',                                 # 29
        '德尼斯',                               # 30
        '利戈尔',                               # 31
        '露西',                                 # 32
        '坎诺',                                 # 33
        '雅莉丝',                               # 34
        '珐奥娜',                               # 35
        '来学院的客人',                         # 36
        '资料',                                 # 37
        '目标用照相机',                         # 38
        '',                                     # 39
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
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01580 ._CH',             # 00
        'ED6_DT07/CH01590 ._CH',             # 01
        'ED6_DT07/CH01090 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH02670 ._CH',             # 06
        'ED6_DT07/CH02680 ._CH',             # 07
        'ED6_DT07/CH02600 ._CH',             # 08
        'ED6_DT07/CH02603 ._CH',             # 09
        'ED6_DT07/CH02550 ._CH',             # 0A
        'ED6_DT07/CH02390 ._CH',             # 0B
        'ED6_DT07/CH01210 ._CH',             # 0C
        'ED6_DT07/CH02900 ._CH',             # 0D
        'ED6_DT07/CH02910 ._CH',             # 0E
        'ED6_DT07/CH01083 ._CH',             # 0F
        'ED6_DT07/CH01583 ._CH',             # 10
        'ED6_DT07/CH01363 ._CH',             # 11
        'ED6_DT07/CH01373 ._CH',             # 12
        'ED6_DT07/CH01593 ._CH',             # 13
        'ED6_DT07/CH01093 ._CH',             # 14
        'ED6_DT07/CH02393 ._CH',             # 15
        'ED6_DT07/CH02553 ._CH',             # 16
        'ED6_DT07/CH00043 ._CH',             # 17
        'ED6_DT26/CH20782 ._CH',             # 18
        'ED6_DT26/CH20783 ._CH',             # 19
        'ED6_DT26/CH20777 ._CH',             # 1A
        'ED6_DT26/CH20779 ._CH',             # 1B
        'ED6_DT26/CH20780 ._CH',             # 1C
        'ED6_DT26/CH20783 ._CH',             # 1D
        'ED6_DT07/CH01430 ._CH',             # 1E
        'ED6_DT07/CH01660 ._CH',             # 1F
        'ED6_DT07/CH02490 ._CH',             # 20
        'ED6_DT07/CH01663 ._CH',             # 21
        'ED6_DT07/CH01213 ._CH',             # 22
        'ED6_DT07/CH01433 ._CH',             # 23
        'ED6_DT07/CH02690 ._CH',             # 24
        'ED6_DT07/CH02700 ._CH',             # 25
        'ED6_DT07/CH01200 ._CH',             # 26
        'ED6_DT26/CH20278 ._CH',             # 27
    )

    AddCharChipPat(
        'ED6_DT07/CH01580P._CP',             # 00
        'ED6_DT07/CH01590P._CP',             # 01
        'ED6_DT07/CH01090P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH02670P._CP',             # 06
        'ED6_DT07/CH02680P._CP',             # 07
        'ED6_DT07/CH02600P._CP',             # 08
        'ED6_DT07/CH02603P._CP',             # 09
        'ED6_DT07/CH02550P._CP',             # 0A
        'ED6_DT07/CH02390P._CP',             # 0B
        'ED6_DT07/CH01210P._CP',             # 0C
        'ED6_DT07/CH02900P._CP',             # 0D
        'ED6_DT07/CH02910P._CP',             # 0E
        'ED6_DT07/CH01083P._CP',             # 0F
        'ED6_DT07/CH01583P._CP',             # 10
        'ED6_DT07/CH01363P._CP',             # 11
        'ED6_DT07/CH01373P._CP',             # 12
        'ED6_DT07/CH01593P._CP',             # 13
        'ED6_DT07/CH01093P._CP',             # 14
        'ED6_DT07/CH02393P._CP',             # 15
        'ED6_DT07/CH02553P._CP',             # 16
        'ED6_DT07/CH00043P._CP',             # 17
        'ED6_DT26/CH20782P._CP',             # 18
        'ED6_DT26/CH20783P._CP',             # 19
        'ED6_DT26/CH20777P._CP',             # 1A
        'ED6_DT26/CH20779P._CP',             # 1B
        'ED6_DT26/CH20780P._CP',             # 1C
        'ED6_DT26/CH20783P._CP',             # 1D
        'ED6_DT07/CH01430P._CP',             # 1E
        'ED6_DT07/CH01660P._CP',             # 1F
        'ED6_DT07/CH02490P._CP',             # 20
        'ED6_DT07/CH01663P._CP',             # 21
        'ED6_DT07/CH01213P._CP',             # 22
        'ED6_DT07/CH01433P._CP',             # 23
        'ED6_DT07/CH02690P._CP',             # 24
        'ED6_DT07/CH02700P._CP',             # 25
        'ED6_DT07/CH01200P._CP',             # 26
        'ED6_DT26/CH20278P._CP',             # 27
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 86720,
        Z                   = 0,
        Y                   = 4320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 95280,
        Z                   = 250,
        Y                   = 30600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 48590,
        Z                   = 0,
        Y                   = 31310,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 49940,
        Z                   = 0,
        Y                   = 31300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 37390,
        Z                   = 0,
        Y                   = 950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 2150,
        Z                   = 0,
        Y                   = 4260,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 41720,
        Z                   = 0,
        Y                   = 39400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -3930,
        Z                   = 0,
        Y                   = 5390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 41200,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 131111,
        ChipIndex           = 0x27,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 116010,
        TriggerZ            = 0,
        TriggerY            = 2750,
        TriggerRange        = 400,
        ActorX              = 116010,
        ActorZ              = 1700,
        ActorY              = 4800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51030,
        TriggerZ            = 0,
        TriggerY            = 2090,
        TriggerRange        = 400,
        ActorX              = 51030,
        ActorZ              = 800,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36970,
        TriggerZ            = 0,
        TriggerY            = 2040,
        TriggerRange        = 800,
        ActorX              = 36970,
        ActorZ              = 1000,
        ActorY              = 2040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113820,
        TriggerZ            = 0,
        TriggerY            = 500,
        TriggerRange        = 800,
        ActorX              = 113820,
        ActorZ              = 600,
        ActorY              = 500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41150,
        TriggerZ            = 0,
        TriggerY            = 5500,
        TriggerRange        = 400,
        ActorX              = 41200,
        ActorZ              = 1700,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 50,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_682",          # 00, 0
        "Function_1_AF5",          # 01, 1
        "Function_2_BC2",          # 02, 2
        "Function_3_D3F",          # 03, 3
        "Function_4_D63",          # 04, 4
        "Function_5_D87",          # 05, 5
        "Function_6_FB5",          # 06, 6
        "Function_7_129A",         # 07, 7
        "Function_8_1DDF",         # 08, 8
        "Function_9_21B0",         # 09, 9
        "Function_10_253A",        # 0A, 10
        "Function_11_284B",        # 0B, 11
        "Function_12_2C49",        # 0C, 12
        "Function_13_2E19",        # 0D, 13
        "Function_14_3125",        # 0E, 14
        "Function_15_33BD",        # 0F, 15
        "Function_16_3A1D",        # 10, 16
        "Function_17_3BA1",        # 11, 17
        "Function_18_3CC3",        # 12, 18
        "Function_19_3DF3",        # 13, 19
        "Function_20_3F4E",        # 14, 20
        "Function_21_418A",        # 15, 21
        "Function_22_4267",        # 16, 22
        "Function_23_44C1",        # 17, 23
        "Function_24_4596",        # 18, 24
        "Function_25_46A4",        # 19, 25
        "Function_26_5288",        # 1A, 26
        "Function_27_5309",        # 1B, 27
        "Function_28_535F",        # 1C, 28
        "Function_29_53FE",        # 1D, 29
        "Function_30_5F61",        # 1E, 30
        "Function_31_6093",        # 1F, 31
        "Function_32_61A1",        # 20, 32
        "Function_33_6242",        # 21, 33
        "Function_34_6303",        # 22, 34
        "Function_35_63E9",        # 23, 35
        "Function_36_64AA",        # 24, 36
        "Function_37_6934",        # 25, 37
        "Function_38_6975",        # 26, 38
        "Function_39_6EE5",        # 27, 39
        "Function_40_817B",        # 28, 40
        "Function_41_81E1",        # 29, 41
        "Function_42_8232",        # 2A, 42
        "Function_43_824D",        # 2B, 43
        "Function_44_82AE",        # 2C, 44
        "Function_45_830F",        # 2D, 45
        "Function_46_835F",        # 2E, 46
        "Function_47_8867",        # 2F, 47
        "Function_48_88D1",        # 30, 48
        "Function_49_8A90",        # 31, 49
        "Function_50_8BAF",        # 32, 50
    )


    def Function_0_682(): pass

    label("Function_0_682")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_72D")
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 83020, 0, 4760, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 52560, 0, 1300, 90)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 53740, 0, 1300, 270)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 42100, 0, 32000, 0)
    OP_43(0x1B, 0x0, 0x0, 0x3)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 85660, 0, 34110, 270)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 87380, 0, 35160, 270)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_A7A")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_759")
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 40990, 0, 5500, 0)
    Jump("loc_78A")

    label("loc_759")

    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x10)
    SetChrPos(0x1E, 43110, 0, 4420, 270)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 41740, 0, 4420, 90)

    label("loc_78A")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 87640, 200, 2820, 270)
    SetChrFlags(0x21, 0x10)
    SetChrFlags(0x21, 0x4)
    OP_4A(0x21, 255)
    SetChrChipByIndex(0x21, 33)
    SetChrSubChip(0x21, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 45220, 0, 33500, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 36840, 0, 1520, 0)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 93410, 0, 33000, 180)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 92900, 0, 34100, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 83550, 0, -1490, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 93410, 0, 31740, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -2750, 100, 4100, 90)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x16, 0x4)
    OP_4A(0x16, 255)
    SetChrChipByIndex(0x16, 17)
    SetChrSubChip(0x16, 0)
    Jump("loc_A7A")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_945")
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 89300, 0, 2340, 90)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 85410, 0, 4250, 180)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 36770, 0, 1580, 0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 5080, 250, 30340, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -3730, 0, 32759, 180)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 85660, 0, 30050, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x14, -3880, 0, 31380, 0)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x26, 4800, 250, -1060, 90)
    Jump("loc_A7A")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_A7A")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7140, 0, 34280, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -7140, 0, 33020, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A")
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x1B, 0x10)

    label("loc_98A")

    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 84100, 100, 30000, 90)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x13, 0x4)
    OP_4A(0x13, 255)
    SetChrChipByIndex(0x13, 16)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x2C, 1300, 180, 34060, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x800)
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A")
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 84400, 200, 1000, 90)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    OP_4A(0x18, 255)
    SetChrChipByIndex(0x18, 34)
    SetChrSubChip(0x18, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 87690, 0, 4200, 270)

    label("loc_A7A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AA9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 39)

    label("loc_AA9")

    Jump("loc_AF4")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AD2")
    OP_A3(0x2504)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 38)

    label("loc_AD2")

    Jump("loc_AF4")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_AEB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 29)
    Jump("loc_AF4")

    label("loc_AEB")

    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_AF4")

    Return()

    # Function_0_682 end

    def Function_1_AF5(): pass

    label("Function_1_AF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B14")
    OP_B1("T2510_y")
    Jump("loc_B1D")

    label("loc_B14")

    OP_B1("T2510_n")

    label("loc_B1D")

    OP_A3(0x0)
    Jump("loc_B2C")

    label("loc_B23")

    OP_B1("T2510_n")

    label("loc_B2C")

    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC1")
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_B5B")
    OP_65(0x2, 0x1)
    OP_64(0x4, 0x1)

    label("loc_B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B7C")
    OP_63(0x1E)
    OP_62(0x1E, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B97")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 3)), scpexpr(EXPR_END)), "loc_B97")
    OP_65(0x3, 0x1)

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB7")
    OP_71(0x1004, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    Jump("loc_BC1")

    label("loc_BB7")

    OP_72(0x1004, 0x0)
    ExitThread()
    OP_65(0x1, 0x1)

    label("loc_BC1")

    Return()

    # Function_1_AF5 end

    def Function_2_BC2(): pass

    label("Function_2_BC2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D29")

    label("loc_BE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C00")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D29")

    label("loc_C00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C19")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D29")

    label("loc_C19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D29")

    label("loc_C32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D29")

    label("loc_C4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C64")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D29")

    label("loc_C64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D29")

    label("loc_C7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D29")

    label("loc_C96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D29")

    label("loc_CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D29")

    label("loc_CC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D29")

    label("loc_CE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFA")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D29")

    label("loc_CFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D13")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D29")

    label("loc_D13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D29")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D29")

    label("loc_D3E")

    Return()

    # Function_2_BC2 end

    def Function_3_D3F(): pass

    label("Function_3_D3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D62")
    OP_8D(0xFE, 42880, 32770, 40420, 30320, 2000)
    Jump("Function_3_D3F")

    label("loc_D62")

    Return()

    # Function_3_D3F end

    def Function_4_D63(): pass

    label("Function_4_D63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D86")
    OP_8D(0xFE, 4950, 5500, 2160, 1980, 2000)
    Jump("Function_4_D63")

    label("loc_D86")

    Return()

    # Function_4_D63 end

    def Function_5_D87(): pass

    label("Function_5_D87")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_D94")
    Jump("loc_FB1")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_FB1")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_DF6")

    ChrTalk(    #0
        0xFE,
        "练习应该是从明天开始呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "今天大概是让大家\x01",
            "提前热热身吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E45")

    label("loc_DF6")


    ChrTalk(    #2
        0xFE,
        (
            "我加入了\x01",
            "箭术社团。\x02",
        )
    )

    Jump("loc_E1C")

    label("loc_E1C")

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "因为以前曾经\x01",
            "稍微接触过一些。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_E45")

    Jump("loc_FB1")

    label("loc_E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_E94")

    ChrTalk(    #4
        0xFE,
        (
            "…………咦？\x01",
            "学生会长吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "不，没见过……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EE2")

    label("loc_E94")


    ChrTalk(    #6
        0xFE,
        "我是今天的值日生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "要把黑板\x01",
            "擦得干干净净才行呢。\x02",
        )
    )

    Jump("loc_EDE")

    label("loc_EDE")

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_EE2")

    Jump("loc_FB1")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_END)), "loc_FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F57")

    ChrTalk(    #8
        0xFE,
        (
            "罗伊斯同学\x01",
            "好像是共和国出身的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "作为专攻社会课程的学生\x01",
            "我对他也很有兴趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FAA")

    label("loc_F57")


    ChrTalk(    #10
        0xFE,
        (
            "罗伊斯同学\x01",
            "好像是共和国出身的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "他总是会跟我说\x01",
            "许多有趣的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_FAA")

    Jump("loc_FB1")

    label("loc_FAD")

    Call(0, 36)

    label("loc_FB1")

    TalkEnd(0xFE)
    Return()

    # Function_5_D87 end

    def Function_6_FB5(): pass

    label("Function_6_FB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_112E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1064")

    ChrTalk(    #12
        0xFE,
        (
            "我们的部长和雷克特学长\x01",
            "关系不太好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "因为听说他们是\x01",
            "去年争夺学生会长之位的竞争对手哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "……我倒是觉得利戈尔部长\x01",
            "更加适合那个职位啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112B")

    label("loc_1064")


    ChrTalk(    #15
        0x105,
        (
            "#042F……啊，罗伊斯同学。\x02\x03",

            "你有没有\x01",
            "见到雷克特学长？\x02",
        )
    )

    Jump("loc_10AD")

    label("loc_10AD")

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "雷克特学长……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "不，\x01",
            "在这附近没看见过啊……\x02",
        )
    )

    Jump("loc_10F2")

    label("loc_10F2")

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#047F是吗……\x02\x03",

            "#040F对不起，\x01",
            "耽误你时间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_112B")

    Jump("loc_1296")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1138")
    Jump("loc_1296")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1142")
    Jump("loc_1296")

    label("loc_1142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_114C")
    Jump("loc_1296")

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1296")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_END)), "loc_1292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(    #19
        0xFE,
        (
            "我也差不多\x01",
            "该去社团那边看看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "利戈尔部长\x01",
            "应该已经开始练习了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128F")

    label("loc_11B2")


    ChrTalk(    #21
        0xFE,
        (
            "啊啊，科洛丝同学。\x01",
            "是找其他社会系的同学吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "差不多该到\x01",
            "社团活动的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "我想大家应该\x01",
            "都到那边去了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#542F啊，好的……\x02\x03",

            "#543F谢谢你的忠告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "哪、哪里，\x01",
            "这也不算是什么忠告啦……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_128F")

    Jump("loc_1296")

    label("loc_1292")

    Call(0, 36)

    label("loc_1296")

    TalkEnd(0xFE)
    Return()

    # Function_6_FB5 end

    def Function_7_129A(): pass

    label("Function_7_129A")

    TalkBegin(0x20)
    ClearChrFlags(0x20, 0x10)
    TurnDirection(0x20, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CA")
    SetChrSubChip(0x20, 1)
    Jump("loc_12F0")

    label("loc_12CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x20, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12EB")
    SetChrSubChip(0x20, 2)
    Jump("loc_12F0")

    label("loc_12EB")

    SetChrSubChip(0x20, 0)

    label("loc_12F0")

    OP_8C(0x20, 180, 0)
    SetChrFlags(0x20, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 4)), scpexpr(EXPR_END)), "loc_13A5")

    ChrTalk(    #26
        0x20,
        (
            "#780F雷克特经常到这个房间来\x01",
            "躺在沙发上……\x02\x03",

            "呵呵，\x01",
            "仿佛在静静享受这学院的空气一样。\x02\x03",

            "他果然也是\x01",
            "很喜欢这所学院的吧。\x02",
        )
    )

    Jump("loc_13A1")

    label("loc_13A1")

    CloseMessageWindow()
    Jump("loc_173D")

    label("loc_13A5")


    ChrTalk(    #27
        0x20,
        (
            "#780F哦？\x01",
            "又在找雷克特吗？\x02",
        )
    )

    Jump("loc_13D1")

    label("loc_13D1")

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040F是、是的。\x02\x03",

            "#045F…………是这样的。\x02\x03",

            "明天要召开学生大会，\x01",
            "可他却又不知道逃到什么地方去了。\x02\x03",

            "必要的资料\x01",
            "完全没有准备好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x20,
        "#781F呵呵，那也够伤脑筋的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        (
            "#040F校长，那个……\x02\x03",

            "您好像十分\x01",
            "信赖雷克特学长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x20,
        (
            "#780F…………啊啊，是啊。\x02\x03",

            "#783F他是有自知之明的。\x02\x03",

            "自己在做什么，\x01",
            "会造成什么样的结果，\x01",
            "他自己都明白。\x02\x03",

            "#780F于是就在这个基础上\x01",
            "随心所欲的去做。\x02\x03",

            "而且也有应对的心理准备。\x02\x03",

            "#781F呵呵，虽然称不上『信赖』，\x01",
            "但我确实觉得他是个\x01",
            "相当有趣的学生会长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#047F……的确，\x01",
            "被抓住的时候还是会乖乖做事。\x02\x03",

            "平时虽然是一副吊儿郎当的样子，\x01",
            "但他实际上似乎确实\x01",
            "会用心考虑很多事情。\x02\x03",

            "#042F不过，既然如此……\x01",
            "一开始就不要逃，好好做完不就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x20,
        (
            "#780F呵呵，的确如此。\x02\x03",

            "下次你就这么跟他说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        (
            "#041F是，\x01",
            "我会劝告他的。\x02",
        )
    )

    Jump("loc_1739")

    label("loc_1739")

    CloseMessageWindow()
    OP_A2(0x2F74)

    label("loc_173D")

    Jump("loc_1DD6")

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_174A")
    Jump("loc_1DD6")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1845")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_183E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17B0")

    ChrTalk(    #35
        0x20,
        (
            "#780F卢安就在穿过林间小道之后\x01",
            "往南的方向。\x02\x03",

            "路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183B")

    label("loc_17B0")


    ChrTalk(    #36
        0x20,
        (
            "#780F一直关在学院里面\x01",
            "很无聊吧。\x02\x03",

            "难得外出一次，\x01",
            "就去好好散散心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#045F啊哈哈……\x01",
            "谢谢您。\x02",
        )
    )

    Jump("loc_1837")

    label("loc_1837")

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_183B")

    Jump("loc_1842")

    label("loc_183E")

    Call(0, 46)

    label("loc_1842")

    Jump("loc_1DD6")

    label("loc_1845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 3)), scpexpr(EXPR_END)), "loc_18C9")

    ChrTalk(    #38
        0x20,
        (
            "#780F要找雷克特的话，\x01",
            "刚才他还睡在那边的沙发上呢。\x02\x03",

            "不过在我看文件的时候\x01",
            "又不知道跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B70")

    label("loc_18C9")


    ChrTalk(    #39
        0x13B,
        (
            "#647F抱歉，校长。\x02\x03",

            "您有没有见过\x01",
            "我们的学生会长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        (
            "#045F因为有点事，所以……\x01",
            "但怎么也找不到他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x20,
        (
            "#783F啊啊，找雷克特吗。\x02\x03",

            "#780F刚才他还在那边的沙发上\x01",
            "睡觉来着……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x152, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x152,
        (
            "#733F在、在沙发上睡觉！？\x01",
            "而且还是在校长室！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        "#047F（雷克特学长…………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13B,
        (
            "#646F面对校长都如此肆无忌惮……\x02\x03",

            "看来只好靠我们的力量\x01",
            "做个了结了……！\x02\x03",

            "#645F校长，给您添麻烦了，\x01",
            "实在抱歉。\x02\x03",

            "稍后我一定\x01",
            "对那家伙严加惩治……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x20,
        (
            "#781F呵呵，不必介意。\x02\x03",

            "因为他好像\x01",
            "很喜欢这里呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        "#044F啊、啊…………？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F73)
    OP_65(0x3, 0x1)

    label("loc_1B70")

    Jump("loc_1DD6")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 2)), scpexpr(EXPR_END)), "loc_1C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BDF")

    ChrTalk(    #47
        0x20,
        (
            "#780F学生会在社团大楼的二层。\x02\x03",

            "有什么不明白的事\x01",
            "就去问他们好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C7B")

    label("loc_1BDF")


    ChrTalk(    #48
        0x20,
        (
            "#780F啊啊，\x01",
            "你还不熟悉学院的设施吧。\x02\x03",

            "有什么不明白的事\x01",
            "就去问学生会的人好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        (
            "#040F……好的。\x02\x03",

            "#543F校长，谢谢您。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1C7B")

    Jump("loc_1DD6")

    label("loc_1C7E")


    ChrTalk(    #50
        0x20,
        (
            "#780F哦，科洛丝。\x02\x03",

            "对校园生活已经习惯了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        (
            "#043F校长，那个……\x02\x03",

            "#047F您能允许我突然插班\x01",
            "真是太感谢了。\x02\x03",

            "#049F关于这次的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x20,
        (
            "#783F……科洛丝。\x02\x03",

            "你接受了正式的插班考试，\x01",
            "并且顺利取得了合格分数。\x02\x03",

            "#780F仅此而已。\x01",
            "不需要介意多余的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        "#542F啊……是、是的……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F72)

    label("loc_1DD6")

    SetChrSubChip(0x20, 0)
    TalkEnd(0x20)
    Return()

    # Function_7_129A end

    def Function_8_1DDF(): pass

    label("Function_8_1DDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E43")

    ChrTalk(    #54
        0xFE,
        (
            "我想在明天的课上\x01",
            "尝试使用新教材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "光是追着教科书跑\x01",
            "的确很无聊呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA1")

    label("loc_1E43")


    ChrTalk(    #56
        0xFE,
        (
            "我想在明天的课上\x01",
            "尝试使用新教材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "对了，\x01",
            "就用小说来做阅读练习好了。\x02",
        )
    )

    Jump("loc_1E9D")

    label("loc_1E9D")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1EA1")

    Jump("loc_219C")

    label("loc_1EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1EAE")
    Jump("loc_219C")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F0A")

    ChrTalk(    #58
        0xFE,
        (
            "米丽亚老师一直\x01",
            "对批改试卷都很热心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "咦，今天是怎么回事呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA5")

    label("loc_1F0A")


    ChrTalk(    #60
        0xFE,
        "这次的考试也顺利结束了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "对于一年级学生来说\x01",
            "是初次经历的定期考试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "不过多考几次\x01",
            "也就习惯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "就算考得不好也不用太担心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1FA5")

    Jump("loc_219C")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_20C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_201B")

    ChrTalk(    #64
        0xFE,
        (
            "雷克特同学时不时\x01",
            "就会找借口去戏弄米丽亚老师呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "米丽亚老师也差不多\x01",
            "该习惯了才好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C1")

    label("loc_201B")


    ChrTalk(    #66
        0xFE,
        "咦，要找雷克特同学？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "刚才还在那边的\x01",
            "米丽亚老师的座位上坐着呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "我记得当时\x01",
            "他好像在看什么书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "我正准备跟他说话，\x01",
            "他就呼啦一下不见了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_20C1")

    Jump("loc_219C")

    label("loc_20C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_219C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2134")

    ChrTalk(    #70
        0xFE,
        (
            "我被邀请担当\x01",
            "吹奏乐社团的顾问……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "但实际上我是音痴啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "这样也没问题吗？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_219C")

    label("loc_2134")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #73
        0xFE,
        "吹奏乐社团的顾问吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "嗯嗯，我是没问题……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "但是我可是完全不懂乐器的哦？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_219C")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21AF")
    OP_4A(0x21, 255)

    label("loc_21AF")

    Return()

    # Function_8_1DDF end

    def Function_9_21B0(): pass

    label("Function_9_21B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_22E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_226A")

    ChrTalk(    #76
        0xFE,
        (
            "明明是那副德性，\x01",
            "成绩居然还那么优秀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "啊啊，\x01",
            "真想出更难的试题让他伤透脑筋……！\x02",
        )
    )

    Jump("loc_2229")

    label("loc_2229")

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "但是这样其他的学生就……\x01",
            "………………（嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E0")

    label("loc_226A")


    ChrTalk(    #79
        0xFE,
        (
            "雷克特啊，\x01",
            "可是把其他候补全都淘汰掉\x01",
            "才当上学生会长的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "但我可不承认。\x01",
            "………………（嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_22E0")

    Jump("loc_2536")

    label("loc_22E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_22ED")
    Jump("loc_2536")

    label("loc_22ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_22F7")
    Jump("loc_2536")

    label("loc_22F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_246D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_236D")

    ChrTalk(    #81
        0xFE,
        (
            "仔细想想，\x01",
            "结果他还不是一样没上课。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0xFE,
        "…………那个笨蛋……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_246A")

    label("loc_236D")


    ChrTalk(    #83
        0xFE,
        (
            "雷克特那家伙，\x01",
            "今天好不容易来上课……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "但是态度实在太嚣张，\x01",
            "我就让他到走廊罚站去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "…………结果刚才一问\x01",
            "拉迪奥老师才知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "雷克特竟然直到刚才\x01",
            "还坐在我的位子上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0xFE,
        "…………那个笨蛋……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_246A")

    Jump("loc_2536")

    label("loc_246D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_24CE")

    ChrTalk(    #88
        0xFE,
        (
            "社会系的课程表\x01",
            "还没决定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "唉，反正这对碧欧拉来说\x01",
            "是常有的事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2536")

    label("loc_24CE")


    ChrTalk(    #90
        0xFE,
        "下个月的课程表已经定了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "我写在这里，\x01",
            "大家各自检查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "………………明白吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2536")

    TalkEnd(0xFE)
    Return()

    # Function_9_21B0 end

    def Function_10_253A(): pass

    label("Function_10_253A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_25D8")

    ChrTalk(    #93
        0xFE,
        (
            "雷克特同学演讲很有一手呢。\x01",
            "我都忍不住听入迷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "他只有在那个时候\x01",
            "说话才会一本正经啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "说不定意外地是块当政治家的料。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2672")

    label("loc_25D8")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #96
        0xFE,
        "讨厌～米丽亚真是的～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "那不是因为利戈尔同学\x01",
            "肚子痛请假而已吗～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "因为候选人只有那两个人，\x01",
            "所以那种结果也是理所当然的吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2672")

    Jump("loc_2837")

    label("loc_2675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_267F")
    Jump("loc_2837")

    label("loc_267F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2689")
    Jump("loc_2837")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_26E9")

    ChrTalk(    #99
        0xFE,
        (
            "这么说来，好像见过，\x01",
            "又好像没见过…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "唔，到底是怎么样呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2775")

    label("loc_26E9")


    ChrTalk(    #101
        0x105,
        (
            "#040F那个，不好意思，\x01",
            "碧欧拉老师……\x02\x03",

            "您有没有在这附近\x01",
            "见过雷克特学长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "咦？雷克特同学？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "唔～我觉得应该没见过……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2775")

    Jump("loc_2837")

    label("loc_2778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27D2")

    ChrTalk(    #104
        0xFE,
        "哎呀，少了一小时……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "呜呜～…………\x01",
            "我就是不擅长弄这个～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2837")

    label("loc_27D2")


    ChrTalk(    #106
        0xFE,
        (
            "为什么这个课程表\x01",
            "不能被认可呢～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "不是很完美吗～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x105,
        "#047F（看来似乎很忙……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2837")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_284A")
    OP_4A(0x18, 255)

    label("loc_284A")

    Return()

    # Function_10_253A end

    def Function_11_284B(): pass

    label("Function_11_284B")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2858")
    Jump("loc_2C45")

    label("loc_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_2862")
    Jump("loc_2C45")

    label("loc_2862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_297C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_28CD")
    OP_8C(0x2A, 180, 0)

    ChrTalk(    #109
        0x2A,
        (
            "那么，\x01",
            "请看一下这个小册子。\x02",
        )
    )

    Jump("loc_28A2")

    label("loc_28A2")

    CloseMessageWindow()

    ChrTalk(    #110
        0x2A,
        (
            "里面记载了\x01",
            "本学院的概要情况……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2979")

    label("loc_28CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2930")

    ChrTalk(    #111
        0x2A,
        (
            "来学院参观的人\x01",
            "还挺多的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x2A,
        (
            "每次学生会长\x01",
            "都会帮忙应付，\x01",
            "真是省了好多事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2979")

    label("loc_2930")


    ChrTalk(    #113
        0x2A,
        (
            "这给客人们\x01",
            "也留下了好印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x2A,
        (
            "来学院参观的人\x01",
            "还挺多的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2979")

    Jump("loc_2C45")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2A01")

    ChrTalk(    #115
        0x2A,
        (
            "其实刚才副会长同学\x01",
            "也问了我同样的问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x2A,
        (
            "然后就大失所望地\x01",
            "到二楼去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x2A,
        "好像一副很累的样子……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3B")

    label("loc_2A01")


    ChrTalk(    #118
        0x2A,
        "学生会长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x2A,
        (
            "不，\x01",
            "今天还没见过呢。\x02",
        )
    )

    Jump("loc_2A37")

    label("loc_2A37")

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2A3B")

    Jump("loc_2C45")

    label("loc_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2C45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 5)), scpexpr(EXPR_END)), "loc_2B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2ABC")

    ChrTalk(    #120
        0x2A,
        (
            "这一届的学生会长\x01",
            "好像是个很老练的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x2A,
        (
            "我当接待很长时间了，\x01",
            "那样的学生还是第一次见到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2ABC")


    ChrTalk(    #122
        0x2A,
        (
            "这么说来，\x01",
            "刚才我看到了\x01",
            "本届学生会长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x2A,
        (
            "呵呵，\x01",
            "他是个非常老练的人呢。\x02",
        )
    )

    Jump("loc_2B17")

    label("loc_2B17")

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2B1B")

    Jump("loc_2C45")

    label("loc_2B1E")


    ChrTalk(    #124
        0x2A,
        "哎呀，科洛丝同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x2A,
        "对学院已经习惯了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#044F啊……是、是的。\x02\x03",

            "#047F那个，\x01",
            "办插班手续的时候承蒙您多照顾了。\x02\x03",

            "#542F托您的福，\x01",
            "我才能够顺利开始校园生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x2A,
        "呵呵，太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x2A,
        (
            "有什么不明白的地方\x01",
            "就不要客气，尽管问哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#542F……好的。\x01",
            "谢谢您。\x02",
        )
    )

    Jump("loc_2C41")

    label("loc_2C41")

    CloseMessageWindow()
    OP_A2(0x2F75)

    label("loc_2C45")

    TalkEnd(0x2A)
    Return()

    # Function_11_284B end

    def Function_12_2C49(): pass

    label("Function_12_2C49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2C56")
    Jump("loc_2E15")

    label("loc_2C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_2C60")
    Jump("loc_2E15")

    label("loc_2C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2CB4")

    ChrTalk(    #130
        0xFE,
        (
            "考试成绩应该会\x01",
            "贴在这块公告板上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "呵呵，真是期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_2CB4")


    ChrTalk(    #132
        0xFE,
        (
            "哎呀，科洛丝同学。\x01",
            "考试感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        (
            "#044F嗯……\x02\x03",

            "#045F有点难呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "我这次相当有自信。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "呵呵，真期待成绩公布啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2D42")

    Jump("loc_2E15")

    label("loc_2D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2DA1")

    ChrTalk(    #136
        0xFE,
        (
            "我本来是想尽量\x01",
            "集中精力在学习上的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "可是这样就被说服了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E0B")

    label("loc_2DA1")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #138
        0xFE,
        (
            "不、不，\x01",
            "社团活动什么的还是……\x02",
        )
    )

    Jump("loc_2DDA")

    label("loc_2DDA")

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "我本来是想尽量\x01",
            "集中精力在学习上的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2E0B")

    Jump("loc_2E15")

    label("loc_2E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2E15")

    label("loc_2E15")

    TalkEnd(0xFE)
    Return()

    # Function_12_2C49 end

    def Function_13_2E19(): pass

    label("Function_13_2E19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2E97")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #140
        0xFE,
        (
            "因为是休假期间，\x01",
            "所以早上晚点起也不要紧吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "把午休时间错开……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "啦啦啦～……⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F07")

    label("loc_2E97")


    ChrTalk(    #143
        0xFE,
        (
            "我正在制作\x01",
            "长假时的活动表呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "虽然有点麻烦，\x01",
            "但实际做起来\x01",
            "还挺有趣的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "啦啦啦～……⊙\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2F07")

    Jump("loc_3121")

    label("loc_2F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_2F14")
    Jump("loc_3121")

    label("loc_2F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2F50")

    ChrTalk(    #146
        0xFE,
        (
            "唉，\x01",
            "我会当上部长都怪蕾娜……\x02",
        )
    )

    Jump("loc_2F4C")

    label("loc_2F4C")

    CloseMessageWindow()
    Jump("loc_2F93")

    label("loc_2F50")

    OP_8C(0xFE, 180, 0)

    ChrTalk(    #147
        0xFE,
        "嗯、嗯嗯。所以……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "在这里登记\x01",
            "就可以了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2F93")

    Jump("loc_3121")

    label("loc_2F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_2FA0")
    Jump("loc_3121")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3121")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 3)), scpexpr(EXPR_END)), "loc_3063")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2FEE")

    ChrTalk(    #149
        0xFE,
        "听说科洛丝同学很优秀啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "唉，真羡慕啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3060")

    label("loc_2FEE")


    ChrTalk(    #151
        0xFE,
        (
            "我记得你是叫科洛丝吧。\x01",
            "听说是位非常优秀的转学生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "我叫芙拉瑟·贝伦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "以后还请多多指教。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3060")

    Jump("loc_3121")

    label("loc_3063")


    ChrTalk(    #154
        0x105,
        (
            "#542F抱歉，打扰一下……\x02\x03",

            "你是社会系的学生吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "不是，\x01",
            "我是自然科学系的。\x02",
        )
    )

    Jump("loc_30C3")

    label("loc_30C3")

    CloseMessageWindow()

    ChrTalk(    #156
        0x105,
        (
            "#044F啊……\x02\x03",

            "（弄、弄错了……）\x02\x03",

            "#043F对、对不起。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0x2F7B)

    label("loc_3121")

    TalkEnd(0xFE)
    Return()

    # Function_13_2E19 end

    def Function_14_3125(): pass

    label("Function_14_3125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3180")

    ChrTalk(    #157
        0xFE,
        "长假差不多该开始了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "就趁这个机会\x01",
            "让芙拉瑟回家看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31FE")

    label("loc_3180")


    ChrTalk(    #159
        0xFE,
        (
            "看来她总算是\x01",
            "拿出干劲了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "不过，\x01",
            "考试成绩也全部出来了。\x02",
        )
    )

    Jump("loc_31D0")

    label("loc_31D0")

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "差不多\x01",
            "该做回国的准备了。\x02",
        )
    )

    Jump("loc_31FA")

    label("loc_31FA")

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_31FE")

    Jump("loc_33B9")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_320B")
    Jump("loc_33B9")

    label("loc_320B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_32B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_326E")

    ChrTalk(    #162
        0xFE,
        "这是芙拉瑟的第一件工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "呵呵，\x01",
            "和往常一样静静的守望吧。\x02",
        )
    )

    Jump("loc_326A")

    label("loc_326A")

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_326E")


    ChrTalk(    #164
        0xFE,
        (
            "部长的工作\x01",
            "这么快就来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "呵呵，跟我预想的一样。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_32B2")

    Jump("loc_33B9")

    label("loc_32B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_32BF")
    Jump("loc_33B9")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_33B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3321")

    ChrTalk(    #166
        0xFE,
        (
            "芙拉瑟好像\x01",
            "没有当部长的意愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "呵呵，\x01",
            "看来需要用点策略呢。\x02",
        )
    )

    Jump("loc_331D")

    label("loc_331D")

    CloseMessageWindow()
    Jump("loc_33B9")

    label("loc_3321")


    ChrTalk(    #168
        0xFE,
        (
            "要尽快决定谁来当\x01",
            "新的部长才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "当然我肯定是\x01",
            "要推荐芙拉瑟的，\x01",
            "但是她本人好像没有这个意愿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "呵呵，\x01",
            "看来需要用点策略呢。\x02",
        )
    )

    Jump("loc_33B5")

    label("loc_33B5")

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_33B9")

    TalkEnd(0xFE)
    Return()

    # Function_14_3125 end

    def Function_15_33BD(): pass

    label("Function_15_33BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_33CA")
    Jump("loc_3A09")

    label("loc_33CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_33D4")
    Jump("loc_3A09")

    label("loc_33D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_349E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3431")

    ChrTalk(    #171
        0xFE,
        (
            "我有一些问题\x01",
            "要请教米丽亚老师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "还是在这里稍微\x01",
            "等一会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349B")

    label("loc_3431")


    ChrTalk(    #173
        0xFE,
        "哎呀，科洛丝同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "其实我正打算\x01",
            "请教米丽亚老师一些问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "不过她现在好像不在呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_349B")

    Jump("loc_3A09")

    label("loc_349E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_391E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 5)), scpexpr(EXPR_END)), "loc_3605")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3514")

    ChrTalk(    #176
        0xFE,
        (
            "说到雷克特学长，\x01",
            "我的脑子里就只有\x01",
            "『学生会的怪人』这点印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "他到底是什么人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3602")

    label("loc_3514")


    ChrTalk(    #178
        0xFE,
        (
            "说到雷克特学长，\x01",
            "我的脑子里就只有\x01",
            "『学生会的怪人』这点印象呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "他会是比雷欧学长\x01",
            "更厉害的实力派吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x13B,
        (
            "#645F不，\x01",
            "现在还不知道……\x02",
        )
    )

    Jump("loc_35AE")

    label("loc_35AE")

    CloseMessageWindow()

    ChrTalk(    #181
        0x152,
        (
            "#734F那个，\x01",
            "该说是学院七大不可思议之一吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_A2(0xE)

    label("loc_3602")

    Jump("loc_391B")

    label("loc_3605")


    ChrTalk(    #182
        0x13B,
        (
            "#640F不好意思，请问……\x02\x03",

            "有没有在这附近见过\x01",
            "我们的学生会长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "咦？　雷欧学长吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "下课之后他好像\x01",
            "就去学生会室了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x105,
        (
            "#045F不、不是……\x02\x03",

            "我们要找的是\x01",
            "雷克特学长……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #186
        0x152,
        (
            "#732F那、那个……\x02\x03",

            "现在的学生会长\x01",
            "是雷克特学长哦。\x02\x03",

            "#734F好像经常被弄错……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "咦，是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "真、真是不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "我一直以为\x01",
            "雷欧学长才是学生会长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x152,
        (
            "#735F（又有人误会了吗……）\x02\x03",

            "（之前明明还很努力\x01",
            "  到处说明了一遍呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x13B,
        (
            "#645F（唉，会搞错也不奇怪。）\x02\x03",

            "（实质上掌管事务的\x01",
            "  也确实是雷欧学长嘛……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x105,
        "#047F（果然…………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "嗯，说到雷克特学长，\x01",
            "就是那个有点奇怪的人……对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "平时就不太经常见到他……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "嗯嗯，\x01",
            "今天应该也没见过哦。\x02",
        )
    )

    Jump("loc_38DD")

    label("loc_38DD")

    CloseMessageWindow()

    ChrTalk(    #196
        0x13B,
        "#645F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x152,
        "#734F不好意思，打扰你了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F7D)

    label("loc_391B")

    Jump("loc_3A09")

    label("loc_391E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3983")

    ChrTalk(    #198
        0xFE,
        (
            "雷欧学长直截了当的分析\x01",
            "总是一针见血。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "听了他的话\x01",
            "真让人感到无比佩服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A09")

    label("loc_3983")


    ChrTalk(    #200
        0xFE,
        (
            "雷欧学长的分析\x01",
            "到底是分量不同啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "只靠这点数据\x01",
            "就能看穿材料的特性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "……理论证明也非常完美。\x01",
            "呼，真是佩服啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_3A09")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1C")
    OP_4A(0xFE, 255)

    label("loc_3A1C")

    Return()

    # Function_15_33BD end

    def Function_16_3A1D(): pass

    label("Function_16_3A1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3A2A")
    Jump("loc_3B9D")

    label("loc_3A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3A34")
    Jump("loc_3B9D")

    label("loc_3A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3A3E")
    Jump("loc_3B9D")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3A6D")

    ChrTalk(    #203
        0xFE,
        "一定很好玩的！　对吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB0")

    label("loc_3A6D")


    ChrTalk(    #204
        0xFE,
        "没问题啦～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "加入了社团\x01",
            "又不一定会让\x01",
            "成绩变差～。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3AB0")

    Jump("loc_3B9D")

    label("loc_3AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3B02")

    ChrTalk(    #206
        0xFE,
        "好～吹奏乐社团东山再起☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "嘿嘿，看我大显身手～⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B9D")

    label("loc_3B02")


    ChrTalk(    #208
        0xFE,
        "啊，科洛丝同学～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "我啊，\x01",
            "早就想加入吹奏乐社团了。\x02",
        )
    )

    Jump("loc_3B4B")

    label("loc_3B4B")

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "可是从去年开始\x01",
            "成员数就是零了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "所以我现在\x01",
            "正在跟老师商量呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3B9D")

    TalkEnd(0xFE)
    Return()

    # Function_16_3A1D end

    def Function_17_3BA1(): pass

    label("Function_17_3BA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3BAE")
    Jump("loc_3CAF")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3BB8")
    Jump("loc_3CAF")

    label("loc_3BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_3C16")

    ChrTalk(    #212
        0xFE,
        "考试也总算通过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "在被汉斯抢先之前，\x01",
            "至少要表白我的心意……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C9B")

    label("loc_3C16")

    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #214
        0xFE,
        (
            "……不、不准看！\x01",
            "我正在写信呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "你问是给谁的？\x01",
            "当然是给露西学姐的啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_3C9B")

    Jump("loc_3CAF")

    label("loc_3C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3CA8")
    Jump("loc_3CAF")

    label("loc_3CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3CAF")

    label("loc_3CAF")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CC2")
    OP_4A(0xFE, 255)

    label("loc_3CC2")

    Return()

    # Function_17_3BA1 end

    def Function_18_3CC3(): pass

    label("Function_18_3CC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3CD0")
    Jump("loc_3DEF")

    label("loc_3CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3CDA")
    Jump("loc_3DEF")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_3D33")

    ChrTalk(    #216
        0x1E,
        (
            "#1779F……来参观本学院吗？\x02\x03",

            "哈哈，十分荣幸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDB")

    label("loc_3D33")


    ChrTalk(    #217
        0x1E,
        (
            "#1775F我是担任\x01",
            "学生会长的雷克特。\x01",
            "请多指教。\x02\x03",

            "#1779F……来参观本学院吗？\x02\x03",

            "哈哈，十分荣幸。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x105,
        "#045F（……完全变了个样啊…………）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_3DDB")

    Jump("loc_3DEF")

    label("loc_3DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3DE8")
    Jump("loc_3DEF")

    label("loc_3DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3DEF")

    label("loc_3DEF")

    TalkEnd(0xFE)
    Return()

    # Function_18_3CC3 end

    def Function_19_3DF3(): pass

    label("Function_19_3DF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_3E00")
    Jump("loc_3F4A")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_3E0A")
    Jump("loc_3F4A")

    label("loc_3E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_3F39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_3E67")

    ChrTalk(    #219
        0xFE,
        "唔唔，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "哎呀，\x01",
            "我想让我儿子进这个学院……\x02",
        )
    )

    Jump("loc_3E63")

    label("loc_3E63")

    CloseMessageWindow()
    Jump("loc_3F36")

    label("loc_3E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_3EB6")

    ChrTalk(    #221
        0xFE,
        (
            "不愧是王立学院的\x01",
            "学生会长啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "哎呀呀，真是位出色的人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F36")

    label("loc_3EB6")


    ChrTalk(    #223
        0xFE,
        (
            "哦，这位就是\x01",
            "杰尼丝王立学院的学生会长吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "唔，\x01",
            "真是位相当出色的人嘛。\x02",
        )
    )

    Jump("loc_3F11")

    label("loc_3F11")

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        "#045F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_3F36")

    Jump("loc_3F4A")

    label("loc_3F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_3F43")
    Jump("loc_3F4A")

    label("loc_3F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3F4A")

    label("loc_3F4A")

    TalkEnd(0xFE)
    Return()

    # Function_19_3DF3 end

    def Function_20_3F4E(): pass

    label("Function_20_3F4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_4186")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_3F98")

    ChrTalk(    #226
        0x27,
        (
            "#1795F唉…………\x02\x03",

            "雷克特那笨蛋……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4186")

    label("loc_3F98")

    EventBegin(0x1)
    Fade(1000)
    OP_6D(42200, 0, 38800, 0)
    SetChrPos(0x105, 41600, 0, 38200, 0)
    SetChrPos(0x152, 42180, 0, 37500, 0)
    SetChrPos(0x13B, 41140, 0, 37100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #227
        0x27,
        (
            "#1793F这次我都用手铐绑住他了。\x02\x03",

            "但结果却还是\x01",
            "被他逃走了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #228
        0x105,
        "#043F那、那个，露西学姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x27,
        (
            "#1793F雷克特那家伙啊，\x01",
            "拥有瞬间移动的特技哦。\x02\x03",

            "所以凭我的力量\x01",
            "已经不可能抓到他了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x152,
        (
            "#737F（……露、露西学姐！\x01",
            "  振作点啊！！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x13B,
        (
            "#645F（连学姐\x01",
            "  也已经这么疲惫了吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x13)
    EventEnd(0x4)

    label("loc_4186")

    TalkEnd(0xFE)
    Return()

    # Function_20_3F4E end

    def Function_21_418A(): pass

    label("Function_21_418A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_41E9")

    ChrTalk(    #232
        0xFE,
        "这样就是三胜两败吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "嗯，看来能和她\x01",
            "成为不错的竞争对手呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4263")

    label("loc_41E9")


    ChrTalk(    #234
        0xFE,
        (
            "唔，\x01",
            "败给露西同学了吗。\x02",
        )
    )

    Jump("loc_420D")

    label("loc_420D")

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "我也尝试过\x01",
            "各种各样的学习方法……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "她到底是用什么方法\x01",
            "复习考试的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_4263")

    TalkEnd(0xFE)
    Return()

    # Function_21_418A end

    def Function_22_4267(): pass

    label("Function_22_4267")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_4361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_42D0")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #237
        0x26,
        (
            "……败给雷欧·洛连兹\x01",
            "实在是没办法。\x02\x03",

            "但是真不想\x01",
            "败给雷克特那家伙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435E")

    label("loc_42D0")


    ChrTalk(    #238
        0x26,
        "啊啊，是科洛丝吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x26,
        (
            "跟昨天说的一样，\x01",
            "社团活动从明天开始继续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x26,
        (
            "今天就好好休息，\x01",
            "调整一下状态吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        "#040F啊，好的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_435E")

    Jump("loc_44BD")

    label("loc_4361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_44BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_43AA")

    ChrTalk(    #242
        0x26,
        "无论多少次我都要说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x26,
        "别跟那种人扯上关系！\x02",
    )

    CloseMessageWindow()
    Jump("loc_44BD")

    label("loc_43AA")


    ChrTalk(    #244
        0x13B,
        "#640F那、那个，对不起。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x26,
        "嗯…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x13B,
        (
            "#640F你有没有在这附近\x01",
            "见过学生会长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x26,
        (
            "学生会长…………\x01",
            "……是说雷克特吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x26,
        "呼……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x26,
        (
            "你们啊，\x01",
            "可别和那种人扯上关系哦。\x02",
        )
    )

    Jump("loc_4482")

    label("loc_4482")

    CloseMessageWindow()

    ChrTalk(    #250
        0x26,
        "我能说的就是这些了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x105,
        "#045F啊，是…………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_44BD")

    TalkEnd(0xFE)
    Return()

    # Function_22_4267 end

    def Function_23_44C1(): pass

    label("Function_23_44C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_4592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_4516")

    ChrTalk(    #252
        0xFE,
        (
            "肩上坐着的那只隼\x01",
            "好像很不错啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "简直就像一幅画……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4592")

    label("loc_4516")


    ChrTalk(    #254
        0xFE,
        (
            "………之前有一次\x01",
            "学生会长强行让我\x01",
            "给他画了一幅画呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "结果那张画\x01",
            "在比赛中拿了优胜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "…………为什么？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_4592")

    TalkEnd(0xFE)
    Return()

    # Function_23_44C1 end

    def Function_24_4596(): pass

    label("Function_24_4596")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_46A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_4620")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #257
        0x15,
        (
            "#640F嗯嗯，\x01",
            "麻烦你在这个文件里\x01",
            "写上这期社团的预算。\x02\x03",

            "#643F嗯，\x01",
            "在这栏写上活动内容……\x02",
        )
    )

    Jump("loc_461C")

    label("loc_461C")

    CloseMessageWindow()
    Jump("loc_46A0")

    label("loc_4620")


    ChrTalk(    #258
        0x15,
        (
            "#640F啊，科洛丝～。\x02\x03",

            "现在我正在\x01",
            "走访各个社团的部长呢。\x02\x03",

            "#648F这可比寻找那个学生会长\x01",
            "要有趣得多呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_46A0")

    TalkEnd(0xFE)
    Return()

    # Function_24_4596 end

    def Function_25_46A4(): pass

    label("Function_25_46A4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_21()
    OP_C4(0x0, 0x800)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #259
        "\x18\x07\x0C那个时候，我发誓不依赖任何人。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #260
        (
            "\x18\x07\x0C讨厌被束缚的生活。\x01",
            "讨厌随波逐流的生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #261
        "\x18\x07\x0C……我要用自己的脚走下去。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #262
        "\x18\x07\x0C隐藏在心中的，默默的决心。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #263
        (
            "\x18\x07\x0C其实心中也有所察觉，\x01",
            "那只不过是单纯的借口―――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x12, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x15, 21)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x10, 15)
    SetChrChipByIndex(0x11, 20)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 19)
    SetChrChipByIndex(0x16, 17)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x105, 4960, 250, 30360, 270)
    SetChrPos(0x14, 500, 200, 30000, 90)
    SetChrPos(0x11, 500, 200, 32000, 90)
    SetChrPos(0x16, -2750, 100, 34100, 90)
    SetChrPos(0x12, -2750, 200, 30000, 90)
    SetChrPos(0x15, -2750, 200, 32000, 90)
    SetChrPos(0x10, 500, 200, 34100, 90)
    SetChrPos(0x17, -5900, 100, 32000, 90)
    SetChrPos(0x13, -5900, 100, 34100, 90)
    SetChrPos(0x18, 5300, 250, 32119, 270)
    OP_6D(4200, 0, 32500, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    SoundLoad(233)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #264
        "\x07\x05＜社会系教室·一年级共同授课＞\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1E()
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #265
        0x18,
        (
            "#11P好了好了，大家。\x01",
            "都看这边～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x18,
        (
            "#11P这位是插班生\x01",
            "科洛丝·琳希同学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x18,
        (
            "#11P选的课程是……唔……是社会系。\x01",
            "嗯，是我这班的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x105, 400)
    Sleep(300)

    ChrTalk(    #268
        0x18,
        (
            "#5P那么科洛丝同学，\x01",
            "请跟大家打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x18, 400)
    Sleep(300)

    ChrTalk(    #269
        0x105,
        "#047F#12P……是。\x02",
    )

    CloseMessageWindow()

    def lambda_4ACD():
        OP_6D(1700, 0, 33000, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_4ACD)

    def lambda_4AE5():
        OP_67(0, 4600, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_4AE5)

    def lambda_4AFD():
        OP_6B(3300, 1500)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_4AFD)
    OP_8C(0x105, 270, 400)

    def lambda_4B14():
        OP_8E(0xFE, 0x116C, 0xFA, 0x7698, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4B14)
    Sleep(300)
    OP_8C(0x18, 270, 500)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(500)

    ChrTalk(    #270
        0x105,
        (
            "#042F#2P我是插班到一年级的\x01",
            "科洛丝·琳希。\x02\x03",

            "在这所出色的学院学习、生活\x01",
            "是我长久以来一直期待的事情。\x02\x03",

            "今天能够成为集体中的一员\x01",
            "我感到非常荣幸。\x02\x03",

            "#543F我还十分不成熟，\x01",
            "可能会给各位\x01",
            "添很多麻烦……\x02\x03",

            "#542F但是我会尽最大努力的。\x01",
            "请大家多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x18, 0x3, 0x0, 0x1C)
    OP_22(0xE9, 0x0, 0x64)
    Sleep(2000)
    OP_44(0x18, 0x3)
    Sleep(2000)

    NpcTalk(    #271
        0x15,
        "戴眼镜的女学生",
        (
            "#647F（唔，突然来的插班生啊……）\x02\x03",

            "#649F（是什么地方的名门闺秀吧？\x01",
            "  有一种不好接近的感觉……）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #272
        0x12,
        "梳分头的男学生",
        (
            "#730F#6P（五月份才插班进来呢。\x01",
            "  感觉好像有什么内情似的。）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #273
        0x14,
        "弗雷",
        "#6P啊，能不能问个问题～？\x02",
    )

    Jump("loc_4D83")

    label("loc_4D83")

    CloseMessageWindow()

    NpcTalk(    #274
        0x14,
        "弗雷",
        (
            "#6P科洛丝同学是哪里出身？\x01",
            "是利贝尔人吗？\x02",
        )
    )

    Jump("loc_4DC3")

    label("loc_4DC3")

    CloseMessageWindow()

    ChrTalk(    #275
        0x105,
        (
            "#044F嗯……\x02\x03",

            "#542F是的。\x01",
            "格兰赛尔……地区出身的。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #276
        0x11,
        "塞尔玛",
        "你有什么兴趣爱好呢？\x02",
    )

    Jump("loc_4E39")

    label("loc_4E39")

    CloseMessageWindow()

    ChrTalk(    #277
        0x105,
        "#045F啊……没什么特别的。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #278
        0x14,
        "弗雷",
        "#6P咦，真的吗～？\x02",
    )

    Jump("loc_4E88")

    label("loc_4E88")

    CloseMessageWindow()

    NpcTalk(    #279
        0x14,
        "弗雷",
        "#6P真无聊啊。\x02",
    )

    Jump("loc_4EAD")

    label("loc_4EAD")

    CloseMessageWindow()

    ChrTalk(    #280
        0x105,
        (
            "#043F嗯……\x02\x03",

            "……但我确实……\x01",
            "没什么……兴趣爱好……\x02\x03",

            "#049F（……勉强要说的话……\x01",
            "  算是做点心吧……）\x02\x03",

            "（不过这也是不值得\x01",
            "  在别人面前提起的事情……）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #281
        0x16,
        "罗迪",
        (
            "#5P插班考试\x01",
            "好像非常难吧？\x02",
        )
    )

    Jump("loc_4F98")

    label("loc_4F98")

    CloseMessageWindow()

    NpcTalk(    #282
        0x16,
        "罗迪",
        "#5P你竟然考过了啊。\x02",
    )

    Jump("loc_4FC3")

    label("loc_4FC3")

    CloseMessageWindow()

    NpcTalk(    #283
        0x17,
        "米克",
        "#2P咦，比入学考试还难吗？\x02",
    )

    Jump("loc_4FF4")

    label("loc_4FF4")

    CloseMessageWindow()

    NpcTalk(    #284
        0x17,
        "米克",
        "#2P哇，不可能～！\x02",
    )

    Jump("loc_501D")

    label("loc_501D")

    CloseMessageWindow()

    NpcTalk(    #285
        0x10,
        "罗基克",
        "#5P嗯嗯，很优秀嘛……\x02",
    )

    Jump("loc_504F")

    label("loc_504F")

    CloseMessageWindow()
    OP_59()
    OP_22(0xAE, 0x0, 0x64)
    OP_43(0x18, 0x3, 0x0, 0x1C)
    Sleep(2000)
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #286
        0x105,
        "#043F那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x18,
        "#11P好了好了，大家！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x18,
        (
            "#11P提问就留到\x01",
            "下课再说～！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x18, 0x0, 0x0, 0x1B)
    OP_44(0x18, 0x3)
    TurnDirection(0x18, 0x105, 400)
    Sleep(300)

    ChrTalk(    #289
        0x18,
        (
            "#5P科洛丝同学，\x01",
            "你随便找个座位坐吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x18, 400)
    Sleep(300)

    ChrTalk(    #290
        0x105,
        "#044F#12P……啊，是。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 225, 400)
    Sleep(300)

    def lambda_5163():

        label("loc_5163")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_5163")

    QueueWorkItem2(0x18, 2, lambda_5163)
    OP_43(0x105, 0x0, 0x0, 0x1A)
    Sleep(3000)
    OP_44(0x18, 0x2)
    OP_8C(0x18, 270, 400)
    Sleep(300)

    ChrTalk(    #291
        0x18,
        "#11P那么就开始上课了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x18,
        "#11P打开教科书第２３页……\x02",
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x105, 0x0)
    Sleep(500)
    Fade(300)
    SetChrSubChip(0x15, 2)
    Sleep(500)

    NpcTalk(    #293
        0x15,
        "戴眼镜的女学生",
        (
            "#647F#5P（唔…………\x01",
            "　『神秘的插班生』……）\x02\x03",

            "#640F（真令人在意……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_525D():
        OP_6B(3200, 4000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_525D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x2D, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 123, 0, 0)
    IdleLoop()
    Return()

    # Function_25_46A4 end

    def Function_26_5288(): pass

    label("Function_26_5288")


    def lambda_528E():
        OP_8E(0xFE, 0x94C, 0x0, 0x6FCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_528E)
    WaitChrThread(0x105, 0x1)

    def lambda_52AE():
        OP_8E(0xFE, 0xFFFFE764, 0x0, 0x6FCC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52AE)
    WaitChrThread(0x105, 0x1)

    def lambda_52CE():
        OP_8E(0xFE, 0xFFFFE764, 0x0, 0x7210, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_52CE)
    WaitChrThread(0x105, 0x1)
    Fade(500)
    SetChrPos(0x105, -5900, 100, 30000, 90)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 23)
    Return()

    # Function_26_5288 end

    def Function_27_5309(): pass

    label("Function_27_5309")

    OP_24(0xAE, 0x5A)
    Sleep(200)
    OP_24(0xAE, 0x50)
    Sleep(200)
    OP_24(0xAE, 0x46)
    Sleep(200)
    OP_24(0xAE, 0x3C)
    Sleep(200)
    OP_24(0xAE, 0x32)
    Sleep(200)
    OP_24(0xAE, 0x28)
    Sleep(200)
    OP_24(0xAE, 0x1E)
    Sleep(200)
    OP_24(0xAE, 0x14)
    Sleep(200)
    OP_24(0xAE, 0xA)
    Sleep(200)
    OP_24(0xAE, 0x0)
    Return()

    # Function_27_5309 end

    def Function_28_535F(): pass

    label("Function_28_535F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53FD")
    OP_62(0x14, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x16, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x11, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    Jump("Function_28_535F")

    label("loc_53FD")

    Return()

    # Function_28_535F end

    def Function_29_53FE(): pass

    label("Function_29_53FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_4A(0x10, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1C, 255)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #294
        "\x07\x00之后过了两周……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #295
        (
            "\x07\x00学生之间开始流传\x01",
            "『神秘的插班生』的传闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #296
        (
            "\x07\x00关于头脑非常聪明，礼仪端正，\x01",
            "但是却相当刻板的一年级学生的话题。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #297
        (
            "\x07\x00本以为经过一段时间后，\x01",
            "她的紧张也会缓解一些……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_6D(37080, 0, 31600, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrPos(0x105, 2160, 0, 34220, 270)
    SetChrPos(0x19, 32800, 0, 33500, 180)
    SetChrPos(0x10, 32800, 0, 33500, 180)
    SetChrPos(0x1D, 32800, 0, 33500, 180)
    SetChrPos(0x1C, 32800, 0, 33500, 180)
    SetChrPos(0x1A, 43000, 0, 30600, 0)
    OP_A3(0x3)

    def lambda_561A():
        OP_6B(3400, 6000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_561A)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0xF)
    OP_73(0xF)

    def lambda_5644():
        OP_8E(0xFE, 0x8020, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5644)
    WaitChrThread(0x19, 0x1)

    def lambda_5664():
        OP_8E(0xFE, 0x8688, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_5664)
    WaitChrThread(0x19, 0x1)

    ChrTalk(    #298 op#A op#5
        0x19,
        "#25A#5P唉～终于结束了啊……\x05\x02",
    )

    CloseMessageWindow()
    OP_43(0x19, 0x3, 0x0, 0x1F)

    def lambda_56B4():
        OP_8E(0xFE, 0x8020, 0x0, 0x72D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56B4)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #299 op#A op#5
        0x10,
        (
            "#30A#5P嗯，\x01",
            "今天也是很有意义的一天啊。\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x21)

    def lambda_570F():
        OP_8E(0xFE, 0x8020, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_570F)
    WaitChrThread(0x1D, 0x1)
    OP_8C(0x1D, 0, 400)

    ChrTalk(    #300 op#A op#5
        0x1D,
        "#30A#12P莫妮卡～练习要开始了哦～！\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301 op#A op#5
        0x1C,
        "#2P#17A啊，是～！\x05\x02",
    )

    CloseMessageWindow()
    OP_4A(0x18, 255)
    OP_43(0x18, 0x0, 0x0, 0x1E)
    Sleep(500)

    def lambda_5795():
        OP_8E(0xFE, 0x8020, 0x0, 0x7A44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5795)
    WaitChrThread(0x1C, 0x1)
    Sleep(300)

    def lambda_57BA():

        label("loc_57BA")

        TurnDirection(0xFE, 0x1D, 400)
        OP_48()
        Jump("loc_57BA")

    QueueWorkItem2(0x1C, 2, lambda_57BA)
    OP_43(0x1D, 0x3, 0x0, 0x23)
    Sleep(100)
    OP_44(0x1C, 0x2)
    OP_43(0x1C, 0x3, 0x0, 0x22)
    OP_A2(0x3)
    WaitChrThread(0x18, 0x0)
    Fade(1000)
    OP_6D(-3060, 0, 32780, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    SetChrPos(0x18, 2880, 0, 26500, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7140, 0, 34280, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -7140, 0, 33020, 0)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_43(0x105, 0x2, 0x0, 0x2)

    def lambda_5881():
        OP_6D(4059, 0, 32780, 4000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_5881)
    WaitChrThread(0x2D, 0x0)

    def lambda_589E():
        OP_8E(0xFE, 0xB40, 0x0, 0x71E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_589E)

    def lambda_58B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_58B9)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 270, 400)
    Sleep(800)
    OP_8C(0x18, 315, 400)
    Sleep(800)
    OP_8C(0x18, 270, 400)
    Sleep(300)

    ChrTalk(    #302
        0x18,
        (
            "#11P哎呀呀，\x01",
            "大家都已经回去了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x18,
        (
            "#11P本来还想\x01",
            "把这资料发下去的……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x105, 0x2)
    SetChrSubChip(0x105, 0)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x105, 180, 400)

    ChrTalk(    #304
        0x105,
        (
            "#044F啊…………\x02\x03",

            "（老师有什么麻烦吗。）\x02\x03",

            "#047F（……………………好！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59EA():
        OP_6D(4370, 0, 31610, 2000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_59EA)

    def lambda_5A02():
        OP_6B(3580, 2000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_5A02)

    def lambda_5A12():
        OP_8E(0xFE, 0xB40, 0x0, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A12)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(300)

    ChrTalk(    #305
        0x105,
        (
            "#042F#5P那、那个……碧欧拉老师，\x01",
            "请问有什么麻烦事吗。\x02\x03",

            "不介意的话，\x01",
            "我可以帮忙……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x105, 400)

    ChrTalk(    #306
        0x18,
        "#12P嗯……但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x18,
        "#12P是、是吗…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x18,
        "#12P那么，就拜托你吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #309
        0x105,
        "#542F#5P好、好的。\x02",
    )

    CloseMessageWindow()

    def lambda_5B3D():
        OP_8E(0xFE, 0xB40, 0x0, 0x7404, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5B3D)
    WaitChrThread(0x18, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #310
        "\x07\x05科洛丝得到老师给的资料。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #311
        0x18,
        (
            "#12P不好意思，能不能帮忙把\x01",
            "这些资料发给社会系的同学呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x18,
        (
            "#12P这资料挺重要的，\x01",
            "可别漏发哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x105,
        "#042F#5P好的，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x18,
        "#12P啊，我得赶快走了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x18,
        "#12P职员会议要开始了～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x18, 180, 600)

    def lambda_5C97():
        OP_8E(0xFE, 0xB40, 0x0, 0x6784, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5C97)
    Sleep(300)

    def lambda_5CB7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_5CB7)
    WaitChrThread(0x18, 0x1)
    OP_63(0x18)
    Sleep(500)
    SetChrFlags(0x18, 0x80)
    Sleep(500)

    ChrTalk(    #316
        0x105,
        "#047F#5P……………………嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Sleep(300)

    def lambda_5D17():
        OP_6D(3300, 0, 35650, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_5D17)

    def lambda_5D2F():
        OP_8E(0xFE, 0x8D4, 0x0, 0x85CA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D2F)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x2D, 0x0)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #317
        0x105,
        (
            "#044F#12P这个资料，\x01",
            "是社会系课程的全年学分表……？\x02\x03",

            "#042F这可得仔细分发才行……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #318
        0x105,
        (
            "#047F#11P（总之，\x01",
            "　先去发给留在教室里的人……）\x02\x03",

            "（然后是去社团活动的人，\x01",
            "　还有回宿舍的人。）\x02\x03",

            "#042F…………好！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F65)
    OP_59()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2880, 0, 31000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x2C, 1300, 180, 34060, 0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x800)
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x2BC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x1B, 0x10)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_29_53FE end

    def Function_30_5F61(): pass

    label("Function_30_5F61")

    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    SetChrPos(0x18, 47100, 0, 35300, 180)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5F94():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5F94)
    WaitChrThread(0x18, 0x1)

    def lambda_5FB4():
        OP_8E(0xFE, 0x9E34, 0x0, 0x9664, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5FB4)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5FE6():
        OP_8E(0xFE, 0x9D6C, 0x0, 0x8EF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5FE6)
    WaitChrThread(0x18, 0x1)

    def lambda_6006():
        OP_8E(0xFE, 0x9C40, 0x0, 0x81B0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6006)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6038():
        OP_8E(0xFE, 0x92E0, 0x0, 0x7918, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6038)
    WaitChrThread(0x18, 0x1)

    def lambda_6058():
        OP_8E(0xFE, 0x8020, 0x0, 0x7918, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6058)
    WaitChrThread(0x18, 0x1)

    def lambda_6078():
        OP_8E(0xFE, 0x8020, 0x0, 0x82DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_6078)
    WaitChrThread(0x18, 0x1)
    Return()

    # Function_30_5F61 end

    def Function_31_6093(): pass

    label("Function_31_6093")


    def lambda_6099():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x7788, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6099)
    Sleep(500)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_60D0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_60D0)
    WaitChrThread(0x19, 0x1)
    Sleep(1000)
    OP_62(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A6(0x3)
    OP_63(0x19)
    Sleep(500)

    def lambda_6105():

        label("loc_6105")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_6105")

    QueueWorkItem2(0x1A, 2, lambda_6105)

    def lambda_6116():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6116)
    Sleep(500)
    OP_44(0x1A, 0x2)
    OP_43(0x1A, 0x3, 0x0, 0x20)
    WaitChrThread(0x19, 0x1)

    def lambda_6146():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6146)
    WaitChrThread(0x19, 0x1)

    def lambda_6166():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6166)
    WaitChrThread(0x19, 0x1)

    def lambda_6186():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6186)
    WaitChrThread(0x19, 0x1)
    Return()

    # Function_31_6093 end

    def Function_32_61A1(): pass

    label("Function_32_61A1")


    def lambda_61A7():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x7E2B, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_61A7)
    WaitChrThread(0x1A, 0x1)

    def lambda_61C7():
        OP_8E(0xFE, 0xA1E0, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_61C7)
    WaitChrThread(0x1A, 0x1)

    def lambda_61E7():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_61E7)
    WaitChrThread(0x1A, 0x1)

    def lambda_6207():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6207)
    WaitChrThread(0x1A, 0x1)

    def lambda_6227():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_6227)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_32_61A1 end

    def Function_33_6242(): pass

    label("Function_33_6242")


    def lambda_6248():
        OP_8E(0xFE, 0x9088, 0x0, 0x72D8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6248)
    WaitChrThread(0x10, 0x1)

    def lambda_6268():
        OP_8E(0xFE, 0x9920, 0x0, 0x7B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6268)
    WaitChrThread(0x10, 0x1)

    def lambda_6288():
        OP_8E(0xFE, 0x9920, 0x0, 0x8AFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6288)
    WaitChrThread(0x10, 0x1)

    def lambda_62A8():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62A8)
    WaitChrThread(0x10, 0x1)

    def lambda_62C8():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62C8)
    WaitChrThread(0x10, 0x1)

    def lambda_62E8():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62E8)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_33_6242 end

    def Function_34_6303(): pass

    label("Function_34_6303")

    Sleep(400)

    def lambda_630E():
        OP_8E(0xFE, 0x8534, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_630E)
    WaitChrThread(0xFE, 0x1)

    def lambda_632E():
        OP_8E(0xFE, 0x9218, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_632E)
    WaitChrThread(0xFE, 0x1)

    def lambda_634E():
        OP_8E(0xFE, 0x99E8, 0x0, 0x7D00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_634E)
    WaitChrThread(0xFE, 0x1)

    def lambda_636E():
        OP_8E(0xFE, 0x99E8, 0x0, 0x8BD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_636E)
    WaitChrThread(0xFE, 0x1)

    def lambda_638E():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_638E)
    WaitChrThread(0xFE, 0x1)

    def lambda_63AE():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63AE)
    WaitChrThread(0xFE, 0x1)

    def lambda_63CE():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63CE)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_34_6303 end

    def Function_35_63E9(): pass

    label("Function_35_63E9")


    def lambda_63EF():
        OP_8E(0xFE, 0x9218, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_63EF)
    WaitChrThread(0x1D, 0x1)

    def lambda_640F():
        OP_8E(0xFE, 0x99E8, 0x0, 0x7D00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_640F)
    WaitChrThread(0x1D, 0x1)

    def lambda_642F():
        OP_8E(0xFE, 0x99E8, 0x0, 0x8BD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_642F)
    WaitChrThread(0x1D, 0x1)

    def lambda_644F():
        OP_8E(0xFE, 0xA474, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_644F)
    WaitChrThread(0x1D, 0x1)

    def lambda_646F():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x9664, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_646F)
    WaitChrThread(0x1D, 0x1)

    def lambda_648F():
        OP_8E(0xFE, 0xB7FC, 0x0, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_648F)
    WaitChrThread(0x1D, 0x1)
    Return()

    # Function_35_63E9 end

    def Function_36_64AA(): pass

    label("Function_36_64AA")

    EventBegin(0x0)
    OP_4A(0x11, 255)
    OP_4A(0x1B, 255)
    Fade(1000)
    OP_6D(-5200, 0, 34200, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(3760, 0)
    OP_6C(50000, 0)
    OP_6E(222, 0)
    SetChrPos(0x105, -7140, 0, 31540, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #319
        0x11,
        (
            "#5P啊，这么说，\x01",
            "共和国有那种东西啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x1B,
        (
            "#2P嗯嗯，\x01",
            "因为国土很辽阔嘛。\x02",
        )
    )

    Jump("loc_6571")

    label("loc_6571")

    CloseMessageWindow()

    ChrTalk(    #321
        0x1B,
        "#2P于是就采用了那样的交通手段……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x105,
        "#542F#12P对、对不起………\x02",
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x1B, 180, 400)
    Sleep(300)

    ChrTalk(    #323
        0x1B,
        "#5P哎呀，科洛丝同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x1B,
        "#5P……怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x105,
        (
            "#047F#12P嗯，这个嘛……\x02\x03",

            "#040F碧欧拉老师\x01",
            "让我发这些资料……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #326
        "\x07\x05把资料交给罗伊斯和塞尔玛。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #327
        0x11,
        "#5P啊，是社会系课程的学分表呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x11,
        (
            "#5P谢谢你拿给我们，\x01",
            "科洛丝同学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x105,
        (
            "#045F#12P哪里，不用客气。\x02\x03",

            "#542F我才是打扰了你们，\x01",
            "实在抱歉。\x02\x03",

            "#543F那我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x1B,
        "#5P好，好的……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    def lambda_67C1():

        label("loc_67C1")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_67C1")

    QueueWorkItem2(0x11, 2, lambda_67C1)

    def lambda_67D2():

        label("loc_67D2")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_67D2")

    QueueWorkItem2(0x1B, 2, lambda_67D2)
    OP_43(0x105, 0x3, 0x0, 0x25)
    Sleep(3000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_63(0x1B)
    Sleep(500)

    ChrTalk(    #331
        0x11,
        (
            "#5P科洛丝同学，\x01",
            "真是讲究礼仪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x1B,
        "#6P嗯嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x1B,
        (
            "#6P说话这么谨慎，\x01",
            "让我也有点紧张了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_689F():
        OP_6B(3660, 3000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_689F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x2D, 0x0)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0x2)
    OP_44(0x1B, 0x2)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, 33000, 0, 31400, 180)
    OP_6D(33000, 0, 31400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F67)
    EventEnd(0x0)
    Return()

    # Function_36_64AA end

    def Function_37_6934(): pass

    label("Function_37_6934")


    def lambda_693A():
        OP_8E(0xFE, 0xFFFFE41C, 0x0, 0x6FF4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_693A)
    WaitChrThread(0x105, 0x1)

    def lambda_695A():
        OP_8E(0xFE, 0xBB8, 0x0, 0x6FF4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695A)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_37_6934 end

    def Function_38_6975(): pass

    label("Function_38_6975")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-4340, 0, 32800, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x11, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrPos(0x105, 2960, 0, 26500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_69EA():
        OP_6D(3680, 0, 32800, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_69EA)
    FadeToBright(2000, 0)
    Sleep(4000)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_6A1A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6A1A)

    def lambda_6A2C():
        OP_8E(0xFE, 0xB90, 0x0, 0x6FF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6A2C)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 270, 500)
    Sleep(500)
    OP_8C(0x105, 0, 500)
    Sleep(500)

    def lambda_6A7B():
        OP_6D(3680, 0, 34800, 1100)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_6A7B)

    def lambda_6A93():
        OP_67(0, 5700, -10000, 1100)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_6A93)

    def lambda_6AAB():
        OP_8E(0xFE, 0x870, 0x0, 0x8534, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6AAB)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 600)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x2C, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #334
        0x105,
        "#047F#5P呼…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x105, 0, 400)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #335
        0x105,
        (
            "#049F#5P…………………………\x02\x03",

            "……我这样\x01",
            "没问题吗………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x105, 180, 350)
    Sleep(300)

    def lambda_6B97():
        OP_8E(0xFE, 0x870, 0x0, 0x6F7C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B97)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x105, 0x1)
    OP_6D(33000, 0, 33500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrPos(0x105, 33000, 0, 33500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0xF)
    OP_73(0xF)

    def lambda_6C38():
        OP_8E(0xFE, 0x80E8, 0x0, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C38)
    WaitChrThread(0x105, 0x1)
    OP_6F(0x2, 15)
    OP_70(0x2, 0x0)

    def lambda_6C66():
        OP_6D(42120, 0, 34520, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_6C66)

    def lambda_6C7E():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_6C7E)

    def lambda_6C8E():
        OP_8E(0xFE, 0x9E98, 0x0, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C8E)
    WaitChrThread(0x105, 0x1)

    def lambda_6CAE():
        OP_8E(0xFE, 0x9E98, 0x0, 0x80E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CAE)
    WaitChrThread(0x105, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 55160, 0, 34080, 0)

    NpcTalk(    #336
        0x1D,
        "声音",
        (
            "#3P#1S……对了，\x01",
            "刚才那个插班生来过了……\x02",
        )
    )

    Jump("loc_6D1D")

    label("loc_6D1D")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 90, 500)
    Sleep(500)

    NpcTalk(    #337
        0x1D,
        "声音",
        "#3P#1S……啊啊，那个天才……\x02",
    )

    Jump("loc_6D78")

    label("loc_6D78")

    CloseMessageWindow()

    NpcTalk(    #338
        0x1D,
        "声音",
        "#3P#1S……她啊…………\x02",
    )

    Jump("loc_6DA5")

    label("loc_6DA5")

    CloseMessageWindow()

    NpcTalk(    #339
        0x1D,
        "声音",
        "#3P#1S……………这样呢………\x02",
    )

    Jump("loc_6DD8")

    label("loc_6DD8")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #340
        0x105,
        (
            "#043F哎，这个……\x02\x03",

            "#049F（要、要早点回去，\x01",
            "  复习功课才行……）\x02\x03",

            "（而且也要确认一下\x01",
            "  已经修得的学分……！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E78():
        OP_8E(0xFE, 0x9E98, 0x0, 0x96B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E78)
    WaitChrThread(0x105, 0x1)

    def lambda_6E98():
        OP_8E(0xFE, 0xB608, 0xFFFFF830, 0x96B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E98)
    WaitChrThread(0x105, 0x1)

    def lambda_6EB8():
        OP_8E(0xFE, 0xB608, 0xFFFFF254, 0x8AAC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6EB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_38_6975 end

    def Function_39_6EE5(): pass

    label("Function_39_6EE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-4350, 200, 33340, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x1E, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x18, 255)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x105, 23)
    SetChrChipByIndex(0x1E, 26)
    SetChrChipByIndex(0x19, 24)
    SetChrChipByIndex(0x1D, 20)
    SetChrChipByIndex(0x1C, 18)
    SetChrChipByIndex(0x1B, 16)
    SetChrChipByIndex(0x10, 15)
    SetChrChipByIndex(0x11, 20)
    SetChrPos(0x19, 500, 200, 30000, 90)
    SetChrPos(0x1E, 500, 200, 32000, 90)
    SetChrPos(0x105, 500, 200, 34100, 90)
    SetChrPos(0x1D, -2750, 200, 30000, 90)
    SetChrPos(0x1C, -2750, 200, 32000, 90)
    SetChrPos(0x1B, -2750, 100, 34100, 90)
    SetChrPos(0x10, -5900, 100, 30000, 90)
    SetChrPos(0x11, -5900, 100, 32000, 90)
    SetChrPos(0x18, 4440, 250, 29740, 270)

    def lambda_7092():
        OP_6D(2070, 200, 33190, 5500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7092)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2B)
    Sleep(1000)
    OP_62(0x1E, 0x6E, 1800, 0x1C, 0x21, 0x12C, 0x0)
    Sleep(2000)
    SetChrSubChip(0x105, 2)
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x1E, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1D, 0x4)
    ClearChrFlags(0x1C, 0x4)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    OP_6D(6180, 0, 3680, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_4A(0x26, 255)
    OP_4A(0x27, 255)
    OP_4A(0x28, 255)
    OP_4A(0x29, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x21, 255)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x26, 29)
    SetChrChipByIndex(0x27, 28)
    SetChrChipByIndex(0x28, 16)
    SetChrChipByIndex(0x29, 19)
    SetChrChipByIndex(0x15, 21)
    SetChrChipByIndex(0x16, 17)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x26, 500, 200, 0, 90)
    SetChrPos(0x27, 500, 200, 2000, 90)
    SetChrPos(0x28, 500, 200, 4100, 90)
    SetChrPos(0x29, -2750, 200, 0, 90)
    SetChrPos(0x15, -2750, 200, 2000, 90)
    SetChrPos(0x16, -2750, 100, 4100, 90)
    SetChrPos(0x17, -5900, 100, 0, 90)
    SetChrPos(0x21, 5300, 250, 2120, 270)

    def lambda_72B5():
        OP_6D(-790, 0, 3010, 5500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_72B5)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2C)
    Sleep(1000)
    OP_62(0x15, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x15, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(2000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    ClearChrFlags(0x29, 0x4)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)
    OP_6D(89540, 1500, 32299, 0)
    OP_67(0, 6390, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_4A(0x1F, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x23, 255)
    OP_4A(0x24, 255)
    OP_4A(0x25, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x22, 255)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x1F, 27)
    SetChrChipByIndex(0x1A, 25)
    SetChrChipByIndex(0x23, 20)
    SetChrChipByIndex(0x24, 18)
    SetChrChipByIndex(0x25, 17)
    SetChrChipByIndex(0x12, 22)
    SetChrChipByIndex(0x13, 16)
    SetChrChipByIndex(0x14, 19)
    SetChrPos(0x1F, 90500, 200, 30000, 90)
    SetChrPos(0x1A, 90500, 200, 32000, 90)
    SetChrPos(0x23, 90500, 200, 34100, 90)
    SetChrPos(0x24, 87250, 200, 30000, 90)
    SetChrPos(0x25, 87250, 200, 32000, 90)
    SetChrPos(0x12, 87250, 100, 34100, 90)
    SetChrPos(0x13, 84100, 100, 30000, 90)
    SetChrPos(0x14, 84100, 100, 32000, 90)
    SetChrPos(0x22, 92400, 0, 35300, 270)
    OP_43(0x22, 0x0, 0x0, 0x29)
    SoundLoad(138)

    def lambda_74FC():
        OP_6D(89540, 200, 32299, 4500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_74FC)

    def lambda_7514():
        OP_67(0, 5500, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7514)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x105, 0x3, 0x0, 0x2D)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x12, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_62(0x12, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_22(0x8A, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x22, 0x0)

    def lambda_7595():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_7595)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x25, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x2D, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_23(0x8A)
    Sleep(2000)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x22, 0x80)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x1A, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x4)
    OP_6D(41540, 0, 38140, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(14000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x15, 40560, 0, 36200, 70)
    SetChrPos(0x12, 41900, 0, 37040, 230)
    SetChrPos(0x105, 37840, 0, 28560, 14)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x15, 11)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x12, 10)
    SetChrSubChip(0x12, 0)
    OP_4A(0x15, 255)
    OP_4A(0x12, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #341
        0x12,
        (
            "#734F#11P呼，\x01",
            "终于结束了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x15,
        (
            "#645F#6P不愧是有名的王立学院，\x01",
            "课程还真不简单啊～。\x02\x03",

            "真是累死我了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7800():
        OP_8E(0xFE, 0xA0DC, 0x0, 0x8854, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7800)
    Sleep(1300)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_784E():

        label("loc_784E")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_784E")

    QueueWorkItem2(0x15, 2, lambda_784E)
    Sleep(100)

    def lambda_7864():

        label("loc_7864")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_7864")

    QueueWorkItem2(0x12, 2, lambda_7864)
    Sleep(300)

    ChrTalk(    #343
        0x15,
        (
            "#640F#5P啊，科洛丝。\x02\x03",

            "怎么样？\x01",
            "考试的感觉。\x02",
        )
    )

    Jump("loc_78BE")

    label("loc_78BE")

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    OP_44(0x15, 0x2)
    OP_44(0x12, 0x2)
    TurnDirection(0x105, 0x15, 400)
    Sleep(300)

    ChrTalk(    #344
        0x105,
        (
            "#045F#12P嗯……\x01",
            "马马虎虎吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7907():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7907)
    TurnDirection(0x12, 0x15, 500)
    Sleep(1200)

    def lambda_7921():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7921)
    TurnDirection(0x12, 0x105, 500)
    Sleep(300)

    ChrTalk(    #345
        0x15,
        (
            "#649F#5P又来了～……\x01",
            "你这家伙总是这么假谦虚！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x12,
        (
            "#730F#11P刚才那笑容是怎么回事？\x01",
            "真是的…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x105,
        "#041F#12P呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x15,
        "#641F#5P这么从容的样子真让人火大……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 7)
    SetChrSubChip(0x1F, 0)
    OP_4A(0x1F, 255)
    SetChrPos(0x1F, 46130, 0, 28570, 315)

    def lambda_7A25():
        OP_8E(0xFE, 0xA5B4, 0x0, 0x8430, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7A25)
    Sleep(500)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0x1F, 0x1)
    Sleep(300)

    ChrTalk(    #349
        0x1F,
        (
            "#1780F你们几个挡路了，\x01",
            "别傻站在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7AF7():

        label("loc_7AF7")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_7AF7")

    QueueWorkItem2(0x15, 2, lambda_7AF7)

    def lambda_7B08():

        label("loc_7B08")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_7B08")

    QueueWorkItem2(0x12, 2, lambda_7B08)

    def lambda_7B19():

        label("loc_7B19")

        TurnDirection(0xFE, 0x1F, 500)
        OP_48()
        Jump("loc_7B19")

    QueueWorkItem2(0x105, 2, lambda_7B19)
    Sleep(300)

    ChrTalk(    #350
        0x105,
        "#044F#5P啊，雷欧学长……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(160, 110, -1, -1)
    SetChrName("一年级学生们")

    AnonymousTalk(    #351
        "\x07\x00#3S对、对不起。#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_7BAC():
        OP_8F(0xFE, 0x9E20, 0x0, 0x85DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BAC)

    def lambda_7BC7():
        OP_8F(0xFE, 0x9C04, 0x0, 0x8BF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7BC7)

    def lambda_7BE2():
        OP_8F(0xFE, 0xA5AA, 0x0, 0x92D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7BE2)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_7C0C():
        OP_8E(0xFE, 0xA23A, 0x0, 0x8A02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7C0C)
    WaitChrThread(0x1F, 0x1)

    def lambda_7C2C():
        OP_8E(0xFE, 0xA154, 0x0, 0x97EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7C2C)
    WaitChrThread(0x1F, 0x1)
    Sleep(300)

    ChrTalk(    #352
        0x1F,
        "#1782F#5P对了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1F, 190, 400)
    Sleep(300)

    ChrTalk(    #353
        0x1F,
        (
            "#1780F#5P从今天开始继续学生会活动。\x02\x03",

            "乔儿和汉斯两点钟\x01",
            "到学生会室开会。\x02\x03",

            "#1783F别迟到哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x15,
        "#642F是、是！\x02",
    )


    ChrTalk(    #355
        0x12,
        "#732F#4P是、是！\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #356
        0x1F,
        (
            "#1782F#5P……对了。\x02\x03",

            "#1781F科洛丝，你看情况行事吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D68():
        OP_8E(0xFE, 0xB554, 0xFFFFF830, 0x97EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7D68)
    WaitChrThread(0x1F, 0x1)
    OP_44(0x105, 0x2)
    OP_44(0x15, 0x2)
    OP_44(0x12, 0x2)

    def lambda_7D94():
        OP_8E(0xFE, 0xB554, 0xFFFFF254, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_7D94)
    WaitChrThread(0x1F, 0x1)
    SetChrFlags(0x1F, 0x80)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #357
        0x105,
        "#044F#6P………………哎？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x15,
        (
            "#648F#5P……唔，\x01",
            "他是希望科洛丝也去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 240, 400)

    def lambda_7E6F():
        OP_8F(0xFE, 0xA280, 0x0, 0x8F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7E6F)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #359
        0x12,
        (
            "#730F#11P对于抓捕雷克特学长，\x01",
            "科洛丝是不可或缺的人才。\x02\x03",

            "#731F雷欧学长也算是\x01",
            "承认科洛丝了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 14, 400)
    Sleep(300)

    ChrTalk(    #360
        0x105,
        (
            "#045F#6P啊、啊哈哈……\x02\x03",

            "感觉这么说\x01",
            "好像有点夸张……\x02\x03",

            "#048F不过，我也去看看吧。\x01",
            "好像很有趣的样子……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7F8E():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_7F8E)
    TurnDirection(0x12, 0x105, 500)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #361
        0x12,
        (
            "#734F#11P……不、不，\x01",
            "我想没有那么有趣啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x15,
        (
            "#640F#5P不过，\x01",
            "科洛丝能来的话就帮大忙了。\x02\x03",

            "#641F当然是热烈欢迎啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x12,
        (
            "#731F#11P那么，吃完午饭以后\x01",
            "我们三个一起去学生会室吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x105,
        "#041F#6P好的。\x02",
    )

    CloseMessageWindow()

    def lambda_80C6():
        OP_8C(0xFE, 14, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_80C6)
    OP_43(0x12, 0x3, 0x0, 0x28)

    def lambda_80DB():
        OP_8C(0xFE, 60, 500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_80DB)
    OP_43(0x15, 0x3, 0x0, 0x28)
    Sleep(400)

    def lambda_80F5():
        OP_8E(0xFE, 0xA140, 0x0, 0x904C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80F5)
    WaitChrThread(0x105, 0x1)
    OP_43(0x105, 0x3, 0x0, 0x28)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x2F6C)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_39_6EE5 end

    def Function_40_817B(): pass

    label("Function_40_817B")

    WaitChrThread(0xFE, 0x2)

    def lambda_8186():
        OP_8E(0xFE, 0xA7BC, 0x0, 0x96C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8186)
    WaitChrThread(0xFE, 0x1)

    def lambda_81A6():
        OP_8E(0xFE, 0xB860, 0xFFFFF830, 0x96C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_81A6)
    WaitChrThread(0xFE, 0x1)

    def lambda_81C6():
        OP_8E(0xFE, 0xB860, 0xFFFFF254, 0x89E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_81C6)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_40_817B end

    def Function_41_81E1(): pass

    label("Function_41_81E1")

    OP_8E(0x22, 0x15D9C, 0x0, 0x89E4, 0x7D0, 0x0)
    OP_8E(0x22, 0x15D9C, 0x0, 0x7080, 0x7D0, 0x0)
    OP_8E(0x22, 0x14FB4, 0x0, 0x7080, 0x7D0, 0x0)
    OP_8E(0x22, 0x14FB4, 0x0, 0x89E4, 0x7D0, 0x0)
    Return()

    # Function_41_81E1 end

    def Function_42_8232(): pass

    label("Function_42_8232")

    OP_62(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFE)
    Return()

    # Function_42_8232 end

    def Function_43_824D(): pass

    label("Function_43_824D")

    OP_43(0x19, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1C, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1D, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x1B, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x19, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x11, 0x3, 0x0, 0x2A)
    Sleep(1000)
    Return()

    # Function_43_824D end

    def Function_44_82AE(): pass

    label("Function_44_82AE")

    OP_43(0x29, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x28, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x26, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x17, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x27, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x16, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x29, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x28, 0x3, 0x0, 0x2A)
    Sleep(1000)
    Return()

    # Function_44_82AE end

    def Function_45_830F(): pass

    label("Function_45_830F")

    OP_43(0x13, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x1F, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x25, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x14, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x1A, 0x3, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x24, 0x3, 0x0, 0x2A)
    Sleep(1000)
    OP_43(0x23, 0x3, 0x0, 0x2A)
    Return()

    # Function_45_830F end

    def Function_46_835F(): pass

    label("Function_46_835F")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(116660, 0, 4640, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x20, 0)
    SetChrPos(0x105, 115970, 0, 2460, 0)
    Sleep(1000)

    ChrTalk(    #365
        0x20,
        (
            "#780F#5P哦，科洛丝。\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x105,
        (
            "#543F#12P不好意思，校长。\x01",
            "我有些重要的事……\x02\x03",

            "#542F能不能批准我外出呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #367
        "\x07\x05科洛丝简短地说明了情况。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #368
        0x20,
        (
            "#783F#5P原来如此，\x01",
            "因为学生会的事要去卢安……\x02\x03",

            "#780F当然没问题。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #369
        "\x07\x05得到了外出许可证。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #370
        0x105,
        "#048F#12P非常感谢您。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x20,
        (
            "#780F#5P嗯，\x01",
            "你似乎也差不多习惯这里的生活了吧。\x02\x03",

            "#781F呵呵，我听说了哦。\x01",
            "你经常在学院里到处跑对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x105,
        (
            "#045F#12P啊、啊哈哈……\x02\x03",

            "最近在给学生会\x01",
            "帮忙一些事情。\x02\x03",

            "所以，那个……\x01",
            "有些事要跑来跑去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x20,
        "#781F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x105,
        (
            "#542F#12P嗯，\x01",
            "那么我就此告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x20,
        "#780F#5P啊啊，路上小心哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x105,
        "#041F#12P嗯。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 135, 400)

    def lambda_86C7():
        OP_8E(0xFE, 0x1C908, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86C7)
    WaitChrThread(0x105, 0x1)

    def lambda_86E7():
        OP_8E(0xFE, 0x1C908, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86E7)
    WaitChrThread(0x105, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_8711():
        OP_8E(0xFE, 0x1C908, 0x0, 0xFFFFF254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8711)

    def lambda_872C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_872C)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x20)
    Sleep(500)

    ChrTalk(    #377
        0x20,
        (
            "#781F#5P呵呵……\x01",
            "她的表情开朗多了呢。\x02\x03",

            "#780F嗯……\x01",
            "这可能也是托他的福吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(59000, 0, 1400, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, 59000, 0, 1400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x1E, 0x80)
    OP_63(0x1E)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x10)
    SetChrPos(0x2B, 40990, 0, 5500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F6D)
    EventEnd(0x0)
    Return()

    # Function_46_835F end

    def Function_47_8867(): pass

    label("Function_47_8867")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #378
        "\x07\x05职员室里好像正在开会。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #379
        0x105,
        "#047F（……不能进去呢。）\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_47_8867 end

    def Function_48_88D1(): pass

    label("Function_48_88D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_89E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8947")

    ChrTalk(    #380
        0x105,
        (
            "#040F第二是雷欧学长，\x01",
            "第三是利戈尔部长……\x02\x03",

            "#045F啊，我也是一年级生里的第一名……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89E6")

    label("loc_8947")


    ChrTalk(    #381
        0x105,
        (
            "#040F这是定期考试的成绩吧……\x01",
            "三年级前五名……\x02\x03",

            "#044F……第一是………\x01",
            "雷克特·亚兰德尔！？\x02\x03",

            "他明明是几乎\x01",
            "从来没有上过课啊……？？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_89E6")

    Jump("loc_8A8C")

    label("loc_89E9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #382
        (
            "\x07\x05　　　　※时间表变更通知※\x01",
            "１８日第２节　　　　社会系体育课≡社会课\x01",
            "１９日第３·４节　　全学年共同授课≡各系主课\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8A8C")

    TalkEnd(0xFF)
    Return()

    # Function_48_88D1 end

    def Function_49_8A90(): pass

    label("Function_49_8A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8AE1")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #383
        "\x07\x05还保留着一些温度…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_8BAB")

    label("loc_8AE1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #384
        "\x07\x05还保留着一些温度…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #385
        0x13B,
        (
            "#647F他应该还\x01",
            "没走多远吧。\x02\x03",

            "#1891F那就地毯式搜索吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x152,
        "#732F哦！\x02",
    )

    Jump("loc_8B8B")

    label("loc_8B8B")

    CloseMessageWindow()

    ChrTalk(    #387
        0x105,
        "#042F好、好的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8BAB")

    TalkEnd(0xFF)
    Return()

    # Function_49_8A90 end

    def Function_50_8BAF(): pass

    label("Function_50_8BAF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #388
        (
            "\x07\x05　　走　\x01",
            "　　廊　\x01",
            "　　里　\x01",
            "　　请　\x01",
            "　　安　\x01",
            "　学静　\x01",
            "　生！　\x01",
            "　指　　\x01",
            "　导　　\x01",
            "　部　　\x02",
        )
    )

    Jump("loc_8C9C")

    label("loc_8C9C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_50_8BAF end

    SaveToFile()

Try(main)
