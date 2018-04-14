from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '普利亚姆',                             # 9
        '爱玲',                                 # 10
        '列曼',                                 # 11
        '冈多夫',                               # 12
        '阿利瑟',                               # 13
        '温丝',                                 # 14
        '雷伊',                                 # 15
        '玛多克工房长',                         # 16
        '格斯塔夫维修长',                       # 17
        '市民',                                 # 18
        '市民',                                 # 19
        '市民',                                 # 20
        '市民',                                 # 21
        '市民',                                 # 22
        '市民',                                 # 23
        '市民',                                 # 24
        '市民',                                 # 25
        '市民',                                 # 26
        '市民',                                 # 27
        '市民',                                 # 28
        '市民',                                 # 29
        '市民',                                 # 30
        '市民',                                 # 31
        '市民',                                 # 32
        '市民',                                 # 33
        '市民',                                 # 34
        '市民',                                 # 35
        '市民',                                 # 36
        '市民',                                 # 37
        '市民',                                 # 38
        '市民',                                 # 39
        '市民',                                 # 40
        '市民',                                 # 41
        '市民',                                 # 42
        ' ',                                    # 43
        '斯坦因',                               # 44
        '康丝坦茨',                             # 45
        '蔡斯飞船坪',                           # 46
        '蔡斯市·市区',                         # 47
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01450 ._CH',             # 02
        'ED6_DT07/CH01750 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01470 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH02620 ._CH',             # 07
        'ED6_DT07/CH02440 ._CH',             # 08
        'ED6_DT07/CH01100 ._CH',             # 09
        'ED6_DT07/CH01110 ._CH',             # 0A
        'ED6_DT07/CH01120 ._CH',             # 0B
        'ED6_DT07/CH01200 ._CH',             # 0C
        'ED6_DT07/CH01210 ._CH',             # 0D
        'ED6_DT07/CH01290 ._CH',             # 0E
        'ED6_DT07/CH01160 ._CH',             # 0F
        'ED6_DT07/CH01170 ._CH',             # 10
        'ED6_DT07/CH01180 ._CH',             # 11
        'ED6_DT07/CH01490 ._CH',             # 12
        'ED6_DT07/CH01250 ._CH',             # 13
        'ED6_DT07/CH01270 ._CH',             # 14
        'ED6_DT07/CH01290 ._CH',             # 15
        'ED6_DT07/CH01680 ._CH',             # 16
        'ED6_DT07/CH01690 ._CH',             # 17
        'ED6_DT07/CH01200 ._CH',             # 18
        'ED6_DT07/CH01230 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01450P._CP',             # 02
        'ED6_DT07/CH01750P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01470P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH02620P._CP',             # 07
        'ED6_DT07/CH02440P._CP',             # 08
        'ED6_DT07/CH01100P._CP',             # 09
        'ED6_DT07/CH01110P._CP',             # 0A
        'ED6_DT07/CH01120P._CP',             # 0B
        'ED6_DT07/CH01200P._CP',             # 0C
        'ED6_DT07/CH01210P._CP',             # 0D
        'ED6_DT07/CH01290P._CP',             # 0E
        'ED6_DT07/CH01160P._CP',             # 0F
        'ED6_DT07/CH01170P._CP',             # 10
        'ED6_DT07/CH01180P._CP',             # 11
        'ED6_DT07/CH01490P._CP',             # 12
        'ED6_DT07/CH01250P._CP',             # 13
        'ED6_DT07/CH01270P._CP',             # 14
        'ED6_DT07/CH01290P._CP',             # 15
        'ED6_DT07/CH01680P._CP',             # 16
        'ED6_DT07/CH01690P._CP',             # 17
        'ED6_DT07/CH01200P._CP',             # 18
        'ED6_DT07/CH01230P._CP',             # 19
    )

    DeclNpc(
        X                   = -26340,
        Z                   = 8000,
        Y                   = 65489,
        Direction           = 74,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -18800,
        Z                   = 8000,
        Y                   = 64430,
        Direction           = 164,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -24430,
        Z                   = 8000,
        Y                   = 68160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24460,
        Z                   = 8000,
        Y                   = 67320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -14900,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -16239,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -19310,
        Z                   = 8000,
        Y                   = 60470,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        ChipIndex           = 0xC,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -48400,
        Z                   = 25180,
        Y                   = 59290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -41320,
        Z                   = 22000,
        Y                   = 50520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -23030,
        Z                   = 8000,
        Y                   = 86970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 28060,
        Z                   = 8000,
        Y                   = 58980,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -35690,
        Y                   = 9750,
        Z                   = 58940,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = -23010,
        Y                   = 7750,
        Z                   = 74850,
        Range               = 1500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )


    DeclActor(
        TriggerX            = -52000,
        TriggerZ            = 25000,
        TriggerY            = 59710,
        TriggerRange        = 1700,
        ActorX              = -52000,
        ActorZ              = 26000,
        ActorY              = 59710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6BE",          # 00, 0
        "Function_1_78F",          # 01, 1
        "Function_2_839",          # 02, 2
        "Function_3_86F",          # 03, 3
        "Function_4_D08",          # 04, 4
        "Function_5_11D5",         # 05, 5
        "Function_6_157D",         # 06, 6
        "Function_7_1C78",         # 07, 7
        "Function_8_1DE7",         # 08, 8
        "Function_9_229D",         # 09, 9
        "Function_10_247D",        # 0A, 10
        "Function_11_25A5",        # 0B, 11
        "Function_12_27E9",        # 0C, 12
        "Function_13_2B9D",        # 0D, 13
        "Function_14_2D07",        # 0E, 14
        "Function_15_2D49",        # 0F, 15
        "Function_16_2D8B",        # 10, 16
        "Function_17_2DCD",        # 11, 17
        "Function_18_2E17",        # 12, 18
        "Function_19_2E66",        # 13, 19
        "Function_20_2E94",        # 14, 20
        "Function_21_2E98",        # 15, 21
    )


    def Function_0_6BE(): pass

    label("Function_0_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_707")
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -49500, 25000, 57820, 270)
    OP_8C(0x2B, 270, 0)
    SetChrPos(0x2C, -45970, 25180, 58340, 270)
    ClearChrFlags(0x2C, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_704")

    label("loc_704")

    Jump("loc_777")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_720")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_777")

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_743")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_777")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_75C")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_777")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_777")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_78E")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_78E")

    Return()

    # Function_0_6BE end

    def Function_1_78F(): pass

    label("Function_1_78F")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x230052)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_809")
    OP_6F(0x0, 59)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 59)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_76(0xFF, 0x21, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_10(0x4, 0x0)
    Jump("loc_82C")

    label("loc_809")

    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x2A, 0x0, 0x0, 0x2)

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_838")
    OP_64(0x0, 0x1)

    label("loc_838")

    Return()

    # Function_1_78F end

    def Function_2_839(): pass

    label("Function_2_839")

    OP_72(0x5, 0x20)
    OP_72(0x4, 0x20)

    label("loc_843")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86E")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_843")

    label("loc_86E")

    Return()

    # Function_2_839 end

    def Function_3_86F(): pass

    label("Function_3_86F")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88C")
    OP_A9(0x9C)
    TalkEnd(0x8)
    Return()

    label("loc_88C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89D")
    TalkEnd(0x8)
    Return()

    label("loc_89D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_9AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_950")

    ChrTalk(    #0
        0xFE,
        (
            "呀，欢迎。\x01",
            "来点冷饮怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "我听说了，\x01",
            "导力器的恢复装置\x01",
            "现在导力机能全部丧失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "在这种时候更需要饮料！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "来喝一瓶吧！\x01",
            "恢复体力是很重要的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9A9")

    label("loc_950")


    ChrTalk(    #4
        0xFE,
        "在这种时候更需要饮料！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "不管是滋补强身型还是营养补充型，\x01",
            "各种饮料我这里都有哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A9")

    Jump("loc_D04")

    label("loc_9AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50")

    ChrTalk(    #6
        0xFE,
        (
            "导力器停止运转的时候\x01",
            "引起了很大骚乱，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "工房长虽然拼命解释说明，\x01",
            "但还是无法平息大家的不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我也一样，连卖饮料\x01",
            "的心情都受影响了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A9B")

    label("loc_A50")


    ChrTalk(    #9
        0xFE,
        "之前的骚乱真是不得了，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "大家都围在一起，\x01",
            "工房长简直都快哭出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9B")

    Jump("loc_D04")

    label("loc_A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AEF")

    ChrTalk(    #11
        0xFE,
        (
            "工房船刚才\x01",
            "开走了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "好像有好几个研究员\x01",
            "乘坐在上面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B30")

    label("loc_AEF")


    ChrTalk(    #13
        0xFE,
        (
            "工房船刚才\x01",
            "开走了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "似乎已经很久\x01",
            "没看见那艘船了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B30")

    Jump("loc_D04")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B88")

    ChrTalk(    #15
        0xFE,
        (
            "工房船似乎已经\x01",
            "开始准备出港了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "目的地好像是\x01",
            "雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_B88")


    ChrTalk(    #17
        0xFE,
        (
            "工房船似乎已经\x01",
            "开始准备出港了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "列曼那家伙也\x01",
            "充满干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "看来一定是很\x01",
            "重要的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BF0")

    Jump("loc_D04")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_C3F")

    ChrTalk(    #20
        0xFE,
        (
            "哟～辛苦了。\x01",
            "要喝点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "这里也有很多\x01",
            "保健型饮品哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C99")

    ChrTalk(    #22
        0x8,
        "呼～地震时真是吓了一跳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "在受惊的时候\x01",
            "只要喝点饮料就会平静了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D04")

    label("loc_C99")


    ChrTalk(    #24
        0x8,
        "呼～地震时真是吓了一跳。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "在受惊的时候\x01",
            "只要喝点饮料就会平静了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "所以啦，\x01",
            "要不要喝点冷饮？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D04")

    TalkEnd(0x8)
    Return()

    # Function_3_86F end

    def Function_4_D08(): pass

    label("Function_4_D08")

    TalkBegin(0x9)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    OP_A9(0x9D)
    TalkEnd(0x9)
    Return()

    label("loc_D25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D36")
    TalkEnd(0x9)
    Return()

    label("loc_D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(    #27
        0xFE,
        (
            "啊，欢迎光临。\x01",
            "要买花吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "就算着急\x01",
            "也没有任何用，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "在这样的时候\x01",
            "就更想看花了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_DF6")

    label("loc_DA8")


    ChrTalk(    #30
        0xFE,
        (
            "就算着急\x01",
            "也是没用的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "所以，倒不如专心插花，\x01",
            "还能让心情变得平静些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF6")

    Jump("loc_11D1")

    label("loc_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E83")

    ChrTalk(    #32
        0xFE,
        (
            "中央工房的骚乱\x01",
            "非常可怕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "城里的居民们\x01",
            "似乎都来势汹汹…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "……那样的事情，\x01",
            "真希望不要再发生第二次了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_EA4")

    label("loc_E83")


    ChrTalk(    #35
        0xFE,
        (
            "中央工房的骚乱\x01",
            "非常可怕……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA4")

    Jump("loc_11D1")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_F81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F02")

    ChrTalk(    #36
        0xFE,
        (
            "本想让繁忙的他们\x01",
            "多欣赏欣赏花草的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "呼～看来要\x01",
            "更加努力才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F7E")

    label("loc_F02")


    ChrTalk(    #38
        0xFE,
        (
            "中央工房的人们\x01",
            "好像总是那么忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "本想让繁忙的他们\x01",
            "多看看花，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "唉，却总是从门前路过\x01",
            "从不留步看看。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F7E")

    Jump("loc_11D1")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_103F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FF2")

    ChrTalk(    #41
        0xFE,
        (
            "如果地方不大的话\x01",
            "推荐选用小一些的花来摆放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "在有限的空间内装饰\x01",
            "多种颜色的花也很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103C")

    label("loc_FF2")


    ChrTalk(    #43
        0xFE,
        (
            "最近稍许素雅些的\x01",
            "小型花很受欢迎哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "已经变成了花坛中的主角。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_103C")

    Jump("loc_11D1")

    label("loc_103F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(    #45
        0xFE,
        (
            "除了观赏用的花之外，\x01",
            "还有在制作料理中使用的花哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "如果有兴趣的话\x01",
            "请一定要试一次。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_112E")

    label("loc_10AC")


    ChrTalk(    #47
        0xFE,
        (
            "欢迎光临。\x01",
            "插花是很有意思的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "除了观赏用的花之外，\x01",
            "还有在制作料理中使用的花哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "如果有兴趣的话\x01",
            "请一定要试一次。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_112E")

    Jump("loc_11D1")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_11D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1186")

    ChrTalk(    #50
        0x9,
        (
            "飞船坪那边\x01",
            "好像震得相当厉害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "在这里都能听得到\x01",
            "惨叫声呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D1")

    label("loc_1186")


    ChrTalk(    #52
        0x9,
        (
            "还好……\x01",
            "商品全都没事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "已经好久没有过地震了，\x01",
            "真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11D1")

    TalkEnd(0x9)
    Return()

    # Function_4_D08 end

    def Function_5_11D5(): pass

    label("Function_5_11D5")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_132C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_127C")

    ChrTalk(    #54
        0xFE,
        (
            "听说军队的警备艇\x01",
            "好像也有一些紧急迫降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "以时间来看的话，\x01",
            "也许工房船也会有同样遭遇吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "那么一想的话，\x01",
            "也许我们还算是幸运的了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1329")

    label("loc_127C")


    ChrTalk(    #57
        0xFE,
        (
            "听说军队的警备艇\x01",
            "好像也有一些紧急迫降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "工房船如果遇到相同遭遇的话，\x01",
            "也许后果就不堪设想了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "因为工房船和警备艇的性格构造是不同的，\x01",
            "没办法进行那种安全着陆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1329")

    Jump("loc_1579")

    label("loc_132C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AA")

    ChrTalk(    #60
        0xFE,
        (
            "工房船还没有从船库\x01",
            "中出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "现在还在\x01",
            "整备状态中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "因为我是操舵手，\x01",
            "那些事不是我负责的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1400")

    label("loc_13AA")


    ChrTalk(    #63
        0xFE,
        (
            "导力引擎可不是\x01",
            "普通的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "要是有诗人在的话，\x01",
            "一定会把机翼比作鸟的翅膀吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1400")

    Jump("loc_1579")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_14DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_145C")

    ChrTalk(    #65
        0xFE,
        (
            "新型引擎和\x01",
            "『埃尔赛尤』的组合吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "光是想想就要让人\x01",
            "流鼻血了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DC")

    label("loc_145C")


    ChrTalk(    #67
        0xFE,
        (
            "说到最近的重要工作，\x01",
            "那就是『埃尔赛尤』的主机换装了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "新型的引擎\x01",
            "要装载上去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "接下来要去雷斯顿要塞\x01",
            "进行工事。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14DC")

    Jump("loc_1579")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1579")

    ChrTalk(    #70
        0xFE,
        (
            "呼～不管怎么说，地震在\x01",
            "船降落后才发生真是幸运。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "如果是在降落的瞬间震动\x01",
            "那后果就严重了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "驾驶定期船的那些人\x01",
            "现在大概也是满手冷汗吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1579")

    TalkEnd(0xA)
    Return()

    # Function_5_11D5 end

    def Function_6_157D(): pass

    label("Function_6_157D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 1)), scpexpr(EXPR_END)), "loc_15C8")

    ChrTalk(    #73
        0xFE,
        (
            "军队的委托\x01",
            "就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "到了王都那边\x01",
            "也要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C74")

    label("loc_15C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18BE")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #75
        0xFE,
        "喔！这不是阿加特吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        "#052F冈多夫，你回来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "嘿嘿，刚刚回来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "每次都把烂摊子留给你，\x01",
            "真是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(    #79
        0xFE,
        (
            "还有那位小姐，\x01",
            "也多亏你的帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "艾丝蒂尔·布莱特的\x01",
            "事迹我可是一直都有所耳闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "现在说这个可能有些晚了，\x01",
            "不过还是祝贺你晋升为正游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1008F嘿嘿嘿，谢谢啦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "不过，经常会和那么危险\x01",
            "的事件有关啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "算了，反正也已经\x01",
            "习惯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "……对了。\x01",
            "你们要离开蔡斯了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1006F嗯，接下来要去王都了。\x02\x03",

            "王国军\x01",
            "发来了正式委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #87
        0xFE,
        "嘿，军队的委托？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "我来的时候\x01",
            "怎么就没有那种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x106,
        "#050F看来是凑巧了吧，\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #90
        0xFE,
        "没赶对时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "也好，那边就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #92
        0xFE,
        (
            "那么，在王都也\x01",
            "也要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1001F嗯，再见啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C71")

    label("loc_18BE")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #94
        0xFE,
        (
            "哦，还以为是谁呢，\x01",
            "那不是雪拉扎德吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x103,
        (
            "#023F冈多夫？\x02\x03",

            "你已经回蔡斯了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "嘿嘿，刚刚回来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "呀～不管怎样，\x01",
            "真是好久没见啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "看样子你比以前\x01",
            "又老练了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        (
            "#021F呵呵，谢谢。\x02\x03",

            "#027F呵呵，说好话也没礼物给你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "呵呵，帮我分担这么多工作就够了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "最近经常出去办事，\x01",
            "总是担心谁在负责蔡斯的事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(    #102
        0xFE,
        (
            "这位小姐也是\x01",
            "帮了不少忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "艾丝蒂尔·布莱特的\x01",
            "事迹我可是一直都有所耳闻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "现在说这个可能有些晚了，\x01",
            "不过还是祝贺你晋升为正游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1008F嘿嘿嘿，谢谢啦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "不过，经常会和那么危险\x01",
            "的事件有关啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "算了，反正也已经\x01",
            "习惯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "……对了。\x01",
            "你们要离开蔡斯了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1006F嗯，接下来要去王都了。\x02\x03",

            "王国军\x01",
            "发来了正式委托。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #110
        0xFE,
        "嘿，军队的委托？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "我来的时候\x01",
            "怎么就没有那种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#023F……好像是搞错了吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #113
        0xFE,
        "没赶对时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "也好，那边就\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xFE,
        (
            "那么，在王都也\x01",
            "也要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1001F嗯，再见啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1C71")

    OP_A2(0x1641)

    label("loc_1C74")

    TalkEnd(0xB)
    Return()

    # Function_6_157D end

    def Function_7_1C78(): pass

    label("Function_7_1C78")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CE4")

    ChrTalk(    #117
        0xFE,
        (
            "我家的阳台已经\x01",
            "没有放花坛的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "嗯～要是再放新花坛的话\x01",
            "就要准备新架子了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2F")

    label("loc_1CE4")


    ChrTalk(    #119
        0xFE,
        (
            "可以只用小型花朵\x01",
            "插载盆景哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "嗯～可是阳台已经\x01",
            "没有地方放了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D2F")

    Jump("loc_1DE3")

    label("loc_1D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1D93")

    ChrTalk(    #121
        0xFE,
        (
            "柔弱可怜的小型花朵\x01",
            "也是很可爱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "呵呵呵～简直就像是\x01",
            "年轻时的我一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE3")

    label("loc_1D93")


    ChrTalk(    #123
        0xFE,
        "哇，这个也很可爱。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "虽然大朵的花很漂亮，\x01",
            "不过小型的花也是很可爱的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1DE3")

    TalkEnd(0xC)
    Return()

    # Function_7_1C78 end

    def Function_8_1DE7(): pass

    label("Function_8_1DE7")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB7")

    ChrTalk(    #125
        0xFE,
        (
            "那么巨大的东西\x01",
            "是怎么浮在天上的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "也许是和飞船一样\x01",
            "装载了导力引擎吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "……虽然是这么想，\x01",
            "但仔细思考一下的话还是不可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "再怎么强的导力器也\x01",
            "不可能有那么强的性能。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1F1B")

    label("loc_1EB7")


    ChrTalk(    #129
        0xFE,
        (
            "那个东西能浮在天上，\x01",
            "原理应该和飞船完全不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "不管怎么说，导力引擎\x01",
            "不可能有那么强的性能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1B")

    Jump("loc_2299")

    label("loc_1F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_202F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC2")

    ChrTalk(    #131
        0xFE,
        "也是很厉害的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "那个浮游物体一定\x01",
            "是超越我们常识范围了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "通过距离也许可以\x01",
            "推算出它的大小吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "不过那就要靠王国军\x01",
            "来调查了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_202C")

    label("loc_1FC2")


    ChrTalk(    #135
        0xFE,
        (
            "那个浮游物体一定\x01",
            "是超越我们常识范围内的存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "只要测算出它的距离\x01",
            "应该就可以知道它的具体大小了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202C")

    Jump("loc_2299")

    label("loc_202F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2072")

    ChrTalk(    #137
        0xFE,
        (
            "妈妈已经忘记当初\x01",
            "的目的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "地震对策怎么样了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2299")

    label("loc_2072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_222B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20CD")

    ChrTalk(    #139
        0xFE,
        (
            "拉赛尔博士的发明\x01",
            "总是很惊人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "他的做事效率\x01",
            "一般人实在比不了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2228")

    label("loc_20CD")

    TurnDirection(0xD, 0x107, 0)

    ChrTalk(    #141
        0xFE,
        "啊～提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "那之后好久不见了。\x01",
            "上次主日学校之后就一直没见面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        (
            "#560F好久不见，温丝。\x02\x03",

            "和妈妈来买东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "嗯，是呀！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "提妲\x01",
            "今天也在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x107,
        (
            "#060F嗯，我们正要去设置\x01",
            "最新的测量仪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "是拉赛尔博士的新发明吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "等下次在主日学校见面的时候\x01",
            "再详细给我介绍吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "那么，下次见啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        "#061F啊，嗯，下次见！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2228")

    Jump("loc_2299")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_225B")

    ChrTalk(    #151
        0xFE,
        (
            "妈妈最近只栽种\x01",
            "那个品种。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2299")

    label("loc_225B")


    ChrTalk(    #152
        0xFE,
        "妈妈，请想一想吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "改变花坛配置\x01",
            "是为了防止地震。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2299")

    TalkEnd(0xD)
    Return()

    # Function_8_1DE7 end

    def Function_9_229D(): pass

    label("Function_9_229D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_236F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_22F7")

    ChrTalk(    #154
        0xFE,
        (
            "呵呵～目标\x01",
            "已经定下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "呵呵，回去以后\x01",
            "马上准备必要材料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236C")

    label("loc_22F7")


    ChrTalk(    #156
        0xFE,
        (
            "呼～接下来准备构想\x01",
            "种植在温室的作物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "它的目的是『净化心灵』，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "让人们心情平衡。\x01",
            "一定会很受欢迎的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_236C")

    Jump("loc_2479")

    label("loc_236F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2479")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_23C7")

    ChrTalk(    #159
        0xFE,
        "原来如此，观赏用吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "那确实也是人类喜爱植物\x01",
            "的一个理由呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2479")

    label("loc_23C7")


    ChrTalk(    #161
        0xFE,
        "嗯，观赏用的花吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "摆上一盆，让研究室充满生机\x01",
            "似乎也不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "嗯，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "以观赏用为视点\x01",
            "似乎很有意思呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "那确实也是人类喜爱植物\x01",
            "的一个理由呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2479")

    TalkEnd(0xE)
    Return()

    # Function_9_229D end

    def Function_10_247D(): pass

    label("Function_10_247D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #166
        0xFE,
        (
            "那个浮游物体出现的时候，\x01",
            "据说天空闪耀着金色的光辉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "从七耀石的属性来说的话，\x01",
            "金是象征着『空间』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "嗯，两者之间\x01",
            "应该有什么关联吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A1")

    label("loc_2526")


    ChrTalk(    #169
        0xFE,
        (
            "我听说出现了奇怪的物体\x01",
            "才特意来这里看……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "但没想到竟然是\x01",
            "这么巨大的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "利贝尔王国内究竟\x01",
            "发生了什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A1")

    TalkEnd(0xFE)
    Return()

    # Function_10_247D end

    def Function_11_25A5(): pass

    label("Function_11_25A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_26C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2682")

    ChrTalk(    #172
        0xFE,
        (
            "本以为再过不久就是\x01",
            "世界末日了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "……距离黄昏似乎\x01",
            "还有一段时间哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "还是回去拿一下\x01",
            "遮阳伞吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "长期遭受日晒的话\x01",
            "皮肤会变差的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "就算是要到另一个世界\x01",
            "也要以最美的状态过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_26C4")

    label("loc_2682")


    ChrTalk(    #177
        0xFE,
        (
            "看来世界末日\x01",
            "还没有降临呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "还是回去拿一下\x01",
            "遮阳伞吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C4")

    Jump("loc_27E5")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_27E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_276B")

    ChrTalk(    #179
        0xFE,
        (
            "天空中漂浮着那种东西时\x01",
            "还去工作的话简直就是傻瓜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "世界的末日大概\x01",
            "已经不远了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "在人生的尽头还在工作岗位上的话\x01",
            "那也实在太逊了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_27E5")

    label("loc_276B")


    ChrTalk(    #182
        0xFE,
        (
            "天空中漂浮着那种东西时\x01",
            "还去工作的话简直就是傻瓜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "那些整天只懂埋头工作的人，\x01",
            "真正重要的东西他们都完全看不见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E5")

    TalkEnd(0xFE)
    Return()

    # Function_11_25A5 end

    def Function_12_27E9(): pass

    label("Function_12_27E9")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    SetChrPos(0xF, -35290, 10000, 59780, 90)
    SetChrPos(0x10, -35230, 10000, 58160, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -33900, 10000, 56360, 331)
    SetChrPos(0x8, -32920, 10000, 61360, 211)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    SetChrPos(0x11, -33530, 10000, 57330, 270)
    SetChrPos(0x12, -33050, 10000, 58910, 270)
    SetChrPos(0x13, -33880, 10000, 61340, 225)
    SetChrPos(0x14, -32500, 10000, 60280, 270)
    SetChrPos(0x15, -32360, 10000, 57680, 270)
    SetChrPos(0x16, -31130, 9500, 59060, 270)
    SetChrPos(0x17, -30660, 9000, 60320, 270)
    SetChrPos(0x18, -30670, 9250, 57500, 270)
    SetChrPos(0x19, -29220, 8000, 58710, 270)
    SetChrPos(0x1A, -29090, 8000, 60610, 270)
    SetChrPos(0x1B, -27830, 8000, 57460, 270)
    SetChrPos(0x1C, -27220, 8000, 59380, 270)
    SetChrPos(0x1D, -27240, 8000, 61340, 225)
    SetChrPos(0x1E, -25050, 8000, 57430, 270)
    SetChrPos(0x1F, -23040, 8000, 59720, 270)
    SetChrPos(0x20, -22340, 8000, 61820, 270)
    SetChrPos(0x21, -21800, 8000, 56830, 315)
    SetChrPos(0x22, -23720, 8000, 58160, 270)
    SetChrPos(0x23, -20480, 8000, 59330, 270)
    SetChrPos(0x24, -19770, 8000, 57860, 270)
    SetChrPos(0x25, -25080, 8000, 60640, 270)
    SetChrPos(0x26, -23770, 8000, 55620, 315)
    SetChrPos(0x27, -8950, 7510, 56760, 270)
    SetChrPos(0x28, -7210, 6760, 56690, 270)
    SetChrPos(0x29, -7900, 7010, 61680, 270)
    ClearChrFlags(0x11, 0x80)
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
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6D(-14360, 8000, 59650, 0)
    OP_67(0, 8840, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(299000, 0)
    OP_6E(455, 0)
    OP_43(0xF, 0x1, 0x0, 0x11)
    OP_43(0x10, 0x1, 0x0, 0x12)
    OP_43(0x27, 0x0, 0x0, 0xE)
    OP_43(0x28, 0x0, 0x0, 0xF)
    OP_43(0x29, 0x0, 0x0, 0x10)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_C8(0x200, 0x46, "C_PLAC23._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_2B38():
        OP_6D(-35500, 10000, 59580, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B38)

    def lambda_2B50():
        OP_67(0, 7230, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2B50)

    def lambda_2B68():
        OP_6C(314000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2B68)
    OP_6E(513, 7000)
    Sleep(1000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R0203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_27E9 end

    def Function_13_2B9D(): pass

    label("Function_13_2B9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D06")
    OP_62(0x11, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x1B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x20, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x25, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x17, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x21, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x26, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x18, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x22, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x19, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x23, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sleep(500)
    OP_62(0x15, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_62(0x24, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sleep(500)
    Jump("Function_13_2B9D")

    label("loc_2D06")

    Return()

    # Function_13_2B9D end

    def Function_14_2D07(): pass

    label("Function_14_2D07")

    OP_8E(0xFE, 0xFFFFD08A, 0x1F40, 0xDE58, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBDB6, 0x1F40, 0xE31C, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Return()

    # Function_14_2D07 end

    def Function_15_2D49(): pass

    label("Function_15_2D49")

    OP_8E(0xFE, 0xFFFFD08A, 0x1F40, 0xDE58, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFB3AC, 0x1F40, 0xDB2E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Return()

    # Function_15_2D49 end

    def Function_16_2D8B(): pass

    label("Function_16_2D8B")

    OP_8E(0xFE, 0xFFFFD044, 0x1F40, 0xF0C8, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFB24E, 0x1F40, 0xEC5E, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Return()

    # Function_16_2D8B end

    def Function_17_2DCD(): pass

    label("Function_17_2DCD")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2DDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E16")
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_2DDF")

    label("loc_2E16")

    Return()

    # Function_17_2DCD end

    def Function_18_2E17(): pass

    label("Function_18_2E17")

    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    label("loc_2E2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E65")
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Jump("loc_2E2E")

    label("loc_2E65")

    Return()

    # Function_18_2E17 end

    def Function_19_2E66(): pass

    label("Function_19_2E66")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400D0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_19_2E66 end

    def Function_20_2E94(): pass

    label("Function_20_2E94")

    SetPlaceName(0x85)
    Return()

    # Function_20_2E94 end

    def Function_21_2E98(): pass

    label("Function_21_2E98")

    SetPlaceName(0x81)
    Return()

    # Function_21_2E98 end

    SaveToFile()

Try(main)
