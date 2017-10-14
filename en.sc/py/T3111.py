from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3111   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3111_1 ._SN',
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
        'Erick',                                # 9
        'Hazel',                                # 10
        'Igor',                                 # 11
        'Freddy',                               # 12
        'Mirano',                               # 13
        'Simon',                                # 14
        'Faye',                                 # 15
        'Prometheus',                           # 16
        'Noticia',                              # 17
        'Rudi',                                 # 18
        'Factory Chief Murdock',                # 19
        '看板',                                 # 20
        'ダミー',                               # 21
        'Elderly Man',                          # 22
        'Wong',                                 # 23
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
        'ED6_DT07/CH01450 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01250 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01233 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01550 ._CH',             # 06
        'ED6_DT07/CH01100 ._CH',             # 07
        'ED6_DT07/CH01210 ._CH',             # 08
        'ED6_DT07/CH01500 ._CH',             # 09
        'ED6_DT07/CH02620 ._CH',             # 0A
        'ED6_DT07/CH01760 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01450P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01250P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01233P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01550P._CP',             # 06
        'ED6_DT07/CH01100P._CP',             # 07
        'ED6_DT07/CH01210P._CP',             # 08
        'ED6_DT07/CH01500P._CP',             # 09
        'ED6_DT07/CH02620P._CP',             # 0A
        'ED6_DT07/CH01760P._CP',             # 0B
    )

    DeclNpc(
        X                   = 8650,
        Z                   = 0,
        Y                   = -1430,
        Direction           = 270,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 6130,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 7720,
        Z                   = 0,
        Y                   = 4160,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 8830,
        Z                   = 0,
        Y                   = 3050,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -6250,
        Z                   = 100,
        Y                   = -4650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -4600,
        Z                   = 0,
        Y                   = -3500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -113390,
        Z                   = -4000,
        Y                   = -111160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -10070,
        Z                   = 0,
        Y                   = -200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -10070,
        Z                   = 0,
        Y                   = -1720,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -121060,
        Z                   = -4000,
        Y                   = -111070,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        Direction           = 14,
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
        Direction           = 14,
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
        X                   = -225250,
        Z                   = 0,
        Y                   = 17330,
        Direction           = 160,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -108560,
        Z                   = 0,
        Y                   = -105400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )


    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 3900,
        TriggerRange        = 400,
        ActorX              = 0,
        ActorZ              = 1500,
        ActorY              = 6130,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6900,
        TriggerZ            = 0,
        TriggerY            = -1410,
        TriggerRange        = 400,
        ActorX              = 8650,
        ActorZ              = 1500,
        ActorY              = -1430,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -200120,
        TriggerZ            = 0,
        TriggerY            = 118010,
        TriggerRange        = 1200,
        ActorX              = -200120,
        ActorZ              = 1500,
        ActorY              = 118010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121030,
        TriggerZ            = -4000,
        TriggerY            = -99900,
        TriggerRange        = 800,
        ActorX              = -121030,
        ActorZ              = -3000,
        ActorY              = -99900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37A",          # 00, 0
        "Function_1_45E",          # 01, 1
        "Function_2_5BE",          # 02, 2
        "Function_3_5C6",          # 03, 3
        "Function_4_21D3",         # 04, 4
        "Function_5_21D8",         # 05, 5
        "Function_6_343B",         # 06, 6
        "Function_7_3A1D",         # 07, 7
        "Function_8_47C9",         # 08, 8
        "Function_9_4E0A",         # 09, 9
        "Function_10_5225",        # 0A, 10
        "Function_11_6043",        # 0B, 11
        "Function_12_6165",        # 0C, 12
        "Function_13_61E9",        # 0D, 13
        "Function_14_631A",        # 0E, 14
        "Function_15_6F95",        # 0F, 15
        "Function_16_6F96",        # 10, 16
        "Function_17_7170",        # 11, 17
        "Function_18_82AC",        # 12, 18
        "Function_19_878B",        # 13, 19
        "Function_20_87EA",        # 14, 20
        "Function_21_8849",        # 15, 21
        "Function_22_88F6",        # 16, 22
        "Function_23_89A3",        # 17, 23
        "Function_24_8D1A",        # 18, 24
        "Function_25_8D80",        # 19, 25
        "Function_26_8DE6",        # 1A, 26
        "Function_27_8EAE",        # 1B, 27
        "Function_28_8F76",        # 1C, 28
        "Function_29_8FFC",        # 1D, 29
        "Function_30_9055",        # 1E, 30
        "Function_31_90BF",        # 1F, 31
    )


    def Function_0_37A(): pass

    label("Function_0_37A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3B7")
    ClearChrFlags(0x16, 0x80)

    label("loc_3B7")

    Jump("loc_3FD")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3DF")
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -113390, -4000, -111160, 0)
    Jump("loc_3FD")

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3E9")
    Jump("loc_3FD")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3FD")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_3FD")

    label("loc_3FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_429")
    SetChrPos(0xE, -116160, -4000, -113310, 90)

    label("loc_429")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45D")
    SetMapFlags(0x10000000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_44F"),
        (103, "loc_456"),
        (SWITCH_DEFAULT, "loc_45D"),
    )


    label("loc_44F")

    Event(0, 18)
    Jump("loc_45D")

    label("loc_456")

    Event(0, 23)
    Jump("loc_45D")

    label("loc_45D")

    Return()

    # Function_0_37A end

    def Function_1_45E(): pass

    label("Function_1_45E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    OP_6F(0x3, 0)
    OP_72(0x3, 0x10)
    OP_6F(0x1, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 29)
    OP_72(0x2, 0x10)
    OP_6F(0x4, 29)
    OP_72(0x4, 0x10)
    OP_6F(0x5, 29)
    OP_72(0x5, 0x10)
    OP_6F(0x7, 29)
    OP_72(0x7, 0x10)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_79(0xFF, 0x2)
    OP_7A(0x3D, 0x2)
    OP_7A(0x3E, 0x2)
    OP_7A(0x3F, 0x2)
    OP_7B()
    OP_72(0x1A, 0x4)
    OP_72(0x1B, 0x4)
    OP_72(0x1C, 0x4)
    OP_72(0x1D, 0x4)
    OP_72(0x1E, 0x4)
    OP_72(0x1F, 0x4)
    OP_76(0xFF, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x6, 0x0)
    Jump("loc_56E")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_562")
    Jump("loc_56E")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56E")

    label("loc_56E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_57E"),
        (109, "loc_57E"),
        (SWITCH_DEFAULT, "loc_5B7"),
    )


    label("loc_57E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A3")
    OP_75(0xFF, 0x16, 0x5)
    Jump("loc_5B4")

    label("loc_5A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B4")
    OP_22(0xA0, 0x1, 0x64)

    label("loc_5B4")

    Jump("loc_5BD")

    label("loc_5B7")

    OP_23(0xA0)
    Jump("loc_5BD")

    label("loc_5BD")

    Return()

    # Function_1_45E end

    def Function_2_5BE(): pass

    label("Function_2_5BE")

    OP_A2(0xE)
    Call(0, 3)
    Return()

    # Function_2_5BE end

    def Function_3_5C6(): pass

    label("Function_3_5C6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Cancel Job\x01",            # 1
            "Upgrade/Exchange\x01",      # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_696")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_659")
    Call(1, 8)
    Jump("loc_68C")

    label("loc_659")

    Call(1, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671")
    Call(1, 12)
    Jump("loc_68C")

    label("loc_671")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    Call(1, 11)

    label("loc_68C")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_696")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B1")
    Call(1, 10)
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CA")
    OP_A9(0x96)
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6CA")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_72A")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_707")
    OP_A9(0x9F)
    Jump("loc_709")

    label("loc_707")

    OP_A9(0x96)

    label("loc_709")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_713")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_727")
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_727")

    Jump("loc_1523")

    label("loc_72A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1523")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 6700, 0, -1700, 90)
    SetChrPos(0x102, 6500, 0, -900, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_791")
    SetChrPos(0xF9, 5500, 0, -1300, 90)
    SetChrPos(0xF8, 5300, 0, -400, 90)
    Jump("loc_7B3")

    label("loc_791")

    SetChrPos(0xF8, 5500, 0, -1300, 90)
    SetChrPos(0xF9, 5300, 0, -400, 90)

    label("loc_7B3")

    OP_8C(0x8, 270, 0)
    OP_6D(7160, 0, -820, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x8,
        (
            "Sorry, but I'm afraid our factory\x01",
            "is currently closed for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "None of the equipment we use\x01",
            "for machining is working.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(    #2
        0x101,
        (
            "#1018F#6POh, right, of course.\x01",
            "Don't worry, though!\x02\x03",

            "I THINK we have a little something to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Huh, what's that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_EF1")

    label("loc_8F7")


    ChrTalk(    #4
        0x101,
        (
            "#1026F#6POhhh, right.\x02\x03",

            "#1015FWell, that's kind of a problem,\x01",
            "isn't it?\x02\x03",

            "If we can't manufacture quartz or\x01",
            "upgrade our slots, we're kinda\x01",
            "in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(    #5
        0x103,
        (
            "#025F#6PYes, at this rate we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD3")

    label("loc_9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A32")

    ChrTalk(    #6
        0x108,
        (
            "#072F#6PAt this rate we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD3")

    label("loc_A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD3")

    ChrTalk(    #7
        0x106,
        (
            "#552F#6PKeep in mind we ARE kind of lucky to\x01",
            "even have arts right now.\x02\x03",

            "Does feel like a waste to just be sittin'\x01",
            "on all this sepith, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B49")

    ChrTalk(    #8
        0x107,
        (
            "#064F#6PAh, but, Estelle...\x02\x03",

            "If it's just for a little while,\x01",
            "we might be able to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB4")

    label("loc_B49")


    ChrTalk(    #9
        0x102,
        (
            "#1043F#6PThat's true, but...\x02\x03",

            "#1040FHowever, we may be able to do\x01",
            "something for a short time, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB4")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")

    def lambda_BE4():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BE4)
    Sleep(120)

    def lambda_BF7():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BF7)

    def lambda_C05():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C05)
    Sleep(120)

    def lambda_C18():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C18)
    Jump("loc_C2A")

    label("loc_C23")

    TurnDirection(0x101, 0x102, 400)

    label("loc_C2A")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #10
        0x101,
        "#1004F#4PHuh...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C94")

    ChrTalk(    #11
        0x106,
        "#052F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_C94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD3")

    ChrTalk(    #12
        0x103,
        "#023F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0F")

    ChrTalk(    #13
        0x108,
        "#073F#6PCan you get the factory working?\x02",
    )

    CloseMessageWindow()

    label("loc_D0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5B")

    ChrTalk(    #14
        0x107,
        (
            "#060F#6PY-Yeah, probably.\x02\x03",

            "If we use the generator...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCD")

    label("loc_D5B")


    ChrTalk(    #15
        0x102,
        (
            "#1040F#6PYes, most likely...\x02\x03",

            "If we use the generator, we can briefly\x01",
            "restore the equipment here, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DCD")


    ChrTalk(    #16
        0x101,
        "#1018F#4PRight, of course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E4A")

    ChrTalk(    #17
        0x8,
        "Uh, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "What the heck is this generator\x01",
            "you're talking about?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9B")

    label("loc_E4A")


    ChrTalk(    #19
        0x8,
        "Umm, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "What the heck is this generator\x01",
            "you're talking about?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B")


    def lambda_EA1():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EA1)
    Sleep(120)

    def lambda_EB4():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EB4)

    def lambda_EC2():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EC2)
    Sleep(120)

    def lambda_ED5():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_ED5)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1B")

    ChrTalk(    #21
        0x107,
        "#560FUm, you see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F39")

    label("loc_F1B")


    ChrTalk(    #22
        0x102,
        "#1040F#6PLet me explain.\x02",
    )

    CloseMessageWindow()

    label("loc_F39")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05Joshua explained that by using the Zero Field Generator the\x01",
            "factory's functionality could be temporarily restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x8,
        (
            "Ohh, so it's a generator that Professor\x01",
            "Russell made!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "I'd love to give it a spin.\x01",
            "Can I try it out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1011F#6PSure, no problem.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110D")

    ChrTalk(    #27
        0x107,
        "#560F#6PUm, would you help me, then, Erick?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Haha, I'm not much of an assistant compared\x01",
            "to you, so go easy on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_110D")


    ChrTalk(    #29
        0x102,
        "#1040F#6PCan I leave equipping the generator to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "Of course. Give me just a sec.\x02",
    )

    CloseMessageWindow()

    label("loc_116B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x8, 270, 0)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05On activation, the Zero Field Generator restored\x01",
            "power to the factory's tools.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x8, 9890, 0, 2600, 180)

    def lambda_11FF():
        OP_8E(0x8, 0x26A2, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11FF)

    def lambda_121A():

        label("loc_121A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_121A")

    QueueWorkItem2(0x0, 1, lambda_121A)

    def lambda_122B():

        label("loc_122B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_122B")

    QueueWorkItem2(0x1, 1, lambda_122B)

    def lambda_123C():

        label("loc_123C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_123C")

    QueueWorkItem2(0x2, 1, lambda_123C)

    def lambda_124D():

        label("loc_124D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_124D")

    QueueWorkItem2(0x3, 1, lambda_124D)
    FadeToBright(1000, 0)
    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0x21CA, 0x0, 0xFFFFFA6A, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    OP_0D()
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)

    ChrTalk(    #32
        0x8,
        (
            "Yep, looks like we're back in business.\x01",
            "For the moment, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "Considering the base theory, this\x01",
            "is only a temporary fix, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1383")

    ChrTalk(    #34
        0x107,
        (
            "#063F#6PYeah, it won't last long.\x02\x03",

            "#561FIt'll go back to how it was before soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C7")

    label("loc_1383")


    ChrTalk(    #35
        0x102,
        (
            "#1040F#6PYes, that's correct.\x02\x03",

            "With time it should stop again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13E1")
    Jump("loc_141F")

    label("loc_13E1")


    ChrTalk(    #36
        0x101,
        (
            "#1007F#6PI-I see...\x01",
            "It's only a temporary solution, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141F")


    ChrTalk(    #37
        0x8,
        "Got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Anyway, let's get your stuff\x01",
            "tuned now while we can, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x9F)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #39
        0x8,
        (
            "If we use that method, you should be able\x01",
            "to use the factory like normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "Since you've got the professor's invention,\x01",
            "use it as best you can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E4)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1636")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1591")

    ChrTalk(    #41
        0x8,
        "Everyone, thanks for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "If anything else comes up,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1633")

    label("loc_1591")


    ChrTalk(    #43
        0x8,
        "Today was a bit of a mess, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "It was my mistake to begin with,\x01",
            "so I'll solve it on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "If anything else comes up,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1633")

    Jump("loc_21CC")

    label("loc_1636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1671")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_166A")
    Call(1, 6)
    Jump("loc_166E")

    label("loc_166A")

    Call(1, 5)

    label("loc_166E")

    Jump("loc_21CC")

    label("loc_1671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_178B")

    ChrTalk(    #46
        0x8,
        (
            "If we could mass produce those Zero Field\x01",
            "Generators, the chaos would subside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "Mass producing such a complex piece of\x01",
            "equipment is a bit of a ridiculous order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "Though, this is Professor Russell we're talking\x01",
            "about. With him, anything seems possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_185A")

    ChrTalk(    #49
        0x8,
        (
            "Ahh, thanks to you guys I was\x01",
            "able to get some work done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "Seeing that generator in action is\x01",
            "pretty inspiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "It's orbal technology that saves people\x01",
            "in times of crisis, all right!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_185A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1963")

    ChrTalk(    #52
        0x8,
        (
            "The head of the central factory\x01",
            "is more or less the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "I'm sure there are some people with questions\x01",
            "about the announcement, but politically it was\x01",
            "the correct decision.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1960")

    ChrTalk(    #54
        0x8,
        (
            "A-Anyway, I need to do something\x01",
            "about my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1960")

    Jump("loc_1AD1")

    label("loc_1963")


    ChrTalk(    #55
        0x8,
        "Hey, how's it going, everyone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "Apparently Murdock sent out an announcement\x01",
            "about the earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Putting aside questions of scientific proof,\x01",
            "it's a good announcement, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "A little bit of reassurance from the Factory\x01",
            "Chief goes a long way to calming people,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACE")

    ChrTalk(    #59
        0x8,
        (
            "A-Anyway, I need to do something\x01",
            "about my own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACE")

    OP_A2(0x0)

    label("loc_1AD1")

    Jump("loc_21CC")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BE7")

    ChrTalk(    #60
        0x8,
        (
            "Rumor has it that the new apprentice girl is\x01",
            "the grandchild of a super-skilled technician\x01",
            "we used to have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I'm an apprentice too, so I've got to\x01",
            "make sure I keep up with her.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE4")

    ChrTalk(    #62
        0x8,
        (
            "*sigh* First I need to do something\x01",
            "about my own work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE4")

    Jump("loc_1D91")

    label("loc_1BE7")


    ChrTalk(    #63
        0x8,
        "Hey, everyone. Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "Oh, yeah, so we got this apprentice\x01",
            "technician recently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "Rumor has it she's the grandchild of a\x01",
            "super-skilled technician we used to have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "She seems like a normal girl, but I'm\x01",
            "sure she's just keeping her genius\x01",
            "under wraps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "I'm an apprentice too, so I've got to\x01",
            "make sure I keep up with her!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8E")

    ChrTalk(    #68
        0x8,
        (
            "*sigh* First I need to do something\x01",
            "about my own work...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8E")

    OP_A2(0x0)

    label("loc_1D91")

    Jump("loc_21CC")

    label("loc_1D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1FBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E8B")

    ChrTalk(    #69
        0x8,
        (
            "The central factory's putting some real\x01",
            "effort into making the new model orbments\x01",
            "mainstream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "There's a technician from Rolent\x01",
            "training here right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    ChrTalk(    #71
        0x8,
        (
            "A-Anyway, I need to do something\x01",
            "about my own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E88")

    Jump("loc_1FB7")

    label("loc_1E8B")


    ChrTalk(    #72
        0x8,
        (
            "Hey, everyone.\x01",
            "I owe you for your help before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "By the way, gotten used to your\x01",
            "new model orbments yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "Gotta get used to them more than learn them,\x01",
            "as they say. Experimenting's the best way\x01",
            "to get a feel for them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB4")

    ChrTalk(    #75
        0x8,
        (
            "A-Anyway, I need to do something\x01",
            "about my own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB4")

    OP_A2(0x0)

    label("loc_1FB7")

    Jump("loc_21CC")

    label("loc_1FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_20B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2013")

    ChrTalk(    #76
        0x8,
        "I screwed up at work the other day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "What to do, what to do...\x02",
    )

    CloseMessageWindow()
    Jump("loc_20B2")

    label("loc_2013")


    ChrTalk(    #78
        0x8,
        (
            "It's good that there wasn't any damage\x01",
            "from the earthquake, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "In exchange for that, sort of,\x01",
            "I've got my own trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "Man, what a mess.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_20B2")

    Jump("loc_21CC")

    label("loc_20B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_21CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_216E")

    ChrTalk(    #81
        0x8,
        (
            "I checked on the equipment, but it doesn't\x01",
            "seem like there was any damage from the\x01",
            "earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "Well, the shaking was pretty small,\x01",
            "so I thought it'd be okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CC")

    label("loc_216E")


    ChrTalk(    #83
        0x8,
        "Welcome to the central factory maintenance desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "Take a look around if you like.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_21CC")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    # Function_3_5C6 end

    def Function_4_21D3(): pass

    label("Function_4_21D3")

    Call(0, 5)
    Return()

    # Function_4_21D3 end

    def Function_5_21D8(): pass

    label("Function_5_21D8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2499")

    ChrTalk(    #85
        0x9,
        "Oh, my, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1003FYou okay, Hazel?\x02\x03",

            "Seems pretty dark in here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #87
        0x9,
        (
            "Well, I have a lamp so I'm okay,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "Most research activity has been completely\x01",
            "suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "Without orbal energy there's not much\x01",
            "we can do, really.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230B")

    ChrTalk(    #90
        0x107,
        "#561FAww...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2324")

    label("loc_230B")


    ChrTalk(    #91
        0x101,
        "#1007FAw... True...\x02",
    )

    CloseMessageWindow()

    label("loc_2324")


    ChrTalk(    #92
        0x102,
        (
            "#1043FSeems the situation is more\x01",
            "serious than we'd thought.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #93
        0x9,
        (
            "But, right now is when the central factory's\x01",
            "power is most needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "The entire staff is working together to\x01",
            "resume research as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006FYeah, if there's anything we can\x01",
            "do just say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        "Everyone, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "I hope we can count on you when\x01",
            "that time comes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_A2(0x20CC)
    Jump("loc_2783")

    label("loc_2499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2532")

    ChrTalk(    #98
        0x9,
        (
            "Right now is when the central factory's\x01",
            "power is most needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "We're working as hard as we can to\x01",
            "get our research back underway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2783")

    label("loc_2532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_26F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2667")

    ChrTalk(    #100
        0x9,
        (
            "There's a good view of that floating\x01",
            "object from the roof here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "A gentleman and his child went up\x01",
            "there moments ago to have a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        "To just head to the roof for a closer peek...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "I suppose curiosity could be\x01",
            "said to be the defining characteristic of this\x01",
            "city, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_26F5")

    label("loc_2667")


    ChrTalk(    #104
        0x9,
        (
            "There's a good view of that floating\x01",
            "object from the roof here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "A gentleman and his child went up\x01",
            "there moments ago to have a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F5")

    Jump("loc_2783")

    label("loc_26F8")


    ChrTalk(    #106
        0x9,
        (
            "Right now is when the central factory's\x01",
            "power is most needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "We're working as hard as we can to\x01",
            "get our research back underway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2783")

    Jump("loc_3437")

    label("loc_2786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 7)), scpexpr(EXPR_END)), "loc_27C8")

    ChrTalk(    #108
        0x9,
        "Watch over Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        "Be careful out there.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A43")

    label("loc_27C8")


    ChrTalk(    #110
        0x9,
        "Oh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        "I heard you're leaving Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1000FYeah, we're heading to the capital next.\x02\x03",

            "Seems like the Royal Army needs\x01",
            "us for something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #113
        0x9,
        "Goodness, you really are very busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        "Be sure to take care of yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "Don't push yourself too hard\x01",
            "just because you're young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1016FHaha. We'll be sure to keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29AA")

    ChrTalk(    #117
        0x9,
        "Well, then, take care of Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "Tita, you don't push yourself too hard,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x107,
        "#061FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C5")

    label("loc_29AA")


    ChrTalk(    #120
        0x9,
        "Do take care of Tita.\x02",
    )

    CloseMessageWindow()

    label("loc_29C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29E8")

    ChrTalk(    #121
        0x106,
        "#050FYeah, we will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A00")

    label("loc_29E8")


    ChrTalk(    #122
        0x103,
        "#020FYes, we will.\x02",
    )

    CloseMessageWindow()

    label("loc_2A00")


    ChrTalk(    #123
        0x101,
        "#1011FSee you later, Hazel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        "Take care at the capital.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x163F)

    label("loc_2A43")

    Jump("loc_3437")

    label("loc_2A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2B86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2ADF")

    ChrTalk(    #125
        0x9,
        "We've already contacted Elmo Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "Chief Murdock explained the situation\x01",
            "to them, so I'm sure they'll help out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B83")

    label("loc_2ADF")


    ChrTalk(    #127
        0x9,
        "We've already contacted Elmo Village.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "Chief Murdock explained the situation\x01",
            "to them, so I'm sure they'll help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        "Well, then, please be careful.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2B83")

    Jump("loc_2D95")

    label("loc_2B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C08")

    ChrTalk(    #130
        0x9,
        (
            "Professor Russell is on the fifth floor,\x01",
            "in the Operations room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        "Please use the elevator on the left.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D95")

    label("loc_2C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_2C94")

    ChrTalk(    #132
        0x9,
        (
            "Professor Russell just blew through\x01",
            "here. He seemed in quite the hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "It seems he's come up with some\x01",
            "new experiment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D95")

    label("loc_2C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2D0F")

    ChrTalk(    #134
        0x9,
        (
            "If you're looking for Professor Russell,\x01",
            "he's gone to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        "I imagine he's waiting there for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D95")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2D95")

    ChrTalk(    #136
        0x9,
        (
            "Right now, we don't have any reports\x01",
            "of damage from the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "The city seems safe as well,\x01",
            "so that's a relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D95")

    Jump("loc_3437")

    label("loc_2D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E5B")
    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #138
        0x9,
        "Oh, if it isn't the bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1018FAh, hey, Hazel. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x106,
        "#051FYeah, it has.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #141
        0x9,
        "Glad to see you're all in good health.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F01")

    label("loc_2E5B")

    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #142
        0x9,
        "Oh, who could this be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1018FAh, hey, Hazel. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        (
            "I'm glad to see you're looking as\x01",
            "energetic as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3047")

    ChrTalk(    #145
        0x9,
        (
            "Incidentally, Professor Russell\x01",
            "is in the Operations room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        (
            "I was told to pass that on to\x01",
            "you when you returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1018FAh, got'cha.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #148
        0x9,
        "The Operations room is on the fifth floor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        "Please use the elevator on the left.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1006FThe fifth floor? Got it. Thanks.\x01",
            "We'll head right up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3434")

    label("loc_3047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_31C8")

    ChrTalk(    #151
        0x9,
        "I see... So that's what it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1011FHuh, what was what?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #153
        0x9,
        (
            "Ah, well, Kilika said she'd\x01",
            "called for assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        "She must have meant all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1006FAh, probably, yeah.\x02\x03",

            "We'll be in Zeiss for a while. We're\x01",
            "looking forward to working with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        "Yes, as am I with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x9,
        "Well, then, good luck on your end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1000FYeah, you too, Hazel!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3434")

    label("loc_31C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_32B6")
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #159
        0x9,
        (
            "By the way, it seems Professor\x01",
            "Russell went to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        "I imagine he's waiting there for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1004FAh, got'cha.\x02\x03",

            "#1006FThanks for the heads up.\x01",
            "We'll head over right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        "Good luck with your work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3434")

    label("loc_32B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3434")

    ChrTalk(    #163
        0x9,
        "I see... So that's what it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1011FHuh, what was what?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #165
        0x9,
        (
            "Ah, well, Kilika said she'd\x01",
            "called for assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        "She must have meant all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1006FAh, probably, yeah.\x02\x03",

            "We'll be in Zeiss for a while. We're\x01",
            "looking forward to working with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        "Yes, as am I with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "Well, then, good luck on your end.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1000FYeah, you too, Hazel!\x02",
    )

    CloseMessageWindow()

    label("loc_3434")

    OP_A2(0x1429)

    label("loc_3437")

    TalkEnd(0x9)
    Return()

    # Function_5_21D8 end

    def Function_6_343B(): pass

    label("Function_6_343B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_35C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_34B8")

    ChrTalk(    #171
        0xFE,
        (
            "It seems the factory ship's\x01",
            "departed safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "Now the Arseille will finally have\x01",
            "its own wings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BE")

    label("loc_34B8")


    ChrTalk(    #173
        0xFE,
        (
            "It seems the factory ship's\x01",
            "departed safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Now the Arseille will finally have\x01",
            "its own wings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "After all, development of the engines\x01",
            "was delayed and we've kept her waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I'm sure the Arseille must be getting\x01",
            "terribly impatient as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_35BE")

    Jump("loc_3A19")

    label("loc_35C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3657")

    ChrTalk(    #177
        0xFE,
        (
            "Well, I can fix something like\x01",
            "the town clock, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "I wouldn't even dream of tightening a\x01",
            "screw on the new model engine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3713")

    label("loc_3657")


    ChrTalk(    #179
        0xFE,
        (
            "Seems preparation is underway for the\x01",
            "work on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "This time I'm keeping an eye on\x01",
            "things here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I'm a theorist, anyway. I wouldn't\x01",
            "be of any use at all on site.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3713")

    Jump("loc_3A19")

    label("loc_3716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_383D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3791")

    ChrTalk(    #182
        0xFE,
        (
            "To travel so far to learn about the\x01",
            "new model orbments...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "Now THIS is the soul of a technician.\x02",
    )

    CloseMessageWindow()
    Jump("loc_383A")

    label("loc_3791")


    ChrTalk(    #184
        0xFE,
        (
            "The boy here is a technician that\x01",
            "I've taken under my wing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "He's come all the way from Rolent\x01",
            "to train with the new models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "As expected of my student.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_383A")

    Jump("loc_3A19")

    label("loc_383D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3A19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3923")

    ChrTalk(    #187
        0xFE,
        (
            "Really, the recent crop of researchers are\x01",
            "such cowards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "In my day, we'd keep on experimenting\x01",
            "even when the lab was on fire. Hmph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I'm pretty sure the story about\x01",
            "Russell's head is a joke, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A19")

    label("loc_3923")


    ChrTalk(    #190
        0xFE,
        (
            "Hmph. All that panic over a little earthquake.\x01",
            "What a bunch of cowards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "In my youth, we kept on experimenting\x01",
            "right through a fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "I mean, look at Russell. You only get crazy\x01",
            "hair like that when it all burns off once or\x01",
            "twice.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_3A19")

    TalkEnd(0xA)
    Return()

    # Function_6_343B end

    def Function_7_3A1D(): pass

    label("Function_7_3A1D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_3FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3AC3")

    ChrTalk(    #193
        0xFE,
        "I'll be heading back to Rolent soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "Next time you come by the store\x01",
            "I'll show you the fruits of what I've\x01",
            "learned here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C41")

    label("loc_3AC3")

    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #195
        0xFE,
        (
            "Oh, yeah. Estelle, when will you\x01",
            "be going back to Rolent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1015FMy next stop's the capital,\x01",
            "so it'll still be a bit.\x02\x03",

            "#1000FHow about you, Freddy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "I'm scheduled to return pretty soon.\x01",
            "My training's almost over, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Next time you come by the store\x01",
            "I'll show you the fruits of what I've\x01",
            "learned here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1001FAhaha, looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3C41")

    Jump("loc_3F62")

    label("loc_3C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3CDA")

    ChrTalk(    #200
        0xFE,
        "The new model orbments have an extra slot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "They're way stronger as a result, but it also\x01",
            "makes setting it up kind of complicated.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F62")

    label("loc_3CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3DA3")

    ChrTalk(    #202
        0xFE,
        "I learned septium crafting from my dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "And then I learned the theory behind\x01",
            "quartz circuits from Igor here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "Looking back on it like this,\x01",
            "my life's truly been blessed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EF7")

    label("loc_3DA3")


    ChrTalk(    #205
        0xFE,
        (
            "Igor here was my teacher during my days\x01",
            "at the central factory way back when.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "Since I already knew him, I asked\x01",
            "him to train me this time too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "I learned septium crafting from my dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "And then I learned the theory behind\x01",
            "quartz circuits from Igor here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "Looking back on it like this,\x01",
            "my life's truly been blessed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3EF7")

    Jump("loc_3F62")

    label("loc_3EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3F62")

    ChrTalk(    #210
        0xFE,
        "Earthquakes are rare in Liberl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "I don't remember having any\x01",
            "in either Rolent OR Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F62")

    Jump("loc_3FD7")

    label("loc_3F65")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #212
        0xFE,
        (
            "Seems like you're doing really well.\x01",
            "That's a bit of a relief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "Anyway, good luck with your work.\x02",
    )

    CloseMessageWindow()

    label("loc_3FD7")

    Jump("loc_47C5")

    label("loc_3FDA")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #214
        0xFE,
        "Huh...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4038")

    ChrTalk(    #215
        0xFE,
        "I-Is it really you, Estelle?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_405D")

    label("loc_4038")


    ChrTalk(    #216
        0xFE,
        "E-Estelle! And even Scherazard!\x02",
    )

    CloseMessageWindow()

    label("loc_405D")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #217
        0x101,
        (
            "#1004FFreddy?!\x02\x03",

            "What the heck are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4140")

    ChrTalk(    #218
        0x106,
        "#052FYou two know each other?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#1000FYeah. He works at the orbal factory\x01",
            "in Rolent.\x02\x03",

            "#1004FOh, yeah, how's the store?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Jump("loc_4186")

    label("loc_4140")


    ChrTalk(    #220
        0x103,
        (
            "#020FMy, my. It really is a small world.\x02\x03",

            "How's the shop?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_4186")


    ChrTalk(    #221
        0xFE,
        (
            "Well, I've left things in Rolent to my\x01",
            "dad and came here to train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "I'm learning about the new orbment models.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1011FSo there's training for that, huh.\x02\x03",

            "#1015FOh, yeah, you said you'd studied here\x01",
            "before, didn't you, Freddy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #224
        0xFE,
        (
            "Yep. Had the basics beaten into\x01",
            "me here when I was young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "Well, I guess even now I'm having the basics\x01",
            "of the new model beaten into me. Heh.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_44AC")

    ChrTalk(    #226
        0xFE,
        "By the way, Joshua's not with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#1003FAh, y-yeah...\x02\x03",

            "#1015FSome stuff came up, so we're, ah,\x01",
            "working separately for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "Huh, too bad. Would've been nice\x01",
            "to see Joshua too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "But, I'm pretty happy just to run\x01",
            "into you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "It'll be a good story to tell my dad\x01",
            "once I get back to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "Anyway, good luck with your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1006FGood luck on your end too, Freddy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47BF")

    label("loc_44AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4629")

    ChrTalk(    #233
        0xFE,
        (
            "Incidentally...\x01",
            "You guys seem like you're in a bit of a rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#1002FAh, yeah. We have a kinda urgent\x01",
            "investigation going on right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4583")

    ChrTalk(    #235
        0x106,
        (
            "#050FYep.\x02\x03",

            "So, sorry, but we need to get goin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B6")

    label("loc_4583")


    ChrTalk(    #236
        0x103,
        (
            "#020FIndeed.\x02\x03",

            "Sorry, but if you'll excuse us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B6")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #237
        0xFE,
        "Ahh, got'cha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "Well, good luck with your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1006FThanks. Good luck with your training.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47BF")

    label("loc_4629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_47BF")

    ChrTalk(    #240
        0xFE,
        "By the way, Joshua's not with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1003FAh, y-yeah...\x02\x03",

            "#1015FSome stuff came up, so we're, ah,\x01",
            "working separately for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "Huh, too bad. Would've been nice\x01",
            "to see Joshua too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "But, I'm pretty happy just to run\x01",
            "into you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "It'll be a good story to tell my dad\x01",
            "once I get back to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "Anyway, good luck with your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        "#1006FGood luck on your end too, Freddy.\x02",
    )

    CloseMessageWindow()

    label("loc_47BF")

    OP_A2(0x142A)
    OP_A2(0x3)

    label("loc_47C5")

    TalkEnd(0xB)
    Return()

    # Function_7_3A1D end

    def Function_8_47C9(): pass

    label("Function_8_47C9")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_498A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4876")

    ChrTalk(    #247
        0xFE,
        (
            "I wonder if I can somehow get the\x01",
            "rights to shop that new engine around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "We'd make tons more money if we\x01",
            "handled it than if the country did.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4987")

    label("loc_4876")


    ChrTalk(    #249
        0xFE,
        (
            "So those new model engines are\x01",
            "sold here, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "I wonder if I can't somehow get the\x01",
            "rights to shop that new engine around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "We'd make tons more money if we\x01",
            "handled it than if the country did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "And they'd make more money in taxes,\x01",
            "so everyone's happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4987")

    Jump("loc_4E06")

    label("loc_498A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4A3F")

    ChrTalk(    #253
        0xFE,
        (
            "There are inventions that would take the world\x01",
            "by storm just rolling around the labs here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "If I had the time, I'd love to poke\x01",
            "around and check them out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B34")

    label("loc_4A3F")


    ChrTalk(    #255
        0xFE,
        (
            "There are amazing inventions completely\x01",
            "unavailable in the outside world just rolling\x01",
            "around the labs here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "If I had the time, I'd love to poke\x01",
            "around and check them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "I bet I'd find a thing or two to sink\x01",
            "a little mira in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4B34")

    Jump("loc_4E06")

    label("loc_4B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4BE2")

    ChrTalk(    #258
        0xFE,
        (
            "Trust is the most important thing\x01",
            "in the world of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "I'm not going to trust anything I hear until\x01",
            "I see the real thing with my own eyes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CCB")

    label("loc_4BE2")


    ChrTalk(    #260
        0xFE,
        (
            "Hmm, orbal cameras and household\x01",
            "goods might be the next big thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "The problem is the actual orbments.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "Simon, you've got a tally of the stock\x01",
            "in the basement factory, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        "You need to check them personally.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4CCB")

    Jump("loc_4E06")

    label("loc_4CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4D77")

    ChrTalk(    #264
        0xFE,
        (
            "That earthquake... No way it could have\x01",
            "reached as far as Bose, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "My mother would probably die of shock\x01",
            "if she felt one of those things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E06")

    label("loc_4D77")


    ChrTalk(    #266
        0xFE,
        (
            "Simon, if you're rattled by a tiny thing\x01",
            "like an earthquake, there's no hope\x01",
            "for you in negotiations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "Keep it together, will you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4E06")

    TalkEnd(0xC)
    Return()

    # Function_8_47C9 end

    def Function_9_4E0A(): pass

    label("Function_9_4E0A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_4F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4EA1")

    ChrTalk(    #268
        0xFE,
        (
            "To try and make money with Liberl's\x01",
            "negotiation ace in the hole...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "That's just like Mirano...\x01",
            "She's on some other level.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F50")

    label("loc_4EA1")


    ChrTalk(    #270
        0xFE,
        "T-Trade rights to the new engine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "To try and make money with Liberl's\x01",
            "negotiation ace in the hole...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "That's just like Mirano...\x01",
            "She's on some other level.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_4F50")

    Jump("loc_5221")

    label("loc_4F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4FEE")

    ChrTalk(    #273
        0xFE,
        (
            "U-Umm, it seems we need permission\x01",
            "to peruse the area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "Apparently the security is tighter since\x01",
            "the central factory was attacked once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5221")

    label("loc_4FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_5154")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5093")

    ChrTalk(    #275
        0xFE,
        (
            "I'll check out the basement factory\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "I'll ask the receptionist right away how\x01",
            "long it'll be before I have permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5151")

    label("loc_5093")


    ChrTalk(    #277
        0xFE,
        (
            "Y-Yes, I've checked the documents\x01",
            "on the stock of orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "I'll check out the basement factory\x01",
            "as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "U-Umm, it seems we need permission\x01",
            "to peruse the area.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5151")

    Jump("loc_5221")

    label("loc_5154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_5221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_51A5")

    ChrTalk(    #280
        0xFE,
        (
            "M-My legs... They still kind of feel\x01",
            "like they're shaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5221")

    label("loc_51A5")


    ChrTalk(    #281
        0xFE,
        (
            "M-My legs... They still kind of feel\x01",
            "like they're shaking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "I-It's okay. I'm okay. *pheeeew*\x01",
            "Deeeeep breaths...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5221")

    TalkEnd(0xD)
    Return()

    # Function_9_4E0A end

    def Function_10_5225(): pass

    label("Function_10_5225")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_523D")
    OP_A2(0x7)

    label("loc_523D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Messenger of Love' with high grade\x01",            # 0
            "Did not clear 'Messenger of Love' with high grade\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_52D7"),
        (1, "loc_52DD"),
        (SWITCH_DEFAULT, "loc_52E3"),
    )


    label("loc_52D7")

    OP_A2(0x7)
    Jump("loc_52E3")

    label("loc_52DD")

    OP_A3(0x7)
    Jump("loc_52E3")

    label("loc_52E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5305")
    Call(1, 0)
    Jump("loc_603F")

    label("loc_5305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_537A")

    ChrTalk(    #283
        0xFE,
        "I'll be counting on you from here on out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "Well, good luck with your work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_559E")

    label("loc_537A")


    ChrTalk(    #285
        0xFE,
        "Oh, hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "The guild sign thing sure was a shock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        (
            "#1000FWe really appreciate the help, Faye.\x02\x03",

            "We basically found it thanks to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #288
        0xFE,
        "Haha, it was nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "But, man, what kind of weirdo thief\x01",
            "steals a sign?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "Think you can catch the culprit?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015FIt might be difficult right now.\x02\x03",

            "But we'll catch him someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "Yeah, that's the spirit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "We'll be counting on you, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1001FAhaha, thanks for the encouragement.\x02\x03",

            "Well, then, good luck with your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "Yeah, you all too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x6C, 0x1, 0x2000)

    label("loc_559E")

    Jump("loc_603F")

    label("loc_55A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 3)), scpexpr(EXPR_END)), "loc_5C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_570D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_564A")

    ChrTalk(    #296
        0xFE,
        (
            "I'm gonna head out to Leiston Fortress\x01",
            "on the factory ship soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "Once we get there we're gonna\x01",
            "swap out the Arseille's engine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_570A")

    label("loc_564A")


    ChrTalk(    #298
        0xFE,
        "Now, then, I'd better get to the landing port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "I'm gonna head out to Leiston Fortress\x01",
            "on the factory ship soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "Once we get there we're gonna\x01",
            "swap out the Arseille's engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_570A")

    Jump("loc_5AC5")

    label("loc_570D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_5A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5898")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5798")

    ChrTalk(    #301
        0xFE,
        "I just made up with Bram, too, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "Lately I've been so busy we haven't\x01",
            "had the time to go out at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5895")

    label("loc_5798")


    ChrTalk(    #303
        0xFE,
        (
            "I don't mind being busy, but I kinda\x01",
            "hate not having any downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "I haven't had any time to go out with Bram,\x01",
            "even though we finally made up. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "Once the Arseille's work is done, I think\x01",
            "I'll finally be able to get some time off.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5895")

    Jump("loc_5A47")

    label("loc_5898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_5946")

    ChrTalk(    #306
        0xFE,
        (
            "I don't mind being busy, but I kinda\x01",
            "hate not having any downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "I hope I can go out again with Rudi like we\x01",
            "did for the queen's birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A47")

    label("loc_5946")


    ChrTalk(    #308
        0xFE,
        (
            "I don't mind being busy, but I kinda\x01",
            "hate not having any downtime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "Once the Arseille's work is done, I think\x01",
            "I'll finally be able to get some time off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "I hope I can go out again with Rudi like we\x01",
            "did for the queen's birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_5A47")

    Jump("loc_5AC5")

    label("loc_5A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_5AC5")

    ChrTalk(    #311
        0xFE,
        (
            "Doesn't seem like the earthquake did\x01",
            "anything to the basement factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "The line's working same as always.\x02",
    )

    CloseMessageWindow()

    label("loc_5AC5")

    Jump("loc_5C55")

    label("loc_5AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5B1C")

    ChrTalk(    #313
        0xFE,
        "Aren't you in a hurry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        "Well, let's both do our best on the job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C55")

    label("loc_5B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_5BC7")

    ChrTalk(    #315
        0xFE,
        (
            "As always, I'm pretty busy, but I admit\x01",
            "that's satisfying in its own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "Well, I wouldn't mind some time off\x01",
            "when it's crazy like this, to be honest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C55")

    label("loc_5BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_5C55")

    ChrTalk(    #317
        0xFE,
        "Still, though, earthquakes... That's rare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "There's nothing wrong here in the factory\x01",
            "but I'm worried about the people above.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C55")

    Jump("loc_603F")

    label("loc_5C58")


    ChrTalk(    #319
        0xFE,
        "Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "It's been a while, how have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1018FAh, Faye! We're good.\x02\x03",

            "How about you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #322
        0xFE,
        "Haha, same old, same old. Busy, busy.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5D75")

    ChrTalk(    #323
        0xFE,
        (
            "Thanks to you guys, I've made up\x01",
            "with Bram, too, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "Well, I'd say I'm pretty satisfied with my life.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5DD3")

    label("loc_5D75")


    ChrTalk(    #325
        0xFE,
        (
            "Exports have been going pretty well,\x01",
            "so the basement factory's been\x01",
            "going at full steam.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DD3")


    ChrTalk(    #326
        0xFE,
        "You guys here on work?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_5EEC")

    ChrTalk(    #327
        0x101,
        (
            "#1006FYeah, pretty much.\x02\x03",

            "#1015FWell, actually right now we're in the middle\x01",
            "of an urgent investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "Ah, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        (
            "Well, guess I shouldn't keep you\x01",
            "tied up, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1016FYeah, sorry.\x02\x03",

            "#1006FCatch you later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        "Good luck!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6039")

    label("loc_5EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_6039")

    ChrTalk(    #332
        0x101,
        (
            "#1006FYeah, basically.\x02\x03",

            "We'll be in Zeiss for a while,\x01",
            "so if you need anything just say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "Thanks, I appreciate it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "If anything comes up I won't hesitate\x01",
            "to contact the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "Anyway, I need to get back to\x01",
            "keeping an eye on the line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x101,
        (
            "#1011FAh, yeah, you're on the job.\x02\x03",

            "#1000FWell, see you later, Faye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6039")

    OP_A2(0x142B)
    OP_A2(0x8)

    label("loc_603F")

    TalkEnd(0xE)
    Return()

    # Function_10_5225 end

    def Function_11_6043(): pass

    label("Function_11_6043")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_6161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_615D")

    ChrTalk(    #337
        0xFE,
        (
            "Anyway, it's certainly an earthquake\x01",
            "with no historical precedent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        (
            "In other words, it's an earthquake that was\x01",
            "caused by something completely different\x01",
            "than what we've seen in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        (
            "For example, maybe an unknown volcano\x01",
            "is behind the tremors?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6161")

    label("loc_615D")

    Call(0, 13)

    label("loc_6161")

    TalkEnd(0xF)
    Return()

    # Function_11_6043 end

    def Function_12_6165(): pass

    label("Function_12_6165")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_61E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_61E1")

    ChrTalk(    #340
        0xFE,
        "Is it a special case?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "Could you explain to me what's supposed\x01",
            "to be special about it exactly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61E5")

    label("loc_61E1")

    Call(0, 13)

    label("loc_61E5")

    TalkEnd(0x10)
    Return()

    # Function_12_6165 end

    def Function_13_61E9(): pass

    label("Function_13_61E9")

    OP_4A(0xF, 255)
    OP_4A(0x10, 255)

    ChrTalk(    #342
        0x10,
        (
            "I'm with the Liberl News.\x01",
            "We contacted you earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x10,
        (
            "Let me get right to the point. Have you\x01",
            "determined the source of the earthquakes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xF,
        "No, we still don't know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xF,
        (
            "To be honest, these earthquakes\x01",
            "seem to be rather unique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xF,
        "Even we researchers are a bit confused.\x02",
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_A2(0xA)
    OP_A2(0xB)
    Return()

    # Function_13_61E9 end

    def Function_14_631A(): pass

    label("Function_14_631A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6B0C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6336")
    OP_A2(0x7)

    label("loc_6336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63D6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Messenger Love' with high grade\x01",            # 0
            "Did not clear 'Messenger Love' with high grade\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_63CA"),
        (1, "loc_63D0"),
        (SWITCH_DEFAULT, "loc_63D6"),
    )


    label("loc_63CA")

    OP_A2(0x7)
    Jump("loc_63D6")

    label("loc_63D0")

    OP_A3(0x7)
    Jump("loc_63D6")

    label("loc_63D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_654C")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649B")

    ChrTalk(    #347
        0xFE,
        (
            "We have no idea when the basement\x01",
            "factory will be back up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "It's a highly automated workshop,\x01",
            "so there's not much we can do if\x01",
            "orbments aren't working.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_6546")

    label("loc_649B")


    ChrTalk(    #349
        0xFE,
        (
            "We have no idea when the basement\x01",
            "factory will be back up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "Well, it's an entirely orbment-driven facility,\x01",
            "so there's not much we can do, obviously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6546")

    TalkEnd(0xFE)
    Jump("loc_6B09")

    label("loc_654C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_67F2")
    TalkBegin(0xFE)

    ChrTalk(    #351
        0xFE,
        "Did you get the gasoline?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        "Actually, I've never been to the hot springs.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_66B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_663E")

    ChrTalk(    #353
        0xFE,
        "I've heard it's a soak of a lifetime, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xFE,
        (
            "*sigh* I wonder if the pools at Elmo can\x01",
            "ease the pain of a broken heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_66AD")

    label("loc_663E")


    ChrTalk(    #355
        0xFE,
        "I've never been to the hot springs.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "*sigh* It might be the perfect spot to\x01",
            "wallow in a broken heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66AD")

    Jump("loc_67EC")

    label("loc_66B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6772")

    ChrTalk(    #357
        0xFE,
        "Maybe I'll invite Faye when she gets back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        "Th-Then we can go into the mixed bathing area...\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #359
        0xFE,
        "...Ehehehe. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x101,
        "#1019F(Soooo obvious...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_67EC")

    label("loc_6772")


    ChrTalk(    #361
        0xFE,
        "Maybe I'll invite Faye when she gets back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        "Th-Then we can go into the mixed bathing area...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        "...Ehehehe. ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_67EC")

    TalkEnd(0xFE)
    Jump("loc_6B09")

    label("loc_67F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6806")
    Call(0, 17)
    Return()

    label("loc_6806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_END)), "loc_6990")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_690C")

    ChrTalk(    #364
        0xFE,
        (
            "If you're going to Ruan, the Kaldia\x01",
            "Tunnel's the shortest route, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "...underground it's pitch black without\x01",
            "the orbal lamps, and super dangerous\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "If you're going to use that route,\x01",
            "be sure to be very careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_698A")

    label("loc_690C")


    ChrTalk(    #367
        0xFE,
        (
            "Inside the tunnel is pitch black and\x01",
            "very dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        (
            "If you're going to use that route,\x01",
            "be sure to be very careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698A")

    TalkEnd(0xFE)
    Jump("loc_6B09")

    label("loc_6990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A7B")

    ChrTalk(    #369
        0xFE,
        (
            "If you're looking for Faye, she's out\x01",
            "with the professor somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        (
            "Apparently it was a request from the Royal\x01",
            "Army, but it seemed kind of urgent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "To be honest, I feel a bit nervous without\x01",
            "Faye around.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_6B06")

    label("loc_6A7B")


    ChrTalk(    #372
        0xFE,
        (
            "If you're looking for Faye, she's out\x01",
            "with the professor somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        (
            "To not have her around at a time\x01",
            "like this, of all things...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B06")

    TalkEnd(0xFE)

    label("loc_6B09")

    Jump("loc_6F94")

    label("loc_6B0C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B24")
    OP_A2(0x7)

    label("loc_6B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BC4")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Messenger Love' with high grade\x01",            # 0
            "Did not clear 'Messenger Love' with high grade\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6BB8"),
        (1, "loc_6BBE"),
        (SWITCH_DEFAULT, "loc_6BC4"),
    )


    label("loc_6BB8")

    OP_A2(0x7)
    Jump("loc_6BC4")

    label("loc_6BBE")

    OP_A3(0x7)
    Jump("loc_6BC4")

    label("loc_6BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_6C75")

    ChrTalk(    #374
        0xFE,
        (
            "If you're looking for Faye, she's over at\x01",
            "Leiston Fortress with the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        (
            "Apparently they're going to change\x01",
            "out the Arseille's engine there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D8D")

    label("loc_6C75")


    ChrTalk(    #376
        0xFE,
        (
            "If you're looking for Faye, she's over at\x01",
            "Leiston Fortress with the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "Apparently they're going to change\x01",
            "out the Arseille's engine there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "Now, then, time to get some work\x01",
            "done while she's away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "Until fate sends me an angel,\x01",
            "my lover is my work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_6D8D")

    Jump("loc_6F91")

    label("loc_6D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_6E70")

    ChrTalk(    #380
        0xFE,
        (
            "Faye went off to Leiston Fortress\x01",
            "with the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "*sigh* Just as I'd decided to ask her\x01",
            "if we could start being official, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "Curse you, Arseille...! How dare you\x01",
            "get between me and Faye?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F91")

    label("loc_6E70")


    ChrTalk(    #383
        0xFE,
        (
            "Faye went off to Leiston Fortress\x01",
            "with the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "Apparently they're going to swap out\x01",
            "the Arseille's engine at the base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "J-Just as I'd decided to ask her\x01",
            "if we could start being official, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "Curse you, Arseille...! How dare you\x01",
            "get between me and Faye?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_6F91")

    TalkEnd(0x11)

    label("loc_6F94")

    Return()

    # Function_14_631A end

    def Function_15_6F95(): pass

    label("Function_15_6F95")

    Return()

    # Function_15_6F95 end

    def Function_16_6F96(): pass

    label("Function_16_6F96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_716C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_716C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70C4")

    ChrTalk(    #387
        0xFE,
        (
            "The highway lights are out, so traveling\x01",
            "on any road's dangerous these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "I suspect that passage through the\x01",
            "Kaldia Tunnel is especially bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        "But that's also the only way to get to Ruan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "Man... I hope I don't get an\x01",
            "escort job in that direction.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_716C")

    label("loc_70C4")


    ChrTalk(    #391
        0xFE,
        (
            "The Kaldia Tunnel is pitch black, so it'd\x01",
            "probably be impossible for most people\x01",
            "to get through...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "Man... I hope I don't get an\x01",
            "escort job in that direction.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_716C")

    TalkEnd(0xFE)
    Return()

    # Function_16_6F96 end

    def Function_17_7170(): pass

    label("Function_17_7170")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7195")
    Call(0, 28)
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_7195")

    Fade(1000)
    OP_6D(-119860, -4000, -108560, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(45000, 0)
    OP_6E(278, 0)
    SetChrPos(0x101, -121590, -4000, -109860, 180)
    SetChrPos(0x102, -120550, -4000, -109740, 180)
    SetChrPos(0xF8, -121640, -4000, -108680, 180)
    SetChrPos(0xF9, -120310, -4000, -108480, 180)
    OP_4A(0x11, 255)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72B3")

    ChrTalk(    #393
        0x107,
        "#560F#6PUm, Rudi.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #394
        0x11,
        (
            "#4POh, hey, guys.\x02\x03",

            "Need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#1025F#5PYeah, actually...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7335")

    label("loc_72B3")


    ChrTalk(    #396
        0x101,
        "#1025F#5PUm, Rudi.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #397
        0x11,
        (
            "#4POh, hey, guys.\x02\x03",

            "Need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x102,
        "#1040F#6PYes, actually...\x02",
    )

    CloseMessageWindow()

    label("loc_7335")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #399
        (
            "\x07\x05Estelle asked Rudi for some gasoline to repair the\x01",
            "pump facility.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #400
        0x11,
        (
            "#4PHuh, that does sound rough.\x02\x03",

            "I go to Elmo's hot springs a lot,\x01",
            "so I'd love to help out, but...\x02\x03",

            "You've got bad timing. We don't have\x01",
            "anything in stock right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_749C")

    ChrTalk(    #401
        0x107,
        "#063F#6PO-Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x101,
        "#1007F#5PWell, this is a slight problem...\x02",
    )

    CloseMessageWindow()
    Jump("loc_74E5")

    label("loc_749C")


    ChrTalk(    #403
        0x101,
        "#1026F#5PSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x102,
        "#1043F#6PWell, this is a slight problem...\x02",
    )

    CloseMessageWindow()

    label("loc_74E5")

    SetChrPos(0x12, -114100, 0, -100940, 270)
    ClearChrFlags(0x12, 0x80)

    NpcTalk(    #405
        0x12,
        "Man's Voice",
        "#6P... Is there someone there?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7552")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7590")

    label("loc_7552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7579")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7590")

    label("loc_7579")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7590")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75B7")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_75F5")

    label("loc_75B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75DE")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_75F5")

    label("loc_75DE")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_75F5")

    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_764F():

        label("loc_764F")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_764F")

    QueueWorkItem2(0xF8, 1, lambda_764F)
    Sleep(50)

    def lambda_7665():

        label("loc_7665")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7665")

    QueueWorkItem2(0xF9, 1, lambda_7665)
    Sleep(60)

    def lambda_767B():

        label("loc_767B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_767B")

    QueueWorkItem2(0x101, 1, lambda_767B)
    Sleep(50)

    def lambda_7691():

        label("loc_7691")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_7691")

    QueueWorkItem2(0x102, 1, lambda_7691)
    Sleep(60)

    def lambda_76A7():

        label("loc_76A7")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_76A7")

    QueueWorkItem2(0x11, 1, lambda_76A7)

    def lambda_76B8():
        OP_6D(-119650, -4000, -107120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76B8)

    def lambda_76D0():
        OP_67(0, 6350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_76D0)

    def lambda_76E8():
        OP_6E(286, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_76E8)
    SetChrPos(0x12, -117860, -2000, -100950, 0)
    OP_8E(0x12, 0xFFFE32E8, 0xFFFFF060, 0xFFFE61D2, 0x7D0, 0x0)
    OP_8C(0x12, 225, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7806")

    ChrTalk(    #406
        0x107,
        "#560F#5PAh, Chief Murdock...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x12,
        (
            "#802F#6PTita...and everybody else, too.\x02\x03",

            "#803FI thought I heard voices from down here\x01",
            "and wondered what could be going on.\x02\x03",

            "#800FDid another case come up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78B8")

    label("loc_7806")


    ChrTalk(    #408
        0x101,
        "#1004F#5PAh, Chief Murdock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x12,
        (
            "#802F#6POh, hello there.\x02\x03",

            "#803FI thought I heard voices from down here\x01",
            "and wondered what could be going on.\x02\x03",

            "#800FDid another case come up?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B8")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -121550, -4000, -108680, 0)
    SetChrPos(0x102, -120310, -4000, -108480, 0)
    SetChrPos(0xF8, -121700, -4000, -109860, 0)
    SetChrPos(0xF9, -120300, -4000, -109740, 0)
    SetChrPos(0x12, -120720, -4000, -107000, 180)
    Sleep(2000)
    OP_44(0x11, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #410
        0x12,
        (
            "#803F#3PI see, so that's it.\x02\x03",

            "#806FHmmm, I do remember ordering some gasoline\x01",
            "from the Republic about a month ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        "#1004F#2PR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x102,
        (
            "#1042F#4POne month... That's a long time for a delivery.\x01",
            "It should be here by now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x11,
        "#2PB-But, sir, I haven't received anything like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x12,
        (
            "#803F#3PNo, wait...\x02\x03",

            "#802FI think when I ordered it I said there was no\x01",
            "rush, so it was going to be delivered by sea,\x01",
            "if I remember rightly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B55")

    ChrTalk(    #415
        0x108,
        (
            "#070F#2PIn other words, it wouldn't have come\x01",
            "via airship but by a normal ship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3C")

    label("loc_7B55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BC5")

    ChrTalk(    #416
        0x106,
        (
            "#052F#2PSea delivery, huh...\x02\x03",

            "That'd mean they sent it on a regular ship,\x01",
            "not an airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C3C")

    label("loc_7BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C3C")

    ChrTalk(    #417
        0x103,
        (
            "#023F#2PBy sea, hmm...\x02\x03",

            "That would mean the delivery vessel would\x01",
            "be a normal ship, not an airship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C3C")


    ChrTalk(    #418
        0x12,
        (
            "#803F#3PYes, exactly.\x02\x03",

            "#806FIn which case, it was probably\x01",
            "delivered quite recently.\x02\x03",

            "#800FStands to reason it's probably stored\x01",
            "somewhere in Ruan right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x102,
        (
            "#1042F#4PMakes sense...\x02\x03",

            "Thanks to the Orbal Shutdown Phenomenon,\x01",
            "distribution has been paralyzed, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x101,
        (
            "#1006F#2PSo, we can get some if we go to the\x01",
            "harbor in Ruan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x12,
        (
            "#800F#3PYes, that seems your best chance.\x02\x03",

            "#803FOne moment...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #422
        (
            "\x07\x05Factory Chief Murdock wrote a short letter on the\x01",
            "spot and signed it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8E(0x12, 0xFFFE25E6, 0xFFFFF060, 0xFFFE5B56, 0x7D0, 0x0)
    OP_8C(0x12, 180, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #423
        "\x07\x00Received #1035i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x40B, 1)
    OP_8F(0x12, 0xFFFE2870, 0xFFFFF060, 0xFFFE5E08, 0x7D0, 0x0)

    ChrTalk(    #424
        0x12,
        (
            "#800F#3PGive that letter of introduction to the\x01",
            "harbor master of the Ruan port.\x02\x03",

            "I've asked him to give you the\x01",
            "gasoline if they have any in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1006F#2PThanks, Chief!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F9A")

    ChrTalk(    #426
        0x107,
        "#067F#2PHeehee... Thank you!\x02",
    )

    CloseMessageWindow()

    label("loc_7F9A")


    ChrTalk(    #427
        0x102,
        "#1054F#4PSorry for all the trouble...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x12,
        (
            "#801F#3PNot at all. I may not go as much as the professor,\x01",
            "but I visit the hot springs plenty nonetheless.\x02\x03",

            "As someone in charge of the Zeiss region,\x01",
            "this is the least I can do.\x02\x03",

            "#800FAll right, I need to get back to work.\x02\x03",

            "I've got a mountain of paperwork to get through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        "#1015F#2PI-I see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8140")

    ChrTalk(    #430
        0x107,
        (
            "#063F#2PUm, um...\x01",
            "Don't push yourself too hard, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8178")

    label("loc_8140")


    ChrTalk(    #431
        0x102,
        "#1043F#4PPlease don't push yourself too hard, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_8178")


    ChrTalk(    #432
        0x12,
        (
            "#801F#3PHaha, if you fix the pump, maybe I'll take\x01",
            "a little time off and go to the hot springs.\x02\x03",

            "Well, then, if you'll excuse me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2010)
    OP_28(0xC2, 0x1, 0x200)
    OP_28(0xC2, 0x1, 0x400)

    def lambda_8214():

        label("loc_8214")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_8214")

    QueueWorkItem2(0xF8, 1, lambda_8214)

    def lambda_8225():

        label("loc_8225")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_8225")

    QueueWorkItem2(0xF9, 1, lambda_8225)

    def lambda_8236():

        label("loc_8236")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_8236")

    QueueWorkItem2(0x101, 1, lambda_8236)

    def lambda_8247():

        label("loc_8247")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_8247")

    QueueWorkItem2(0x102, 1, lambda_8247)

    def lambda_8258():

        label("loc_8258")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_8258")

    QueueWorkItem2(0x11, 1, lambda_8258)
    OP_8E(0x12, 0xFFFE32E8, 0xFFFFF060, 0xFFFE61D2, 0x7D0, 0x0)
    OP_8E(0x12, 0xFFFE339C, 0xFFFFF830, 0xFFFE75AA, 0x7D0, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x11, 0x1)
    OP_4B(0x11, 255)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_17_7170 end

    def Function_18_82AC(): pass

    label("Function_18_82AC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82C3")
    Call(0, 28)
    Call(0, 29)

    label("loc_82C3")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-200, 0, 6140, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(350, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_8324():
        OP_6D(620, 0, -7820, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8324)

    def lambda_833C():
        OP_6E(285, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_833C)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0x13)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x14)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x15)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x16)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #433
        0x101,
        "#1004F#6PHoly...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_840B")

    ChrTalk(    #434
        0x106,
        (
            "#052FWell, this is...darker than\x01",
            "I figured it'd be.\x02\x03",

            "Looks like they got some\x01",
            "lamps goin' at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_858B")

    label("loc_840B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_847C")

    ChrTalk(    #435
        0x103,
        (
            "#023FI didn't quite expect it\x01",
            "to be THIS dark.\x02\x03",

            "At least they managed to\x01",
            "light some lamps.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_858B")

    label("loc_847C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_858B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8514")

    ChrTalk(    #436
        0x108,
        (
            "#073F#2PThis is a bit darker than\x01",
            "I'd imagined it would be.\x02\x03",

            "It looks like they found some\x01",
            "lamps to light, at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_858B")

    label("loc_8514")


    ChrTalk(    #437
        0x108,
        (
            "#073FThis is a bit darker than\x01",
            "I'd imagined it would be.\x02\x03",

            "It looks like they found some\x01",
            "lamps to light, at least.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_858B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85C6")

    ChrTalk(    #438
        0x107,
        "#063FI hope everyone here is okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_86D6")

    label("loc_85C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8686")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8635")

    ChrTalk(    #439
        0x108,
        (
            "#072F#2PI doubt the factory workers can get\x01",
            "anything done, as things stand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8683")

    label("loc_8635")


    ChrTalk(    #440
        0x108,
        (
            "#072FI doubt the factory workers can get\x01",
            "anything done, as things stand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8683")

    Jump("loc_86D6")

    label("loc_8686")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86D6")

    ChrTalk(    #441
        0x103,
        (
            "#522FI doubt anyone can get work\x01",
            "done with things like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D6")


    ChrTalk(    #442
        0x101,
        (
            "#1015F#6PSpeaking of which...the elevator\x01",
            "will be dead, won't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x102,
        (
            "#1035F#4PDefinitely.\x02\x03",

            "#1043FWe'll have to make use of the stairs\x01",
            "if we want to go to other floors.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2037)
    EventEnd(0x0)
    Return()

    # Function_18_82AC end

    def Function_19_878B(): pass

    label("Function_19_878B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -760, 0, -11540, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_87B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_87B2)
    OP_8E(0xFE, 0xFFFFFE16, 0x0, 0xFFFFE142, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_19_878B end

    def Function_20_87EA(): pass

    label("Function_20_87EA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 320, 0, -11560, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8811():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8811)
    OP_8E(0xFE, 0x1F4, 0x0, 0xFFFFE0DE, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_20_87EA end

    def Function_21_8849(): pass

    label("Function_21_8849")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -760, 0, -11540, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8870():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8870)
    OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFDBA2, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B7")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_88F5")

    label("loc_88B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88DE")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_88F5")

    label("loc_88DE")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_88F5")

    Return()

    # Function_21_8849 end

    def Function_22_88F6(): pass

    label("Function_22_88F6")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 320, 0, -11560, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_891D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_891D)
    OP_8E(0xFE, 0x14A, 0x0, 0xFFFFDB48, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8964")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_89A2")

    label("loc_8964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_898B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_89A2")

    label("loc_898B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_89A2")

    Return()

    # Function_22_88F6 end

    def Function_23_89A3(): pass

    label("Function_23_89A3")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89BA")
    Call(0, 28)
    Call(0, 29)

    label("loc_89BA")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(-200970, 0, 17180, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(335, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_8A1B():
        OP_6D(-225780, 0, 16880, 4500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A1B)

    def lambda_8A33():
        OP_67(0, 6990, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A33)

    def lambda_8A4B():
        OP_6B(2520, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8A4B)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0x18)
    Sleep(600)
    OP_43(0x102, 0x1, 0x0, 0x19)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x0, 0x1A)
    Sleep(600)
    OP_43(0xF9, 0x1, 0x0, 0x1B)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #444
        0x101,
        "#1004F#4PHoly...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AEA")

    ChrTalk(    #445
        0x106,
        (
            "#052FWell, this is...darker than\x01",
            "I figured it'd be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7B")

    label("loc_8AEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B2F")

    ChrTalk(    #446
        0x103,
        (
            "#023FI didn't quite expect it\x01",
            "to be THIS dark.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7B")

    label("loc_8B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B7B")

    ChrTalk(    #447
        0x108,
        (
            "#073FThis is a bit darker than I'd\x01",
            "imagined it would be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BB6")

    ChrTalk(    #448
        0x107,
        "#063FI hope everyone here is okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C65")

    label("loc_8BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C15")

    ChrTalk(    #449
        0x108,
        (
            "#075FI doubt the factory workers can get\x01",
            "anything done, as things stand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C65")

    label("loc_8C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C65")

    ChrTalk(    #450
        0x103,
        (
            "#522FI doubt anyone can get work\x01",
            "done with things like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C65")


    ChrTalk(    #451
        0x101,
        (
            "#1015F#4PSpeaking of which...the elevator\x01",
            "will be dead, won't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x102,
        (
            "#1035F#6PDefinitely.\x02\x03",

            "#1043FWe'll have to make use of the stairs\x01",
            "if we want to go to other floors.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2037)
    EventEnd(0x0)
    Return()

    # Function_23_89A3 end

    def Function_24_8D1A(): pass

    label("Function_24_8D1A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8D41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_8D41)
    OP_8E(0xFE, 0xFFFC8EE8, 0x0, 0x3BE2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_24_8D1A end

    def Function_25_8D80(): pass

    label("Function_25_8D80")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8DA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_8DA7)
    OP_8E(0xFE, 0xFFFC8EDE, 0x0, 0x3FFB, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_25_8D80 end

    def Function_26_8DE6(): pass

    label("Function_26_8DE6")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8E0D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_8E0D)
    OP_8E(0xFE, 0xFFFC848E, 0x0, 0x3E4E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFC8A4C, 0x0, 0x3ADE, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E6F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8EAD")

    label("loc_8E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E96")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8EAD")

    label("loc_8E96")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8EAD")

    Return()

    # Function_26_8DE6 end

    def Function_27_8EAE(): pass

    label("Function_27_8EAE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230000, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8ED5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_8ED5)
    OP_8E(0xFE, 0xFFFC848E, 0x0, 0x3E4E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFC89AC, 0x0, 0x4024, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F37")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8F75")

    label("loc_8F37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F5E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8F75")

    label("loc_8F5E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8F75")

    Return()

    # Function_27_8EAE end

    def Function_28_8F76(): pass

    label("Function_28_8F76")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8FEF"),
        (1, "loc_8FF5"),
        (SWITCH_DEFAULT, "loc_8FFB"),
    )


    label("loc_8FEF")

    OP_A2(0x1200)
    Jump("loc_8FFB")

    label("loc_8FF5")

    OP_A2(0x1201)
    Jump("loc_8FFB")

    label("loc_8FFB")

    Return()

    # Function_28_8F76 end

    def Function_29_8FFC(): pass

    label("Function_29_8FFC")

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

    # Function_29_8FFC end

    def Function_30_9055(): pass

    label("Function_30_9055")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #453
        (
            "\x07\x05Left: Central Factory Elevator\x01",
            "Right: Basement Workshop\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_9055 end

    def Function_31_90BF(): pass

    label("Function_31_90BF")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #454
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_31_90BF end

    SaveToFile()

Try(main)
