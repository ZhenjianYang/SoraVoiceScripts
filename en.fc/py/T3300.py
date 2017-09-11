from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3300   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3300   ._SN',
            'ED6_DT01/T3300_1 ._SN',
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
        'Gary',                                 # 9
        'Wong',                                 # 10
        'Bruno',                                # 11
        'Private Brahm',                        # 12
        'Private Henning',                      # 13
        'CWO Pace',                             # 14
        'Warrant Officer Gerwin',               # 15
        'Rufus',                                # 16
        'Chicken',                              # 17
        'Chicken',                              # 18
        'Chicken',                              # 19
        'Chicken',                              # 20
        'Tratt Plains Road',                    # 21
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
        'ED6_DT07/CH01530 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01270 ._CH',             # 07
        'ED6_DT07/CH01720 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
        'ED6_DT07/CH01530P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01270P._CP',             # 07
        'ED6_DT07/CH01720P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 0,
        Y                   = 18540,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1990,
        Z                   = -500,
        Y                   = -280,
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


    DeclActor(
        TriggerX            = 8039,
        TriggerZ            = 0,
        TriggerY            = 21240,
        TriggerRange        = 1500,
        ActorX              = 8039,
        ActorZ              = 2000,
        ActorY              = 21240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_53F",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_5BE",          # 03, 3
        "Function_4_5E2",          # 04, 4
        "Function_5_606",          # 05, 5
        "Function_6_754",          # 06, 6
        "Function_7_8A2",          # 07, 7
        "Function_8_92E",          # 08, 8
        "Function_9_954",          # 09, 9
        "Function_10_119E",        # 0A, 10
        "Function_11_12BC",        # 0B, 11
        "Function_12_12C3",        # 0C, 12
        "Function_13_1907",        # 0D, 13
        "Function_14_190E",        # 0E, 14
        "Function_15_2236",        # 0F, 15
        "Function_16_23D3",        # 10, 16
        "Function_17_2898",        # 11, 17
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2C0")
    Jump("loc_3B6")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FD")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 11760, 20, 31780, 236)
    OP_43(0x8, 0x0, 0x0, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 7490, -60, 24130, 273)
    Jump("loc_3B6")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_3B6")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_311")
    Jump("loc_3B6")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_331")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11890, 0, 41360, 226)
    Jump("loc_3B6")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 11890, 0, 41360, 226)
    Jump("loc_3B6")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38E")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 13100, 0, 38170, 53)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16420, 0, 38700, 351)

    label("loc_38E")

    Jump("loc_3B6")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_39B")
    Jump("loc_3B6")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3A5")
    Jump("loc_3B6")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3AF")
    Jump("loc_3B6")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B6")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3FC")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_41C")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    Jump("loc_53E")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_478")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6340, 0, 48700, 159)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4BE")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)
    Jump("loc_53E")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4FB")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1000, 0, 48690, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F8")
    OP_44(0xB, 0xFF)
    SetChrFlags(0xB, 0x10)

    label("loc_4F8")

    Jump("loc_53E")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53E")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 790, 0, 48280, 180)
    SetChrFlags(0xB, 0x10)
    OP_44(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7370, 5500, 49600, 74)
    OP_43(0xE, 0x0, 0x0, 0x4)

    label("loc_53E")

    Return()

    # Function_0_2B6 end

    def Function_1_53F(): pass

    label("Function_1_53F")

    OP_16(0x2, 0xFA0, 0xFFFE1BA0, 0xFFFEB7E0, 0x30055)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_560")
    OP_71(0x4, 0x4)
    Jump("loc_593")

    label("loc_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_56A")
    Jump("loc_593")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_574")
    Jump("loc_593")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_58E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B")
    OP_71(0x4, 0x4)

    label("loc_58B")

    Jump("loc_593")

    label("loc_58E")

    OP_71(0x4, 0x4)

    label("loc_593")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_28(0x2A, 0x1, 0x1000)

    label("loc_5A7")

    Return()

    # Function_1_53F end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5A8")

    label("loc_5BD")

    Return()

    # Function_2_5A8 end

    def Function_3_5BE(): pass

    label("Function_3_5BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5E1")
    OP_8D(0xFE, 8640, 35670, 14490, 27640, 2000)
    Jump("Function_3_5BE")

    label("loc_5E1")

    Return()

    # Function_3_5BE end

    def Function_4_5E2(): pass

    label("Function_4_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_605")
    OP_8D(0xFE, -9410, 54290, -4840, 47630, 2000)
    Jump("Function_4_5E2")

    label("loc_605")

    Return()

    # Function_4_5E2 end

    def Function_5_606(): pass

    label("Function_5_606")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -4320, 30420, 16309, 38200, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_62F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_753")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x10E0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x76D4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x3FB5), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x9538), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ED")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_6DA():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6DA)
    Jump("loc_710")

    label("loc_6ED")


    def lambda_6F3():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F3)
    Sleep(200)

    label("loc_710")

    Sleep(30)
    Jump("loc_750")

    label("loc_718")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_750")
    OP_44(0xFE, 0x2)

    def lambda_738():
        OP_8D(0xFE, -4320, 30420, 16309, 38200, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_738)

    label("loc_750")

    Jump("loc_62F")

    label("loc_753")

    Return()

    # Function_5_606 end

    def Function_6_754(): pass

    label("Function_6_754")

    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, -780, 24910, 8900, 46240, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A1")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_866")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x30C), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0x614E), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x22C4), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0xB4A0), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83B")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_828():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_828)
    Jump("loc_85E")

    label("loc_83B")


    def lambda_841():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_841)
    Sleep(200)

    label("loc_85E")

    Sleep(30)
    Jump("loc_89E")

    label("loc_866")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E")
    OP_44(0xFE, 0x2)

    def lambda_886():
        OP_8D(0xFE, -780, 24910, 8900, 46240, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_886)

    label("loc_89E")

    Jump("loc_77D")

    label("loc_8A1")

    Return()

    # Function_6_754 end

    def Function_7_8A2(): pass

    label("Function_7_8A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    OP_43(0xFE, 0x2, 0x0, 0x8)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_92D")
    TalkBegin(0xFE)
    OP_A2(0xA)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Found \x07\x02Fresh Eggs\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_92D")

    Return()

    # Function_7_8A2 end

    def Function_8_92E(): pass

    label("Function_8_92E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_949")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_8_92E")

    label("loc_949")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_92E end

    def Function_9_954(): pass

    label("Function_9_954")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_992")

    ChrTalk(    #1
        0xFE,
        "I'll leave it to you, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Good luck!\x02",
    )

    CloseMessageWindow()
    Jump("loc_119A")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_A96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9C6")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #3
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_A93")

    label("loc_9C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2C")
    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #4
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Ohhhh, Faye...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "For...give...me...eee...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_A93")

    label("loc_A2C")

    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #7
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Ohhhh, Faye...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm sooo...happy...\x01",
            "I understand now...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_A93")

    Jump("loc_119A")

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(    #10
        0xFE,
        (
            "I wonder if Faye's read my\x01",
            "letter yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "When I get nervous I can't\x01",
            "stop yawning...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC5")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_B8F")

    ChrTalk(    #13
        0xFE,
        (
            "When I think about Faye getting\x01",
            "that letter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I get nervous, and I can't\x01",
            "stop yawning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_DC5")

    label("loc_B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_D0C")

    ChrTalk(    #16
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "D-Did you deliver the letter?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(    #18
        0x101,
        (
            "#001FWe sure did.\x02\x03",

            "And the present too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3D")

    label("loc_C25")


    ChrTalk(    #19
        0x101,
        "#001FYeah, we did.\x02",
    )

    CloseMessageWindow()

    label("loc_C3D")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #20
        0xFE,
        (
            "Th-That's great.\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I wonder if she's reading it\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "...It's kind of unnerving.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x591)
    Jump("loc_D09")

    label("loc_CB5")


    ChrTalk(    #23
        0x101,
        "#000FNo, not just yet.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #24
        0xFE,
        "Oh. Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Well, here you go then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_D09")

    Jump("loc_DC5")

    label("loc_D0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D60")

    ChrTalk(    #26
        0xFE,
        "I'm still so tired...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I should get to bed early\x01",
            "tonight. *yawn*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC5")

    label("loc_D60")

    OP_A2(0x3)

    ChrTalk(    #28
        0xFE,
        "That's odd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It sounded like there was a big\x01",
            "ruckus going on here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "It woke me up.\x02",
    )

    CloseMessageWindow()

    label("loc_DC5")

    Jump("loc_119A")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_E03")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #31
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Zzzzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119A")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_E60")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #33
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "...Mmm...hnn...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Faye... So...sorry...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119A")

    label("loc_E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_110E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1107")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 1)), scpexpr(EXPR_END)), "loc_EF6")

    ChrTalk(    #36
        0xFE,
        (
            "When I think about Faye getting\x01",
            "that letter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I get nervous, and I can't\x01",
            "stop yawning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_FFE")

    label("loc_EF6")

    OP_A2(0x3)
    OP_A2(0x591)

    ChrTalk(    #39
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "D-Did you deliver the letter?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x80)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F7E")

    ChrTalk(    #41
        0x101,
        (
            "#001FWe sure did.\x02\x03",

            "And the present too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F96")

    label("loc_F7E")


    ChrTalk(    #42
        0x101,
        "#001FYeah, we did.\x02",
    )

    CloseMessageWindow()

    label("loc_F96")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #43
        0xFE,
        "Great. Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I wonder if she's reading it\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "...It's kind of unnerving.\x02",
    )

    CloseMessageWindow()

    label("loc_FFE")

    Jump("loc_1104")

    label("loc_1001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_107C")

    ChrTalk(    #46
        0xFE,
        (
            "When I think about Faye getting\x01",
            "that letter...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I get nervous, and I can't\x01",
            "stop yawning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()
    Jump("loc_1104")

    label("loc_107C")


    ChrTalk(    #49
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "D-Did you deliver the letter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#000FNo, not just yet.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #52
        0xFE,
        "Oh. Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I'm counting on you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1104")

    Jump("loc_110B")

    label("loc_1107")

    Call(1, 2)

    label("loc_110B")

    Jump("loc_119A")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_119A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1142")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #54
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_119A")

    label("loc_1142")

    OP_A2(0x3)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(800)

    ChrTalk(    #55
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "...Mmnngmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Nothing...to rep...ort...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_119A")

    TalkEnd(0xFE)
    Return()

    # Function_9_954 end

    def Function_10_119E(): pass

    label("Function_10_119E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_12B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1212")

    ChrTalk(    #58
        0xFE,
        "Oh, don't worry about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "The border patrol's pretty much\x01",
            "just for looks these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B8")

    label("loc_1212")

    OP_A2(0x4)

    ChrTalk(    #60
        0xFE,
        (
            "We're in the middle of inspections now. \x01",
            "There was some big incident in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Lately we've been stepping up all of\x01",
            "our border investigation procedures.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B8")

    TalkEnd(0xFE)
    Return()

    # Function_10_119E end

    def Function_11_12BC(): pass

    label("Function_11_12BC")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_12BC end

    def Function_12_12C3(): pass

    label("Function_12_12C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_140F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1352")

    ChrTalk(    #62
        0xFE,
        (
            "They still haven't got any leads \x01",
            "on the factory attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Even if we reopen inspections\x01",
            "I don't think it'll help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_140C")

    label("loc_1352")

    OP_A2(0x6)

    ChrTalk(    #64
        0xFE,
        (
            "They still haven't got any leads\x01",
            "on the factory attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "And why would they? We were\x01",
            "forced to close inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "The terrorists have probably\x01",
            "already fled the country.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140C")

    Jump("loc_1903")

    label("loc_140F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_14CF")

    ChrTalk(    #67
        0xFE,
        (
            "I know that there are some strict\x01",
            "inspection procedures going on\x01",
            "at the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Until they know everything about\x01",
            "the incident we need to just sit\x01",
            "tight and wait.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CC")

    label("loc_14CF")

    OP_A2(0x6)

    ChrTalk(    #69
        0xFE,
        (
            "We just got an emergency message.\x01",
            "This base is now officially on alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It seems that the incident in\x01",
            "Zeiss was the work of some\x01",
            "well-organized criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "It wouldn't surprise me if spies\x01",
            "from another country were\x01",
            "involved in it, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_1903")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1789")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_16B0")

    ChrTalk(    #72
        0xFE,
        (
            "If the situation changes we'll see\x01",
            "a big difference here right next\x01",
            "to the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I'm sure they have their eyes on\x01",
            "our kingdom's septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "That's why we need to watch\x01",
            "our borders so closely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1786")

    label("loc_16B0")

    OP_A2(0x6)

    ChrTalk(    #75
        0xFE,
        (
            "It looks like Liberl and the Calvard\x01",
            "Republic are on friendly terms...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "But that's probably only because\x01",
            "they have to worry about the\x01",
            "Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "'The enemy of my enemy is\x01",
            "my friend,' right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1786")

    Jump("loc_1903")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_183D")

    ChrTalk(    #78
        0xFE,
        (
            "Sleeping on the job, skipping\x01",
            "duty... This border patrol is an\x01",
            "embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "We're useless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I'm the only one who cares\x01",
            "about anything around here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1903")

    label("loc_183D")

    OP_A2(0x6)

    ChrTalk(    #81
        0xFE,
        "This border patrol is an embarrassment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Sleeping on the job, skipping\x01",
            "duty...it's all because the\x01",
            "chief looks the other way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I'm the only one who cares\x01",
            "about anything around here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1903")

    TalkEnd(0xFE)
    Return()

    # Function_12_12C3 end

    def Function_13_1907(): pass

    label("Function_13_1907")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_13_1907 end

    def Function_14_190E(): pass

    label("Function_14_190E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 0)), scpexpr(EXPR_END)), "loc_19F6")

    ChrTalk(    #84
        0xFE,
        "Still, all these sudden inspections...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I'm glad they started after I\x01",
            "brought through all those\x01",
            "heavy packages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "If I can't get my merchandise\x01",
            "to the Republic, there's no\x01",
            "reason for me to even come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B75")

    label("loc_19F6")


    ChrTalk(    #87
        0xFE,
        (
            "I heard there was an incident\x01",
            "in Zeiss and they're starting\x01",
            "border inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Maybe I should wait a little\x01",
            "and come through later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "Read a book or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "...Do you guys like to read?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "If you want, you can have this\x01",
            "one. I'm done with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5D0)
    OP_3E(0x218, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #92
        "\x07\x00Received \x07\x02Carnelia - Chapter 7\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #93
        0xFE,
        "This book is pretty good.\x02",
    )

    CloseMessageWindow()

    label("loc_1B75")

    Jump("loc_2232")

    label("loc_1B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2095")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C0F")

    ChrTalk(    #94
        0xFE,
        "Better safe than...whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I'm not going to risk my life\x01",
            "just to save the mira it'd cost\x01",
            "to hire some bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFC")

    label("loc_1C0F")

    OP_A2(0x2)

    ChrTalk(    #96
        0xFE,
        "This job has been hell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "On my way to Zeiss, my cart\x01",
            "broke right in the middle of\x01",
            "the Tratt Plains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "The bracers I hired were able\x01",
            "to go and find the parts I\x01",
            "needed to repair it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "...I didn't like being alone.\x02",
    )

    CloseMessageWindow()

    label("loc_1CFC")

    Jump("loc_2092")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x28, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D85")

    ChrTalk(    #100
        0xFE,
        (
            "The one bracer said he had\x01",
            "another job to do. He's\x01",
            "already long gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "Industrious guy, I'd say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EA6")

    label("loc_1D85")

    OP_A2(0x2)

    ChrTalk(    #102
        0xFE,
        "Hello, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Thanks for helping me out\x01",
            "back there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#000FOh, hi!\x02\x03",

            "So you made it all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Yes, that other bracer got me\x01",
            "back to town with my goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "And I got back here safely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "You bracers sure are a\x01",
            "dependable bunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "You all be careful out there.\x02",
    )

    CloseMessageWindow()

    label("loc_1EA6")

    Jump("loc_2092")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F1D")

    ChrTalk(    #109
        0xFE,
        (
            "The one bracer said he had\x01",
            "another job to do. He's\x01",
            "already long gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Industrious guy, I'd say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_1F1D")

    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FEE")

    ChrTalk(    #111
        0xFE,
        (
            "Hello, you all. Thanks again\x01",
            "for helping me out before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "Did you finish your business\x01",
            "in Elmo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#000FWe did. We're on our way\x01",
            "back home now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "Well, watch yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2092")

    label("loc_1FEE")


    ChrTalk(    #116
        0xFE,
        (
            "Hey there. Did you finish your\x01",
            "business in Elmo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I just finished getting all of\x01",
            "my products out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "We all ought to just relax and\x01",
            "enjoy the trip home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2092")

    Jump("loc_2232")

    label("loc_2095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_2102")

    ChrTalk(    #119
        0xFE,
        (
            "All I have to do is wait for my\x01",
            "Republican clearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Might as well take it easy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2232")

    label("loc_2102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_21AC")
    OP_A2(0x2)

    ChrTalk(    #121
        0xFE,
        (
            "Hello, you all. Thanks again for\x01",
            "helping me out before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I'm just sitting and waiting for\x01",
            "my Republican clearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "Might as well take it easy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2232")

    label("loc_21AC")

    OP_A2(0x2)
    OP_A2(0x580)

    ChrTalk(    #124
        0xFE,
        "Hey there. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Weren't you going to Elmo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#000FWe're on our way right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "Well, watch yourselves.\x02",
    )

    CloseMessageWindow()

    label("loc_2232")

    TalkEnd(0xFE)
    Return()

    # Function_14_190E end

    def Function_15_2236(): pass

    label("Function_15_2236")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_23CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22C3")

    ChrTalk(    #129
        0xFE,
        (
            "It seems the bracer I hired,\x01",
            "Wong, is from the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I hope all the people in the\x01",
            "Republic are as nice as him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CF")

    label("loc_22C3")

    OP_A2(0x0)

    ChrTalk(    #131
        0xFE,
        (
            "I'd thought the bracers would\x01",
            "be too busy investigating the\x01",
            "incident to do guard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "But my request went right on\x01",
            "through! I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "I didn't think my bodyguard\x01",
            "request would go through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "But it did! Those bracers are\x01",
            "pretty dependable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CF")

    TalkEnd(0xFE)
    Return()

    # Function_15_2236 end

    def Function_16_23D3(): pass

    label("Function_16_23D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2456")

    ChrTalk(    #135
        0xFE,
        (
            "The best I can do right now is\x01",
            "finish my assignment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I think that'll best benefit\x01",
            "our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2812")

    label("loc_2456")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 4)), scpexpr(EXPR_END)), "loc_265E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24C7")

    ChrTalk(    #137
        0xFE,
        "Gundolf's not here anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "I'm counting on you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "Let's see what we can do!\x02",
    )

    CloseMessageWindow()
    Jump("loc_265B")

    label("loc_24C7")


    ChrTalk(    #140
        0xFE,
        "Hey, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "How goes the investigation?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#000FNot bad, I guess.\x02\x03",

            "How about you, Wong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "After the incident, I got lots of\x01",
            "work from Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I haven't had any time to think\x01",
            "about things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I like to think I'm doing my best\x01",
            "to support the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "But I better not get in the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "Good luck, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#000FLeave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x102,
        "#010FBe careful, Wong.\x02",
    )

    CloseMessageWindow()

    label("loc_265B")

    Jump("loc_2812")

    label("loc_265E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_26E2")

    ChrTalk(    #150
        0xFE,
        (
            "I've got to work extra hard now\x01",
            "that Gundolf's not here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I think I'll rest a bit and then\x01",
            "check on my next job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2812")

    label("loc_26E2")

    OP_A2(0x1)

    ChrTalk(    #152
        0xFE,
        (
            "The attack on the central\x01",
            "factory was a shock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "After the accident, Kilika kept\x01",
            "me busy, so I haven't had time\x01",
            "to think about things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I think the best thing I can\x01",
            "do right now is finish my\x01",
            "assignments as best I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "I like to think I'm doing my best\x01",
            "to support the investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2812")

    Jump("loc_2894")

    label("loc_2815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2894")

    ChrTalk(    #156
        0xFE,
        (
            "Hi, guys. You really helped out\x01",
            "back there. Thanks a bunch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I'm glad we were able to make it\x01",
            "to the garrison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2894")

    TalkEnd(0xFE)
    Return()

    # Function_16_23D3 end

    def Function_17_2898(): pass

    label("Function_17_2898")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        (
            "\x07\x05East: Calvard Republic\x01",
            "West: Zeiss City - 280 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_2898 end

    SaveToFile()

Try(main)
