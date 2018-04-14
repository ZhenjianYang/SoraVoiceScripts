from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0130   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0130.x',
        MapIndex            = 3,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0130_1 ._SN',
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
        '迪拜恩教区长',                         # 9
        '修女梅',                               # 10
        '凯文神父',                             # 11
        '矿工皮尔姆',                           # 12
        '乘务员库因特',                         # 13
        '矿工海涅',                             # 14
        '克露莎',                               # 15
        '阿鲁姆',                               # 16
        '艾娅莉',                               # 17
        '安敦',                                 # 18
        '伴娘',                                 # 19
        '布露姆老奶奶',                         # 20
        '亚尔丽 ',                              # 21
        '鲁克',                                 # 22
        '帕特',                                 # 23
        '赛拉',                                 # 24
        '托露塔',                               # 25
        '胡里奥',                               # 26
        '伊娜',                                 # 27
        '安莉尔',                               # 28
        '临时演员',                             # 29
        '临时演员',                             # 30
        '临时演员',                             # 31
        '临时演员',                             # 32
        '临时演员',                             # 33
        '新郎的亲属',                           # 34
        '新郎的亲属',                           # 35
        '新郎的亲属',                           # 36
        '新娘的亲属',                           # 37
        '新娘的亲属',                           # 38
        '新娘的亲属',                           # 39
        '新娘的朋友',                           # 40
        '新娘的朋友',                           # 41
        '目标用照相机',                         # 42
        '小猫',                                 # 43
        '小猫',                                 # 44
        '小猫',                                 # 45
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01290 ._CH',             # 04
        'ED6_DT07/CH01070 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01150 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT07/CH01690 ._CH',             # 09
        'ED6_DT27/CH03005 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01013 ._CH',             # 0C
        'ED6_DT07/CH01033 ._CH',             # 0D
        'ED6_DT07/CH01160 ._CH',             # 0E
        'ED6_DT07/CH01060 ._CH',             # 0F
        'ED6_DT07/CH01133 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01700 ._CH',             # 12
        'ED6_DT07/CH01053 ._CH',             # 13
        'ED6_DT07/CH01223 ._CH',             # 14
        'ED6_DT07/CH01593 ._CH',             # 15
        'ED6_DT07/CH01233 ._CH',             # 16
        'ED6_DT07/CH01183 ._CH',             # 17
        'ED6_DT07/CH01030 ._CH',             # 18
        'ED6_DT07/CH01200 ._CH',             # 19
        'ED6_DT07/CH01470 ._CH',             # 1A
        'ED6_DT07/CH01490 ._CH',             # 1B
        'ED6_DT07/CH01230 ._CH',             # 1C
        'ED6_DT07/CH01480 ._CH',             # 1D
        'ED6_DT07/CH01213 ._CH',             # 1E
        'ED6_DT07/CH01130 ._CH',             # 1F
        'ED6_DT26/CH20311 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01290P._CP',             # 04
        'ED6_DT07/CH01070P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01150P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT07/CH01690P._CP',             # 09
        'ED6_DT27/CH03005P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01013P._CP',             # 0C
        'ED6_DT07/CH01033P._CP',             # 0D
        'ED6_DT07/CH01160P._CP',             # 0E
        'ED6_DT07/CH01060P._CP',             # 0F
        'ED6_DT07/CH01133P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01700P._CP',             # 12
        'ED6_DT07/CH01053P._CP',             # 13
        'ED6_DT07/CH01223P._CP',             # 14
        'ED6_DT07/CH01593P._CP',             # 15
        'ED6_DT07/CH01233P._CP',             # 16
        'ED6_DT07/CH01183P._CP',             # 17
        'ED6_DT07/CH01030P._CP',             # 18
        'ED6_DT07/CH01200P._CP',             # 19
        'ED6_DT07/CH01470P._CP',             # 1A
        'ED6_DT07/CH01490P._CP',             # 1B
        'ED6_DT07/CH01230P._CP',             # 1C
        'ED6_DT07/CH01480P._CP',             # 1D
        'ED6_DT07/CH01213P._CP',             # 1E
        'ED6_DT07/CH01130P._CP',             # 1F
        'ED6_DT26/CH20311P._CP',             # 20
    )

    DeclNpc(
        X                   = 58800,
        Z                   = 1000,
        Y                   = 52200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -16830,
        Z                   = 0,
        Y                   = 42890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55420,
        Z                   = 0,
        Y                   = 46990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 58970,
        Z                   = 0,
        Y                   = 47900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 62060,
        Z                   = 0,
        Y                   = 43550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56050,
        Z                   = 0,
        Y                   = 40700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 55340,
        Z                   = 0,
        Y                   = 47470,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 47270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 64000,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 58300,
        Z                   = 0,
        Y                   = 44200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57670,
        Z                   = 0,
        Y                   = 48880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55310,
        Z                   = 150,
        Y                   = 45960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56390,
        Z                   = 150,
        Y                   = 45990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 54680,
        Z                   = 0,
        Y                   = 44910,
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
        X                   = 55400,
        Z                   = 0,
        Y                   = 44910,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 56470,
        Z                   = 150,
        Y                   = 44510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 56150,
        Z                   = 0,
        Y                   = 41510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 61860,
        Z                   = 150,
        Y                   = 42920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 62700,
        Z                   = 150,
        Y                   = 42950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62960,
        Z                   = 0,
        Y                   = 43610,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54500,
        Z                   = 150,
        Y                   = 42970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55920,
        Z                   = 150,
        Y                   = 42970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55090,
        Z                   = 150,
        Y                   = 41510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62110,
        Z                   = 150,
        Y                   = 41430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63630,
        Z                   = 150,
        Y                   = 41440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 57680,
        Z                   = 0,
        Y                   = 43380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 58780,
        Z                   = 0,
        Y                   = 46800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 63110,
        Z                   = 0,
        Y                   = 46830,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57650,
        Z                   = 0,
        Y                   = 42350,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -16100,
        Z                   = 0,
        Y                   = 45910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 54130,
        Z                   = 0,
        Y                   = 50110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 52890,
        Z                   = 0,
        Y                   = 48010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 52980,
        Z                   = 0,
        Y                   = 46970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63200,
        Z                   = 0,
        Y                   = 43610,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63700,
        Z                   = 0,
        Y                   = 43610,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 64099,
        Z                   = 0,
        Y                   = 43610,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50290,
        TriggerRange        = 400,
        ActorX              = 58800,
        ActorZ              = 2500,
        ActorY              = 52200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 52200,
        TriggerZ            = 5000,
        TriggerY            = 52260,
        TriggerRange        = 600,
        ActorX              = 52200,
        ActorZ              = 5600,
        ActorY              = 52260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_69A",          # 00, 0
        "Function_1_898",          # 01, 1
        "Function_2_8E3",          # 02, 2
        "Function_3_A60",          # 03, 3
        "Function_4_A84",          # 04, 4
        "Function_5_A89",          # 05, 5
        "Function_6_222A",         # 06, 6
        "Function_7_2803",         # 07, 7
        "Function_8_28E5",         # 08, 8
        "Function_9_2D64",         # 09, 9
        "Function_10_2DE2",        # 0A, 10
        "Function_11_2EA9",        # 0B, 11
        "Function_12_2FD8",        # 0C, 12
        "Function_13_3188",        # 0D, 13
        "Function_14_387E",        # 0E, 14
        "Function_15_3D3F",        # 0F, 15
        "Function_16_3F6E",        # 10, 16
        "Function_17_3FF5",        # 11, 17
        "Function_18_4049",        # 12, 18
        "Function_19_40AA",        # 13, 19
        "Function_20_4105",        # 14, 20
        "Function_21_4150",        # 15, 21
        "Function_22_419B",        # 16, 22
        "Function_23_41EC",        # 17, 23
        "Function_24_4249",        # 18, 24
        "Function_25_42A5",        # 19, 25
        "Function_26_437A",        # 1A, 26
        "Function_27_4FC6",        # 1B, 27
        "Function_28_5024",        # 1C, 28
        "Function_29_5075",        # 1D, 29
        "Function_30_50FF",        # 1E, 30
    )


    def Function_0_69A(): pass

    label("Function_0_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_764")
    SetChrChipByIndex(0x14, 24)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -16010, 0, 43960, 180)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrPos(0x9, 59550, 0, 48300, 270)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xF, 58560, 0, 48300, 90)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x10, -15950, 0, 43090, 270)
    SetChrFlags(0x10, 0x10)
    SetChrChipByIndex(0x17, 31)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -15930, 0, 42250, 0)
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    Jump("loc_7D1")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76F")
    Jump("loc_7D1")

    label("loc_76F")

    SetChrChipByIndex(0x14, 24)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 56320, 0, 46950, 270)
    OP_43(0x14, 0x0, 0x0, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x19, 33)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x19, 55160, 0, 46950, 90)
    ClearChrFlags(0x19, 0x80)
    OP_43(0x19, 0x0, 0x0, 0x2)

    label("loc_7D1")

    Jump("loc_833")

    label("loc_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7E3")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_833")

    label("loc_7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_806")
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_833")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_81A")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x10)
    Jump("loc_833")

    label("loc_81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_824")
    Jump("loc_833")

    label("loc_824")

    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    label("loc_833")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_863")
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x2000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_882")
    Event(1, 7)

    label("loc_882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_897")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_897")

    Return()

    # Function_0_69A end

    def Function_1_898(): pass

    label("Function_1_898")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8BB")
    OP_65(0x1, 0x1)

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CD")
    Jump("loc_8E2")

    label("loc_8CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")
    Jump("loc_8E2")

    label("loc_8D8")

    OP_D2(0x700A8, 0x700AC, 0x21)

    label("loc_8E2")

    Return()

    # Function_1_898 end

    def Function_2_8E3(): pass

    label("Function_2_8E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A4A")

    label("loc_908")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_921")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A4A")

    label("loc_921")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A4A")

    label("loc_93A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A4A")

    label("loc_953")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A4A")

    label("loc_96C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A4A")

    label("loc_985")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A4A")

    label("loc_99E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A4A")

    label("loc_9B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A4A")

    label("loc_9D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A4A")

    label("loc_9E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A02")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A4A")

    label("loc_A02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A4A")

    label("loc_A1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A34")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A4A")

    label("loc_A34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A4A")

    label("loc_A5F")

    Return()

    # Function_2_8E3 end

    def Function_3_A60(): pass

    label("Function_3_A60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A83")
    OP_8D(0xFE, 54500, 46700, 56400, 48400, 2000)
    Jump("Function_3_A60")

    label("loc_A83")

    Return()

    # Function_3_A60 end

    def Function_4_A84(): pass

    label("Function_4_A84")

    Call(0, 5)
    Return()

    # Function_4_A84 end

    def Function_5_A89(): pass

    label("Function_5_A89")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D41")
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(    #0
        0x8,
        "啊……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(    #1
        0x8,
        "不是约修亚吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF4")

    label("loc_AD3")


    ChrTalk(    #2
        0x8,
        (
            "站在那里的…\x01",
            "不是约修亚吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF4")


    ChrTalk(    #3
        0x102,
        (
            "#1035F是的……\x01",
            "我回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "……我一直在等你哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "嗯……\x01",
            "表情很沉稳，很好～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "看来你已经找到自己\x01",
            "的道路了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#1040F是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "……艾丝蒂尔，约修亚，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "如今的世界\x01",
            "再次陷入了混乱，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "但是不管发生什么情况，\x01",
            "也绝对不能迷失自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "引导我们的\x01",
            "希望之光……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "并不在别处，\x01",
            "而是在我们自己的心中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002F嗯……我明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#1040F您的话……\x01",
            "我一定会牢记在心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(    #15
        0x8,
        "嗯，那样再好不过。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "好了，本来还想多和你们\x01",
            "说几句话…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "但如今是非常时刻，\x01",
            "就不多耽误你们的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1016F啊哈哈……说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        "#1040F是，那么改日再来拜访。\x02",
    )

    CloseMessageWindow()

    label("loc_D38")

    OP_A2(0x1)
    OP_A2(0x209E)
    Jump("loc_1091")

    label("loc_D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DD5")

    ChrTalk(    #20
        0x8,
        (
            "不管发生什么事情\x01",
            "也绝对不能迷失自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "引导我们的希望之光，\x01",
            "就在我们自己的心中。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD2")

    ChrTalk(    #22
        0x8,
        (
            "那么… \x01",
            "我也要开始准备婚礼仪式了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD2")

    Jump("loc_1091")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECD")

    ChrTalk(    #23
        0x8,
        (
            "嗯，婚礼总算是\x01",
            "顺利完成了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #24
        0x8,
        (
            "艾丝蒂尔你们\x01",
            "好像也出席了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1011F啊，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        "#1040F嗯，只是最后的部分而已。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "这也是人生的一个重要部分，\x01",
            "值得我们仔细体会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "当然了，对你们来说～\x01",
            "还稍微有些遥远。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_F2F")

    label("loc_ECD")


    ChrTalk(    #29
        0x8,
        (
            "这也是人生的一个重要部分，\x01",
            "值得我们仔细体会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "毕竟这是我们每个人都要\x01",
            "经历思考的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F2F")

    Jump("loc_1091")

    label("loc_F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1007")

    ChrTalk(    #31
        0x8,
        (
            "今天教堂里准备举行\x01",
            "结婚仪式。\x01",
            "准备工作很忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "即使在乌云之下，鸟儿也会鸣叫。\x01",
            "即使在寒冷的冰雪中，草木也会发芽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "因此，即使在如今这种混乱的世态下，\x01",
            "我们也要努力继续\x01",
            "过好自己的生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1091")

    label("loc_1007")


    ChrTalk(    #34
        0x8,
        (
            "即使在乌云之下，鸟儿也会鸣叫。\x01",
            "即使在寒冷的冰雪中，草木也会发芽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "因此，即使在如今这种混乱的世态下，\x01",
            "也要继续过好自己的生活。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1091")

    Jump("loc_2226")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_166A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 5)), scpexpr(EXPR_END)), "loc_1420")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_113A")

    ChrTalk(    #36
        0x8,
        (
            "醉倒的两个人\x01",
            "我已经安置好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "还好没有\x01",
            "酒精中毒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "再怎么自信十足，\x01",
            "也不该喝这么多酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "和爱娜拼酒\x01",
            "简直是折磨自己的身体。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141D")

    label("loc_113A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x800)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")

    ChrTalk(    #40
        0x8,
        (
            "对了，是之前\x01",
            "的酒馆事件吗…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "醉倒的两个人\x01",
            "我已经安置好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "还好没有\x01",
            "酒精中毒。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12EC")
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #43
        0x8,
        (
            "……哎呀。\x01",
            "刚刚才说到你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "……奥利维尔…\x01",
            "已经没关系了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x104,
        (
            "#035F呵～总算没事了，\x02\x03",

            "给大家添麻烦了，\x01",
            "不过现在已经不用担心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "嗯……\x01",
            "所以……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "再怎么自信十足，\x01",
            "也不该喝这么多酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "和爱娜拼酒\x01",
            "简直是折磨自己的身体。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1007F确、确实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        "#034F好、好好记下来了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1373")

    label("loc_12EC")


    ChrTalk(    #51
        0x8,
        (
            "再怎么自信十足，\x01",
            "也不该喝这么多酒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "和爱娜拼酒\x01",
            "就是在破坏自己的身体呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1007F确、确实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        "#025F呼，好好记下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1373")

    OP_28(0x76, 0x1, 0x800)
    OP_A2(0xE)
    Jump("loc_141D")

    label("loc_137F")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(    #55
        0x8,
        (
            "看着艾丝蒂尔的成长，\x01",
            "对我也是很有帮助的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "就算以后到其它地区工作，\x01",
            "也别忘记今天的心情喔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "心中坚定的信念\x01",
            "无论到任何时候也都不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141D")

    Jump("loc_1667")

    label("loc_1420")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #58
        0x8,
        "啊，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "你这次的活跃\x01",
            "我也已经听说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "你终于战胜了困难啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "我身为一名市民，\x01",
            "也要好好感谢你才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1008F嘿嘿……\x02\x03",

            "教区长的赞扬\x01",
            "实在是愧不敢当啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x103,
        (
            "#020F应该道谢的其实是我们才对。\x02\x03",

            "联络大圣堂还有照顾受害者……\x01",
            "真是多亏了您的帮助。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #64
        0x8,
        (
            "哪里，我身为一名神父，\x01",
            "这些都只是份内之事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #65
        0x8,
        (
            "只是，在困难重重的处境下，\x01",
            "看着艾丝蒂尔的成长，\x01",
            "对我也是很有帮助的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "就算以后到其它地区工作，\x01",
            "也别忘记今天的心情喔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1006F……是！\x02\x03",

            "那么先就这样了，教区长…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "一路小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "我会祈愿女神\x01",
            "保佑各位的…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A5D)

    label("loc_1667")

    Jump("loc_2226")

    label("loc_166A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 2)), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(    #70
        0x8,
        (
            "力量不足或是失败…\x01",
            "都不足为惧，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "现在我们唯一能做的\x01",
            "就是拿出自己的全部力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "结果那应该是解决事件\x01",
            "的最佳途径。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B66")

    label("loc_16F8")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #73
        0x8,
        (
            "啊，艾丝蒂尔……\x01",
            "还有雪拉扎德…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "你们已经见到\x01",
            "凯文神父了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1025F啊，是的。\x02\x03",

            "他现在应该还在\x01",
            "帕赛尔农场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "嗯，可是…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "……表情似乎\x01",
            "很迷茫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1026F啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "虽然没有完全理解，\x01",
            "不过只能试试看了……\x01",
            "状况已经是那个样子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "所以，一定不要迷失自我，\x01",
            "努力踏出自己的脚步就对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "未来一定会\x01",
            "越来越好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "也许是因为有优秀的前辈\x01",
            "一直在指导吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1017F嘿嘿……\x01",
            "确实如此呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1980")

    ChrTalk(    #85
        0x104,
        (
            "#031F呵呵～听你这么说，\x01",
            "还真是有点不好意思呢。\x02\x03",

            "呵呵，虽说艾丝蒂尔\x01",
            "确实是我看着成长起来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #86
        0x101,
        (
            "#1007F……啊啊，为什么奥利维尔\x01",
            "会在这时候出现。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA2")

    label("loc_1980")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E6")

    ChrTalk(    #87
        0x106,
        (
            "#051F嘿，真是少见。\x02\x03",

            "要是能一直这样\x01",
            "那可就谢天谢地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        "#021F呵呵，真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA2")

    label("loc_19E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A55")

    ChrTalk(    #89
        0x108,
        (
            "#071F喂喂，怎么了？\x01",
            "竟然会这么老实。\x02\x03",

            "哈哈，这样\x01",
            "可真不像你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        "#020F呵呵，真是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA2")

    label("loc_1A55")


    ChrTalk(    #91
        0x103,
        "#021F呵呵，这还真少见。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #92
        0x101,
        (
            "#1007F嗯……\x01",
            "要是能一直这样就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA2")


    ChrTalk(    #93
        0x8,
        (
            "不管怎样，力量不足或是失败\x01",
            "都不足为惧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "现在我们唯一能做的\x01",
            "就是拿出自己的全部力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "结果那应该是解决事件\x01",
            "的最佳途径。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #96
        0x101,
        "#1006F嗯，教区长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        "#020F嗯，就那么做吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1892)

    label("loc_1B66")

    Jump("loc_2226")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C0F")

    ChrTalk(    #98
        0x8,
        (
            "很遗憾，以手头的资料来看\x01",
            "这是办不到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "我为了保护人们的身心健康\x01",
            "而学习医术和药理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "但这片大地上似乎还有很多\x01",
            "无法理解的神秘现象呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D26")

    label("loc_1C0F")


    ChrTalk(    #101
        0x8,
        (
            "啊，各位。\x01",
            "很早嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "很遗憾，以手头的资料来看\x01",
            "这是办不到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "我为了保护人们的身心健康\x01",
            "而学习医术和药理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "但这片大地上似乎还有很多\x01",
            "无法理解的神秘现象呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "我们作为七耀教会的信徒，\x01",
            "虽然知道追求真理之道遥远而艰辛，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "但只要还有希望\x01",
            "就绝不能放弃努力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1D26")

    Jump("loc_2226")

    label("loc_1D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1FFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 1)), scpexpr(EXPR_END)), "loc_1DE3")

    ChrTalk(    #107
        0x8,
        (
            "正因为无法看到，\x01",
            "所以反而思考了不少东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "完全不用顾及外界的变化，\x01",
            "静下心来重新审视了一下过去的自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "……仔细想想的话，\x01",
            "这场大雾从某种意义上说也是好事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FFC")

    label("loc_1DE3")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #110
        0x8,
        (
            "……啊，这不是艾丝蒂尔\x01",
            "和雪拉扎德吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "嗯，好久不见了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1011F啊，是的……\x01",
            "教区长，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        (
            "#020F教区长身体健康\x01",
            "就比什么都好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        "你们两个都回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "现在洛连特被浓雾笼罩，\x01",
            "看东西都很困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "不过，正因为什么都看不见，\x01",
            "所以反而思考了不少东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "完全不用顾及外界的变化，\x01",
            "静下心来重新审视了一下过去的自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "……仔细想想的话，\x01",
            "这场大雾从某种意义上说也是好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1007F（嗯、嗯……\x01",
            "还是好难懂啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x103,
        (
            "#020F（确实……\x01",
            "  不过，很值得慢慢品味呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1891)

    label("loc_1FFC")

    Jump("loc_2226")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 1)), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(    #121
        0x8,
        "艾丝蒂尔，你终于回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "空之女神爱德丝啊！\x01",
            "请您引导彷徨的人们吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2226")

    label("loc_205F")


    ChrTalk(    #123
        0x8,
        "……啊，这不是艾丝蒂尔吗…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x142, 400)

    ChrTalk(    #124
        0x8,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x142,
        (
            "#1060F初次见面，教区长。\x01",
            "我是巡回神父凯文·格拉汉姆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "喔！说起来的话，听说有个\x01",
            "从总教会被调派到王都的巡回神父，\x01",
            "莫非就是…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x142,
        (
            "#1060F嗯！那就是我啦。\x02\x03",

            "……但…要说清楚为什么会在这里\x01",
            "可就要花费很多时间了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #128
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x142, 400)

    ChrTalk(    #129
        0x8,
        "（…………凯文神父。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x142,
        "#1060F（嗯？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "（艾丝蒂尔那孩子……\x01",
            "　就拜托你了。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x142,
        (
            "#1063F……！！\x02\x03",

            "#1060F（是，我明白了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1031)

    label("loc_2226")

    TalkEnd(0x8)
    Return()

    # Function_5_A89 end

    def Function_6_222A(): pass

    label("Function_6_222A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_2300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B9")

    ChrTalk(    #133
        0x9,
        (
            "结婚仪式顺利结束，\x01",
            "总算是松了口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "不过，竟然在现在这种时期\x01",
            "举办结婚仪式…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        (
            "不愧是洛连特。\x01",
            "真是惊人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_22FD")

    label("loc_22B9")


    ChrTalk(    #136
        0x9,
        (
            "在这种非常时期\x01",
            "举办结婚仪式…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "不愧是洛连特。\x01",
            "真是惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22FD")

    Jump("loc_27FF")

    label("loc_2300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")
    Call(0, 7)
    Jump("loc_2360")

    label("loc_2316")


    ChrTalk(    #138
        0x9,
        (
            "交换戒指之后，\x01",
            "接下来就是接吻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "好啦，之前早已经\x01",
            "练习好了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2360")

    Jump("loc_27FF")

    label("loc_2363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_249F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_23CA")

    ChrTalk(    #140
        0xFE,
        (
            "亚尔特利亚法典国的事情\x01",
            "我也不是太清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "不过那位神父应该就是\x01",
            "出身于那里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249C")

    label("loc_23CA")


    ChrTalk(    #142
        0xFE,
        (
            "之前那位巡回神父和教区长\x01",
            "聊了一阵…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "听说那位巡回神父\x01",
            "是从亚尔特利亚法典国的总部\x01",
            "派遣过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "那么年轻的人竟然就当上神父了，\x01",
            "真是让人吃惊呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "一直都以为总部的神父\x01",
            "都是严肃古板的老头子呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_249C")

    Jump("loc_27FF")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2510")

    ChrTalk(    #146
        0xFE,
        (
            "之前来的那位神父大人……\x01",
            "和我印象中神父的形象完全不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "那种风格也许在\x01",
            "王都很流行吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2594")

    label("loc_2510")


    ChrTalk(    #148
        0xFE,
        (
            "刚才来过一位从王都大圣堂\x01",
            "来的神父。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "无论是发型还是说话方式，\x01",
            "都给人耳目一新的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "难道王都现在流行\x01",
            "那种风格吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2594")

    Jump("loc_27FF")

    label("loc_2597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_26E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_260E")

    ChrTalk(    #151
        0xFE,
        (
            "教区长结果一晚都没睡，\x01",
            "好像不停的做着研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "我身为教会的修女，\x01",
            "也要努力做自己力所能及的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_260E")


    ChrTalk(    #153
        0xFE,
        (
            "教区长结果一晚都没睡，\x01",
            "好像不停的做着研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "只要自己还有一点力气，\x01",
            "我就会继续努力祈祷的…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "不知道什么时候就睡了过去，\x01",
            "等醒来的时候都已经是早上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "呼～离教区长的境界…\x01",
            "实在还差得很远呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_26DF")

    Jump("loc_27FF")

    label("loc_26E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_27B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2753")

    ChrTalk(    #157
        0xFE,
        (
            "今天的礼拜雾气缭绕，\x01",
            "真有点梦幻般的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "虽然希望雾气赶快散去，\x01",
            "天气晴起来也不错…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B3")

    label("loc_2753")


    ChrTalk(    #159
        0xFE,
        (
            "今天的礼拜雾气缭绕，\x01",
            "真有点梦幻般的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "也不错…不过\x01",
            "现在不是说那种话\x01",
            "的时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_27B3")

    Jump("loc_27FF")

    label("loc_27B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_27FF")

    ChrTalk(    #161
        0xFE,
        "空之女神爱德丝！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "请您今天也继续\x01",
            "守护洛连特的子民们吧… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FF")

    TalkEnd(0x9)
    Return()

    # Function_6_222A end

    def Function_7_2803(): pass

    label("Function_7_2803")

    OP_4A(0x9, 255)
    OP_4A(0xF, 255)

    ChrTalk(    #163
        0x9,
        (
            "接下来，\x01",
            "请向前迈出一步——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "请新郎将戒指戴到\x01",
            "新娘的左手无名指。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xF,
        "是、是的…明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        (
            "在婚礼开始之前\x01",
            "还是多练习几次比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "不然太紧张的话，\x01",
            "就算是最简单的动作也许都会失误。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x8)
    ClearChrFlags(0xF, 0x10)
    OP_4B(0x9, 255)
    OP_4B(0xF, 255)
    Return()

    # Function_7_2803 end

    def Function_8_28E5(): pass

    label("Function_8_28E5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34B, 6)), scpexpr(EXPR_END)), "loc_2954")

    ChrTalk(    #168
        0xA,
        (
            "#1060F我还有些事情，\x01",
            "要在教会再待一阵子，\x01",
            "暂时不能离开。\x02\x03",

            "艾丝蒂尔，你们\x01",
            "路上小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D60")

    label("loc_2954")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #169
        0xA,
        (
            "#1062F噢，艾丝蒂尔。\x01",
            "这次也辛苦了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1017F嗯！凯文先生也一样啊。\x02\x03",

            "真是多亏你的帮忙了，\x01",
            "缇欧她们的事……太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "#1061F哈哈～这是什么话，\x01",
            "也太见外了。\x02\x03",

            "我之所以会这么努力，\x01",
            "不全都是因为艾丝蒂尔嘛～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1008F又来了～真是个轻浮的家伙。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B53")

    ChrTalk(    #173
        0x103,
        (
            "#021F真是的，油嘴滑舌的程度\x01",
            "简直和某人不相上下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        (
            "#035F呼，说油嘴滑舌可太让我伤心了……\x02\x03",

            "#030F我一直都是很认真的呀！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1007F不用特意解释啊……\x02\x03",

            "#1011F……不、不好意思打断一下，\x01",
            "凯文先生接下来有何打算？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD6")

    label("loc_2B53")


    ChrTalk(    #176
        0x103,
        (
            "#021F真是的，油嘴滑舌的程度\x01",
            "和奥利维尔有一拼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1016F啊哈哈～这个嘛……\x02\x03",

            "#1011F话说回来，凯文先生\x01",
            "接下来有什么打算吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD6")


    ChrTalk(    #178
        0xA,
        (
            "#1068F嗯，其实还要\x01",
            "继续巡游一阵子。\x02\x03",

            "而且还有些事情…\x01",
            "需要处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1015F呼，需要处理的…事情吗。\x02\x03",

            "#1002F……看起来似乎是有\x01",
            "重要的任务啊。\x02\x03",

            "来到这里应该\x01",
            "也不是偶然吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#1064F呜……艾丝蒂尔～\x01",
            "你的感觉真是敏锐啊。\x02\x03",

            "#1066F哈，总之在这里\x01",
            "还有些事情…\x02\x03",

            "不久的将来后\x01",
            "咱们再见面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1006F嗯，好吧……\x01",
            "到时拜托了。\x02\x03",

            "那么，\x01",
            "凯文先生也要当心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        "#1062F噢，艾丝蒂尔你们也一样。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A5E)

    label("loc_2D60")

    TalkEnd(0xA)
    Return()

    # Function_8_28E5 end

    def Function_9_2D64(): pass

    label("Function_9_2D64")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D9F")

    ChrTalk(    #183
        0xFE,
        (
            "能平安回来，\x01",
            "真是要感谢女神啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDE")

    label("loc_2D9F")


    ChrTalk(    #184
        0xFE,
        (
            "多亏女神\x01",
            "才能平安回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "今后也请继续\x01",
            "守护我们吧…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2DDE")

    TalkEnd(0xB)
    Return()

    # Function_9_2D64 end

    def Function_10_2DE2(): pass

    label("Function_10_2DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DEE")
    SetChrFlags(0xC, 0x10)

    label("loc_2DEE")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2E48")

    ChrTalk(    #186
        0xFE,
        (
            "女神啊！\x01",
            "请把这雾驱散吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "看啊！！就像这样！\x01",
            "一切拜托了！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA5")

    label("loc_2E48")


    ChrTalk(    #188
        0xFE,
        (
            "暂时也没事可做了，\x01",
            "我就过来祈祷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "哈～虽然礼仪可能不对，\x01",
            "但我也是诚心在祈祷呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2EA5")

    TalkEnd(0xC)
    Return()

    # Function_10_2DE2 end

    def Function_11_2EA9(): pass

    label("Function_11_2EA9")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F25")

    ChrTalk(    #190
        0xFE,
        (
            "真是的，皮尔姆那家伙\x01",
            "还真是喜欢祈祷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "我对教会这种地方不是很熟悉，\x01",
            "每次来就这样在这里待着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD4")

    label("loc_2F25")


    ChrTalk(    #192
        0xFE,
        (
            "真是的，皮尔姆那家伙\x01",
            "还真是喜欢祈祷啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "在吃饭之前\x01",
            "一定会来礼拜堂的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "在那家伙看来，\x01",
            "一切都是因为女神的守护吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "却不想想全都多亏了\x01",
            "送他到城里的游击士。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2FD4")

    TalkEnd(0xD)
    Return()

    # Function_11_2EA9 end

    def Function_12_2FD8(): pass

    label("Function_12_2FD8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_302E")

    ChrTalk(    #196
        0xFE,
        (
            "教区长先生\x01",
            "不告诉我重要的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "嗯～那么目标\x01",
            "改为修女吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3083")

    label("loc_302E")


    ChrTalk(    #198
        0xFE,
        (
            "嗯～事情\x01",
            "应该没错…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "但教区长的话\x01",
            "不是很明白。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "把目标换为修女好了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3083")

    Jump("loc_3184")

    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_30D8")

    ChrTalk(    #201
        0xFE,
        (
            "游击士这么早\x01",
            "就开始一起行动… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "……果然是出了什么事呢!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3184")

    label("loc_30D8")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #203
        0xFE,
        "啊，艾丝蒂尔，雪拉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "这么早就\x01",
            "开始行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "呼～果然是昨夜\x01",
            "发生了什么事件吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "可不能这么悠闲了。\x01",
            "克露莎也得赶快开始采访。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3184")

    TalkEnd(0xE)
    Return()

    # Function_12_2FD8 end

    def Function_13_3188(): pass

    label("Function_13_3188")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A1")
    Call(0, 7)
    Jump("loc_3226")

    label("loc_31A1")


    ChrTalk(    #207
        0xFE,
        (
            "在这种时候举办婚礼，\x01",
            "虽然亲属们也有反对的声音，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "但还是想尽早\x01",
            "结为正式夫妇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "我和艾娅莉商量之后，\x01",
            "还是决定计划不变。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3226")

    Jump("loc_387A")

    label("loc_3229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x234, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3273")

    ChrTalk(    #210
        0xFE,
        "啊啊～艾娅莉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_3273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_32E1")

    ChrTalk(    #211
        0xFE,
        (
            "那么，游击士。\x01",
            "戒指的事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "要是发现了什么情况，\x01",
            "请再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_32E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3335")

    ChrTalk(    #213
        0xFE,
        (
            "那么，游击士。\x01",
            "戒指的事拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "要是发现了什么情况，\x01",
            "请再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D9")

    label("loc_3335")

    OP_A2(0x8)

    ChrTalk(    #215
        0xFE,
        "啊，游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "怎、怎么样了？\x01",
            "调查进行得如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#1015F嗯，还在调查中呢。\x02\x03",

            "也许再等一会\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "那、那样啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "嗯，明白了。\x01",
            "我会一直等的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D9")

    Jump("loc_384F")

    label("loc_33DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_347E")

    ChrTalk(    #220
        0xFE,
        (
            "嗯～…………\x01",
            "虽然大圣堂也很有吸引力，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "但结婚仪式还是\x01",
            "在家乡洛连特举办最好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "在初次相遇的地方进行爱的宣誓… \x01",
            "真有种神圣又纯粹的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_347E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_34D5")

    ChrTalk(    #223
        0xFE,
        "啊啊～～我可爱的艾娅莉啊～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "我要像浓雾包裹城镇那样\x01",
            "将你紧紧抱住～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_34D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3513")

    ChrTalk(    #225
        0xFE,
        "再离我近一点，艾娅莉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "我只想看你的笑脸。\x02",
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_384F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_35E1")

    ChrTalk(    #227
        0xFE,
        (
            "你那美妙的颤抖，\x01",
            "还有玫瑰花瓣一样的嘴唇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "从那里散落下来的… \x01",
            "是你我相互间的承诺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "终于…我们终于\x01",
            "能在一起了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "啊啊！光是想一想\x01",
            "就好激动！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36F6")

    label("loc_35E1")


    ChrTalk(    #231
        0xFE,
        (
            "你那美妙的颤抖，\x01",
            "还有玫瑰花瓣一样的嘴唇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "从那里散落下来的… \x01",
            "是你我相互间的承诺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "终于…我们终于\x01",
            "能在一起了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "啊～～～尽管如此……\x01",
            "女神难道没有慈悲之心吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "呼，一定是想给我们的婚姻\x01",
            "最后一次考验吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "那么一定要承受住。\x01",
            "……艾娅莉，这都是为了你。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F6")

    Jump("loc_384F")

    label("loc_36F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #237
        0xFE,
        (
            "在突然的求婚之后，\x01",
            "你那慌乱踌躇的眼神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "啊啊～～陷入遐想之后\x01",
            "那短暂的沉默…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "……即使现在想起来，\x01",
            "我的心脏也变得像要破裂了一样！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_384F")

    label("loc_37A4")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #240
        0xFE,
        "啊啊！！美丽的诞辰庆典之夜！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "艾娅莉……每次看到你的脸，\x01",
            "就会想起那个美妙的夜晚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "在星空和花火的映衬下，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "我鼓起勇气向你袒露\x01",
            "心意的那个夜晚… \x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    Jump("loc_387A")

    label("loc_3852")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3876")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_386F")
    Call(1, 1)
    Jump("loc_3873")

    label("loc_386F")

    Call(1, 0)

    label("loc_3873")

    Jump("loc_387A")

    label("loc_3876")

    Call(1, 3)

    label("loc_387A")

    TalkEnd(0xF)
    Return()

    # Function_13_3188 end

    def Function_14_387E(): pass

    label("Function_14_387E")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3912")

    ChrTalk(    #244
        0xFE,
        (
            "天堂的爸爸……\x01",
            "你能听见吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "艾娅莉…\x01",
            "马上就要做新娘了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "不久之后\x01",
            "将要穿上\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "美丽的婚纱，\x01",
            "爸爸也会喜欢的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3960")

    label("loc_3912")


    ChrTalk(    #248
        0xFE,
        (
            "天堂的爸爸……\x01",
            "艾娅莉要做新娘了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "今后也请您继续\x01",
            "在天堂上守护我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3960")

    Jump("loc_3D3B")

    label("loc_3963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_397D")

    ChrTalk(    #250
        0xFE,
        "阿鲁姆……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_397D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39DF")

    ChrTalk(    #251
        0xFE,
        "我们在这里等着。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "虽然是很艰难的委托，\x01",
            "但请努力坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_39DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3A3E")

    ChrTalk(    #253
        0xFE,
        (
            "真想在王都的大圣堂\x01",
            "举行婚礼仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "在充满回忆的地方\x01",
            "开始新的生活㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_3A3E")

    OP_A2(0x9)

    ChrTalk(    #255
        0xFE,
        (
            "和他开始做\x01",
            "结婚仪式的准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "在我看来，在王都的大圣堂\x01",
            "举行婚礼仪式啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "在充满回忆的地方\x01",
            "开始新的生活㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB8")

    Jump("loc_3D3B")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3AF0")

    ChrTalk(    #258
        0xFE,
        (
            "喂～阿鲁姆。刚刚的句子\x01",
            "有些不太美呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3B2C")

    ChrTalk(    #259
        0xFE,
        "好害羞啊，阿鲁姆……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "用那种眼神看着我…\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3D3B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #261
        0xFE,
        (
            "阿鲁姆就像小狗狗\x01",
            "一样可怜巴巴地等着我的回答，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "真是好可怜的样子…\x01",
            "所以我马上就答应了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "如今……我们终于\x01",
            "可以在一起了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "呼～这真是人生中\x01",
            "最重大的一次事件啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3BFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C9C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #265
        0xFE,
        (
            "幸福的感觉让我的胸口\x01",
            "快要爆炸了一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "我一边偷看他的表情\x01",
            "一边思考。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "呵呵～阿鲁姆那时的表情，\x01",
            "我大概一生也不会忘记呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D3B")

    label("loc_3C9C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #268
        0xFE,
        (
            "呵呵，诞辰庆典那天的事\x01",
            "我现在也仿佛历历在目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "眼前是纯白色的格兰赛尔城，\x01",
            "头上是遍布繁星的夜空…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "然后他就说出了那句\x01",
            "我期待了很久的话…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D3B")

    TalkEnd(0x10)
    Return()

    # Function_14_387E end

    def Function_15_3D3F(): pass

    label("Function_15_3D3F")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_3E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2D")

    ChrTalk(    #271
        0xFE,
        (
            "结婚仪式非常完美，\x01",
            "所以直到现在还沉浸在当时的情景中…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "还要和老公\x01",
            "在这里多待一会儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "和老公一起来礼拜堂，\x01",
            "自结婚仪式之后这好像还是第一次…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "呵呵～偶尔像现在这样见证一下\x01",
            "当时的誓言还是很有意义的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3E8B")

    label("loc_3E2D")


    ChrTalk(    #275
        0xFE,
        (
            "结婚仪式非常完美，\x01",
            "所以直到现在还沉浸在当时的情景中…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "还要和老公\x01",
            "在这里多待一会儿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E8B")

    Jump("loc_3F6A")

    label("loc_3E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_3E98")
    Jump("loc_3F6A")

    label("loc_3E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0C")

    ChrTalk(    #277
        0xFE,
        (
            "啊～不行哦。\x01",
            "到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "新娘马上就要\x01",
            "穿礼服了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "有意思的东西\x01",
            "要留到仪式结束哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3F6A")

    label("loc_3F0C")


    ChrTalk(    #280
        0xFE,
        (
            "是纯白色的礼服，\x01",
            "男方好像不怕花钱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "呵呵，果然不管怎样\x01",
            "都会想到自己的结婚仪式呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F6A")

    TalkEnd(0x14)
    Return()

    # Function_15_3D3F end

    def Function_16_3F6E(): pass

    label("Function_16_3F6E")

    TalkBegin(0x21)

    ChrTalk(    #282
        0xFE,
        (
            "哎呀～真是的，为什么\x01",
            "非要选在这种日子呢… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        (
            "我对新郎劝说过好几次，\x01",
            "让他延期举办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "但他顽固得很，\x01",
            "根本就听不进去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x21)
    Return()

    # Function_16_3F6E end

    def Function_17_3FF5(): pass

    label("Function_17_3FF5")

    TalkBegin(0x22)

    ChrTalk(    #285
        0xFE,
        (
            "阿鲁姆哥哥\x01",
            "看起来好像紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "有点担心他啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "希望不要失败……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x22)
    Return()

    # Function_17_3FF5 end

    def Function_18_4049(): pass

    label("Function_18_4049")

    TalkBegin(0x23)

    ChrTalk(    #288
        0xFE,
        (
            "结婚仪式之后准备\x01",
            "在附近的酒馆开个派对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "听说那里的料理很不错，\x01",
            "所以还蛮期待的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x23)
    Return()

    # Function_18_4049 end

    def Function_19_40AA(): pass

    label("Function_19_40AA")

    TalkBegin(0x24)

    ChrTalk(    #290
        0xFE,
        (
            "王国现在似乎\x01",
            "处于动乱的状况中啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "孙女重要的结婚仪式…\x01",
            "真希望能平安办成。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x24)
    Return()

    # Function_19_40AA end

    def Function_20_4105(): pass

    label("Function_20_4105")

    TalkBegin(0x25)

    ChrTalk(    #292
        0xFE,
        (
            "附近的主妇们\x01",
            "都来帮忙准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "洛连特的人还是\x01",
            "这么热心啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x25)
    Return()

    # Function_20_4105 end

    def Function_21_4150(): pass

    label("Function_21_4150")

    TalkBegin(0x26)

    ChrTalk(    #294
        0xFE,
        (
            "这边的房间\x01",
            "不让进去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "嗯…还想看看\x01",
            "姐姐穿礼服的样子呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x26)
    Return()

    # Function_21_4150 end

    def Function_22_419B(): pass

    label("Function_22_419B")

    TalkBegin(0x27)

    ChrTalk(    #296
        0xFE,
        (
            "艾娅莉要结婚了…\x01",
            "一开始我完全不敢相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "呼～被她抢在\x01",
            "前面了呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x27)
    Return()

    # Function_22_419B end

    def Function_23_41EC(): pass

    label("Function_23_41EC")

    TalkBegin(0x28)

    ChrTalk(    #298
        0xFE,
        (
            "来参加朋友的结婚仪式\x01",
            "虽然很高兴…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "但也替自己着急啊。\x01",
            "必须要赶快寻找目标了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x28)
    Return()

    # Function_23_41EC end

    def Function_24_4249(): pass

    label("Function_24_4249")

    TalkBegin(0x17)

    ChrTalk(    #300
        0xFE,
        (
            "啊，你们也要出席\x01",
            "结婚仪式吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "现在时间还早呢。\x01",
            "接下来新娘还要\x01",
            "试穿礼服呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x17)
    Return()

    # Function_24_4249 end

    def Function_25_42A5(): pass

    label("Function_25_42A5")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_432B")

    ChrTalk(    #302
        0xFE,
        (
            "呀～结婚仪式\x01",
            "真是让人感动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "让人不由自主得想起了\x01",
            "自己当时的经历。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "虽、虽然不是家人…\x01",
            "有些不好意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_4376")

    label("loc_432B")


    ChrTalk(    #305
        0xFE,
        "但结婚仪式真的让人感动呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "虽然不是家人，\x01",
            "但还是很替他们高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4376")

    TalkEnd(0x19)
    Return()

    # Function_25_42A5 end

    def Function_26_437A(): pass

    label("Function_26_437A")

    EventBegin(0x0)
    OP_D2(0x27020F, 0x270214, 0x2)
    OP_D2(0x27043F, 0x270442, 0x3)
    OP_D2(0x270440, 0x270443, 0x4)
    OP_D2(0x260221, 0x260226, 0x6)
    OP_D2(0x260220, 0x260225, 0x7)
    OP_D2(0x7042B, 0x7042F, 0x1B)
    OP_D2(0x703F5, 0x703F9, 0x1C)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 3)
    SetChrChipByIndex(0x2C, 4)
    OP_51(0x2A, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448B")
    Call(0, 29)
    Call(0, 30)

    label("loc_448B")

    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0x21, 0x0)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x24, 0x0)
    OP_44(0x25, 0x0)
    OP_44(0x26, 0x0)
    OP_44(0x27, 0x0)
    OP_44(0x28, 0x0)
    SetChrPos(0x10, 58450, 1000, 50290, 0)
    SetChrPos(0xF, 59530, 1000, 50290, 0)
    SetChrPos(0x8, 59000, 1000, 52160, 180)
    SetChrPos(0x9, 60720, 1000, 52500, 180)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 61680, 0, 44470, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x22, 0x4)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x23, 0x4)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x24, 0x4)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x25, 0x4)
    SetChrFlags(0x26, 0x40)
    SetChrFlags(0x26, 0x4)
    SetChrFlags(0x27, 0x40)
    SetChrFlags(0x27, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x28, 0x4)
    SetChrChipByIndex(0x23, 30)
    SetChrPos(0x21, 53270, 0, 45590, 45)
    SetChrPos(0x22, 53920, 0, 45100, 0)
    SetChrPos(0x23, 54210, 150, 45960, 0)
    SetChrPos(0x24, 61700, 150, 45960, 0)
    SetChrPos(0x25, 63570, 0, 45960, 0)
    SetChrPos(0x26, 62600, 0, 45960, 0)
    SetChrPos(0x27, 63880, 0, 44470, 0)
    SetChrPos(0x28, 62690, 10, 44470, 0)
    SetChrPos(0x101, 58510, 0, 40820, 0)
    SetChrPos(0x102, 59450, 0, 40800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46CC")
    SetChrPos(0xF8, 57880, 0, 39620, 0)
    SetChrPos(0xF9, 60090, 0, 39620, 0)
    Jump("loc_46EE")

    label("loc_46CC")

    SetChrPos(0xF9, 57880, 0, 39620, 0)
    SetChrPos(0xF8, 60090, 0, 39620, 0)

    label("loc_46EE")

    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_20(0x3E8)
    Sleep(1000)
    OP_21()
    OP_1D(0x60)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        "#1011F#1P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        (
            "#1040F#2P哈哈，似乎……\x02\x03",

            "来得正是\x01",
            "好时候呢～\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47AB():
        OP_6C(330000, 4000)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_47AB)
    OP_6D(59020, 1000, 50230, 4000)

    ChrTalk(    #309
        0x8,
        "那么──\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x8,
        (
            "接下来就是交换戒指\x01",
            "和宣誓之吻。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x1B)
    Sleep(200)
    OP_43(0x12, 0x1, 0x0, 0x1C)
    WaitChrThread(0x12, 0x1)
    Sleep(500)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    OP_8C(0xF, 270, 400)
    OP_8C(0x10, 90, 400)
    Sleep(500)

    def lambda_4839():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_4839)
    OP_94(0x0, 0x10, 0x0, 0x96, 0x1F4, 0x0)
    Sleep(500)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xB, 59030, 1000, 50240, 330)
    SetChrPos(0xD, 59300, 1000, 50400, 263)

    NpcTalk(    #311
        0xB,
        "阿鲁姆",
        "#1P艾娅莉……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #312
        0xD,
        "艾娅莉",
        "#2P阿鲁姆……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)

    def lambda_48D7():
        OP_94(0x0, 0xFE, 0x0, 0x96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_48D7)
    OP_94(0x0, 0x10, 0x0, 0x96, 0x1F4, 0x0)
    OP_62(0xF, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #313
        0x8,
        (
            "──我以伟大的创世女神\x01",
            "爱德丝之名……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x8,
        (
            "宣告你们二人从今日开始\x01",
            "结为夫妇！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Fade(1000)
    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x17, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x14, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D3D")

    ChrTalk(    #315
        0x107,
        "#067F哇～好棒啊～\x02",
    )

    CloseMessageWindow()

    label("loc_4D3D")


    ChrTalk(    #316
        0x101,
        (
            "#1017F#1P啊哈哈，还真是……\x01",
            "令人感动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x102,
        "#1053F#2P嗯……我也感觉是呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E6F")

    ChrTalk(    #318
        0x106,
        "#057F…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #319
        0x101,
        (
            "#1019F#1P阿加特……\x01",
            "为什么一直盯着新郎和新娘看啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x106,
        (
            "#552F没，你们才是……\x02\x03",

            "为什么能目不转睛的\x01",
            "看着这种令人害羞的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#1015F#1P是吗？不过我觉得这一幕很感人呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EBA")

    ChrTalk(    #322
        0x108,
        (
            "#071F哈哈～来到这里\x01",
            "也算是缘分。\x02\x03",

            "我们也来\x01",
            "祝福他们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4FAE")

    ChrTalk(    #323
        0x103,
        (
            "#025F呼～纯白的婚纱\x01",
            "真是让人向往…\x02\x03",

            "#020F那么，仪式虽然完毕了，\x01",
            "但接下来才是高潮部分！\x02\x03",

            "请新郎新娘退场，\x01",
            "马上去外边！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #324
        0x101,
        "#1011F#1P？？？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #325
        0x102,
        (
            "#1040F#2P啊啊～是这样啊……\x02\x03",

            "这可是身为女性\x01",
            "绝对不能错过的事件啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FAE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0100   ._SN", 117, 0, 0)
    IdleLoop()
    Return()

    # Function_26_437A end

    def Function_27_4FC6(): pass

    label("Function_27_4FC6")

    OP_8E(0xFE, 0xED30, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEBD2, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8C(0xF, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xF, 0, 400)
    OP_8E(0xFE, 0xED30, 0x3E8, 0xCD14, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_27_4FC6 end

    def Function_28_5024(): pass

    label("Function_28_5024")

    OP_8E(0xFE, 0xE146, 0x3E8, 0xC472, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_8C(0x10, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8C(0x10, 0, 400)
    OP_8E(0xFE, 0xE146, 0x0, 0xBEF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_5024 end

    def Function_29_5075(): pass

    label("Function_29_5075")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_50F2"),
        (1, "loc_50F8"),
        (SWITCH_DEFAULT, "loc_50FE"),
    )


    label("loc_50F2")

    OP_A2(0x1200)
    Jump("loc_50FE")

    label("loc_50F8")

    OP_A2(0x1201)
    Jump("loc_50FE")

    label("loc_50FE")

    Return()

    # Function_29_5075 end

    def Function_30_50FF(): pass

    label("Function_30_50FF")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_30_50FF end

    SaveToFile()

Try(main)
