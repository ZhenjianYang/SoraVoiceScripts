from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '埃里克',                               # 9
        '海泽尔',                               # 10
        '伊格尔',                               # 11
        '佛莱迪',                               # 12
        '米拉诺',                               # 13
        '西蒙',                                 # 14
        '菲',                                   # 15
        '普罗梅笛',                             # 16
        '诺蒂亚',                               # 17
        '鲁迪',                                 # 18
        '玛多克工房长',                         # 19
        '看板',                                 # 20
        '临时',                                 # 21
        '大叔',                                 # 22
        '王',                                   # 23
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
        "Function_4_1ACF",         # 04, 4
        "Function_5_1AD4",         # 05, 5
        "Function_6_2890",         # 06, 6
        "Function_7_2CAC",         # 07, 7
        "Function_8_36CF",         # 08, 8
        "Function_9_3A54",         # 09, 9
        "Function_10_3D15",        # 0A, 10
        "Function_11_476B",        # 0B, 11
        "Function_12_4800",        # 0C, 12
        "Function_13_4853",        # 0D, 13
        "Function_14_4910",        # 0E, 14
        "Function_15_51F2",        # 0F, 15
        "Function_16_51F3",        # 10, 16
        "Function_17_533C",        # 11, 17
        "Function_18_61C0",        # 12, 18
        "Function_19_653B",        # 13, 19
        "Function_20_659A",        # 14, 20
        "Function_21_65F9",        # 15, 21
        "Function_22_66A6",        # 16, 22
        "Function_23_6753",        # 17, 23
        "Function_24_6A47",        # 18, 24
        "Function_25_6AAD",        # 19, 25
        "Function_26_6B13",        # 1A, 26
        "Function_27_6BDB",        # 1B, 27
        "Function_28_6CA3",        # 1C, 28
        "Function_29_6D2A",        # 1D, 29
        "Function_30_6D83",        # 1E, 30
        "Function_31_6DD9",        # 1F, 31
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "工作取消\x01",        # 1
            "改造·换钱\x01",      # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_650")
    Call(1, 8)
    Jump("loc_683")

    label("loc_650")

    Call(1, 9)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668")
    Call(1, 12)
    Jump("loc_683")

    label("loc_668")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_683")
    Call(1, 11)

    label("loc_683")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_68D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    Call(1, 10)
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    OP_A9(0x96)
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6C1")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_721")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6FE")
    OP_A9(0x9F)
    Jump("loc_700")

    label("loc_6FE")

    OP_A9(0x96)

    label("loc_700")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_70A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71E")
    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    label("loc_71E")

    Jump("loc_11DF")

    label("loc_721")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DF")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 6700, 0, -1700, 90)
    SetChrPos(0x102, 6500, 0, -900, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    SetChrPos(0xF9, 5500, 0, -1300, 90)
    SetChrPos(0xF8, 5300, 0, -400, 90)
    Jump("loc_7AA")

    label("loc_788")

    SetChrPos(0xF8, 5500, 0, -1300, 90)
    SetChrPos(0xF9, 5300, 0, -400, 90)

    label("loc_7AA")

    OP_8C(0x8, 270, 0)
    OP_6D(7160, 0, -820, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x8,
        (
            "真是不好意思，\x01",
            "工房现在停业中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "加工用的器材\x01",
            "现在都无法运转了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_879")

    ChrTalk(    #2
        0x101,
        (
            "#1018F#4P啊，那个不用担心。\x02\x03",

            "我们带了好东西来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "哎，究竟是什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEA")

    label("loc_879")


    ChrTalk(    #4
        0x101,
        (
            "#1026F#4P啊，是吗……\x02\x03",

            "#1015F嗯……不过正伤脑筋啊。\x02\x03",

            "结晶回路的合成和结晶孔的强化\x01",
            "都完全不能进行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_922")

    ChrTalk(    #5
        0x103,
        (
            "#025F嗯嗯，难得的发生器\x01",
            "真是暴殄天物了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF")

    label("loc_922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_961")

    ChrTalk(    #6
        0x108,
        (
            "#072F唔，难得的发生器\x01",
            "也只能暴殄天物了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF")

    label("loc_961")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AF")

    ChrTalk(    #7
        0x106,
        (
            "#552F啊啊，难得使用发生器\x01",
            "能使用魔法了。\x02\x03",

            "真是暴殄天物啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A04")

    ChrTalk(    #8
        0x107,
        (
            "#064F啊，不过姐姐……\x02\x03",

            "如果只是一小会儿，\x01",
            "或许能用也说不定哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A52")

    label("loc_A04")


    ChrTalk(    #9
        0x102,
        (
            "#1043F#1P确实如此……\x02\x03",

            "#1040F不过，如果只是一小会儿\x01",
            "或许能用也说不定哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A52")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC1")

    def lambda_A82():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A82)
    Sleep(120)

    def lambda_A95():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A95)

    def lambda_AA3():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_AA3)
    Sleep(120)

    def lambda_AB6():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_AB6)
    Jump("loc_AC8")

    label("loc_AC1")

    TurnDirection(0x101, 0x102, 400)

    label("loc_AC8")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #10
        0x101,
        "#1004F#4P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #11
        0x106,
        "#052F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B80")

    label("loc_B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B53")

    ChrTalk(    #12
        0x103,
        "#023F能让工房运作起来？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B80")

    label("loc_B53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B80")

    ChrTalk(    #13
        0x108,
        "#073F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()

    label("loc_B80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC2")

    ChrTalk(    #14
        0x107,
        (
            "#060F是，是，大概……\x02\x03",

            "用那个发生器的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C08")

    label("loc_BC2")


    ChrTalk(    #15
        0x102,
        (
            "#1040F#1P是，恐怕……\x02\x03",

            "如果使用那个发生器\x01",
            "应该能在短时间内复原。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C08")


    ChrTalk(    #16
        0x101,
        "#1018F#4P啊，原来如此！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C66")

    ChrTalk(    #17
        0x8,
        "那个，提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "那个发生器是什么东西？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C94")

    label("loc_C66")


    ChrTalk(    #19
        0x8,
        "那个，诸位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "那个发生器是什么事？\x02",
    )

    CloseMessageWindow()

    label("loc_C94")


    def lambda_C9A():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C9A)
    Sleep(120)

    def lambda_CAD():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_CAD)

    def lambda_CBB():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_CBB)
    Sleep(120)

    def lambda_CCE():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_CCE)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_CEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D18")

    ChrTalk(    #21
        0x107,
        "#560F嗯，其实是这样……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D39")

    label("loc_D18")


    ChrTalk(    #22
        0x102,
        "#1040F#1P那个，是这样的……\x02",
    )

    CloseMessageWindow()

    label("loc_D39")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05说明了使用『零力场发生器』\x01",
            "可暂时恢复工房机能的事。\x02",
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
            "啊啊！拉赛尔博士\x01",
            "最新发明的发生器吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "请一定拿来试试看啊，\x01",
            "能不能马上借我用用？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1011F#4P啊，嗯，没问题。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA6")

    ChrTalk(    #27
        0x107,
        (
            "#560F那么～埃里克先生。\x01",
            "可以帮我一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "哈哈，没问题，不过我手脚比较笨，\x01",
            "还要请你多指教了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE7")

    label("loc_EA6")


    ChrTalk(    #29
        0x102,
        (
            "#1040F#1P发生器的设置\x01",
            "交给你可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "当然。\x01",
            "稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EE7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x8, 270, 0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05使用『零力场发生器』将工房机能恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x8, 9890, 0, 2600, 180)

    def lambda_F53():
        OP_8E(0x8, 0x26A2, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F53)

    def lambda_F6E():

        label("loc_F6E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F6E")

    QueueWorkItem2(0x0, 1, lambda_F6E)

    def lambda_F7F():

        label("loc_F7F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F7F")

    QueueWorkItem2(0x1, 1, lambda_F7F)

    def lambda_F90():

        label("loc_F90")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F90")

    QueueWorkItem2(0x2, 1, lambda_F90)

    def lambda_FA1():

        label("loc_FA1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FA1")

    QueueWorkItem2(0x3, 1, lambda_FA1)
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
            "嗯，器材确实是\x01",
            "可以运转了，不过…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "从原理上来看的话，\x01",
            "应该只是一时性的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1086")

    ChrTalk(    #34
        0x107,
        (
            "#063F嗯，确实如此。\x02\x03",

            "#561F过一阵子就应该\x01",
            "恢复原状了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C4")

    label("loc_1086")


    ChrTalk(    #35
        0x102,
        (
            "#1040F#1P嗯，是啊。\x02\x03",

            "经过一段时间后\x01",
            "就会再次停止运转了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10DE")
    Jump("loc_1112")

    label("loc_10DE")


    ChrTalk(    #36
        0x101,
        (
            "#1007F#4P是、是吗……\x01",
            "看来是个应急型的装置啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1112")


    ChrTalk(    #37
        0x8,
        "原来如此，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "不管怎样，趁现在可以\x01",
            "好好利用一下工房了。\x02",
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
            "使用这种方法的话，\x01",
            "随时都可以使用工房哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "毕竟是博士辛苦发明出来的东西，\x01",
            "我们要好好利用才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E4)
    EventEnd(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_11DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_12BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1238")

    ChrTalk(    #41
        0x8,
        "各位，今天真是谢谢了，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "以后再有什么事情的话\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BA")

    label("loc_1238")


    ChrTalk(    #43
        0x8,
        "今天虽然很遗憾，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "毕竟是我的失误，\x01",
            "只能靠自己的力量来试着解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "如果以后再有什么事情的话\x01",
            "还请多多关照了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BA")

    Jump("loc_1AC8")

    label("loc_12BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_12F1")
    Call(1, 6)
    Jump("loc_12F5")

    label("loc_12F1")

    Call(1, 5)

    label("loc_12F5")

    Jump("loc_1AC8")

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_13B5")

    ChrTalk(    #46
        0x8,
        (
            "如果零导力发生器可以量产的话\x01",
            "也许就可以平息这次的混乱了吧…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "不过这样复杂的高端装置，\x01",
            "要想量产化实在是太困难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "不过如果是拉赛尔博士的话，\x01",
            "也没准可以创造出奇迹呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC8")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1454")

    ChrTalk(    #49
        0x8,
        (
            "哈～总之全靠大家，\x01",
            "这里又可以开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "看过那发生器的效果之后\x01",
            "我又变得干劲十足了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "能将人类从危机中拯救的\x01",
            "果然还是只有导力技术啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC8")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1610")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1521")

    ChrTalk(    #52
        0x8,
        (
            "中央工房的工房长\x01",
            "在这里的地位就相当于市长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "虽然有些人对安全宣言抱有怀疑，\x01",
            "但从行政方面考虑，这也是最正确的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(    #54
        0x8,
        (
            "……那个暂且不说了，\x01",
            "现在最重要的是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151E")

    Jump("loc_160D")

    label("loc_1521")


    ChrTalk(    #55
        0x8,
        "啊，大家听说了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "玛多克工房长已经发表了\x01",
            "有关地震的安全宣言呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "既然是有科学根据的发言，\x01",
            "我们也就可以放心了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "工房长那么说的话，\x01",
            "大家就可以安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160A")

    ChrTalk(    #59
        0x8,
        (
            "……那个暂且不说了，\x01",
            "现在最重要的是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160A")

    OP_A2(0x0)

    label("loc_160D")

    Jump("loc_1AC8")

    label("loc_1610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16C4")

    ChrTalk(    #60
        0x8,
        (
            "听传闻说，新来的女实习生\x01",
            "是以前某个知名人士\x01",
            "的孙女呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "同、同样是实习生，\x01",
            "我也绝对不会输给她的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C1")

    ChrTalk(    #62
        0x8,
        (
            "呼～还是先考虑自己的工作\x01",
            "该怎么办吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C1")

    Jump("loc_17E5")

    label("loc_16C4")


    ChrTalk(    #63
        0x8,
        (
            "呀，各位。\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "嗯，有个见习职员已经\x01",
            "过来了，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "听说那个新来的小姑娘\x01",
            "是以前某个知名人士\x01",
            "的孙女。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "这样看的话，虽然是个普通女孩，\x01",
            "但肯定会有过人之处吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "同、同样是实习生，\x01",
            "我也绝不能输给她的！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E2")

    ChrTalk(    #68
        0x8,
        (
            "呼～还是先考虑自己的工作\x01",
            "该怎么办吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E2")

    OP_A2(0x0)

    label("loc_17E5")

    Jump("loc_1AC8")

    label("loc_17E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_194A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1891")

    ChrTalk(    #69
        0x8,
        (
            "新型导力器能普及，\x01",
            "中央工房实在功不可没。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "现在也有洛连特的人\x01",
            "来这里进行研修呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")

    ChrTalk(    #71
        0x8,
        (
            "……那个暂且不说了，\x01",
            "现在最重要的是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188E")

    Jump("loc_1947")

    label("loc_1891")


    ChrTalk(    #72
        0x8,
        (
            "呀，各位。\x01",
            "上次真是多谢你们了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "新型的导力器\x01",
            "用得习惯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "总之，努力去习惯吧，\x01",
            "多试试它的各种新功能。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(    #75
        0x8,
        (
            "……那个暂且不说了，\x01",
            "现在最重要的是我的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1944")

    OP_A2(0x0)

    label("loc_1947")

    Jump("loc_1AC8")

    label("loc_194A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1998")

    ChrTalk(    #76
        0x8,
        (
            "很久没有在工作中\x01",
            "遇到失败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "那么，该怎么做呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A05")

    label("loc_1998")


    ChrTalk(    #78
        0x8,
        (
            "地震没有造成重大损害\x01",
            "虽然很好，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "很不幸的是，\x01",
            "我这里却发生了故障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "呼，真是认命了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1A05")

    Jump("loc_1AC8")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A7B")

    ChrTalk(    #81
        0x8,
        (
            "已经检查过部件了，\x01",
            "似乎没有因为地震而受到损坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "哈～那么小的震动，\x01",
            "我就知道不会有事的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC8")

    label("loc_1A7B")


    ChrTalk(    #83
        0x8,
        (
            "欢迎光临中央工房\x01",
            "的维修窗口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "要是有什么需要帮忙的\x01",
            "请尽管说哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1AC8")

    OP_A3(0xE)
    TalkEnd(0x8)
    Return()

    # Function_3_5C6 end

    def Function_4_1ACF(): pass

    label("Function_4_1ACF")

    Call(0, 5)
    Return()

    # Function_4_1ACF end

    def Function_5_1AD4(): pass

    label("Function_5_1AD4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1C")

    ChrTalk(    #85
        0x9,
        "啊，是各位游击士……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1003F海泽尔小姐，你还好吗？\x02\x03",

            "怎么回事，好像\x01",
            "这里好像很昏暗啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #87
        0x9,
        (
            "啊，至少有油灯，\x01",
            "还不要紧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "不过大部分的研究工作\x01",
            "都被迫中止了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "如果没有导力，\x01",
            "任何实验器材也都无法运转。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(    #90
        0x107,
        "#561F啊……是呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C0B")

    label("loc_1BF1")


    ChrTalk(    #91
        0x101,
        "#1007F啊……确实……\x02",
    )

    CloseMessageWindow()

    label("loc_1C0B")


    ChrTalk(    #92
        0x102,
        (
            "#1043F情况似乎比预想中的\x01",
            "还要严重啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #93
        0x9,
        (
            "但我觉得现在这种时候，\x01",
            "中央工房更要发挥自己的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "为了早日重新恢复研究工作，\x01",
            "大家都在拼命努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006F嗯，如果有什么我可以帮忙的\x01",
            "请尽管说哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        "各位，谢谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "像现在这种时候，\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_A2(0x20CC)
    Jump("loc_1EFE")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7E")

    ChrTalk(    #98
        0x9,
        (
            "中央工房更要发挥\x01",
            "自己的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "为了让研究工作重新展开，\x01",
            "我们也要努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFE")

    label("loc_1D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1EAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4B")

    ChrTalk(    #100
        0x9,
        (
            "在这里的屋顶上\x01",
            "可以清楚地看见浮游物体哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "刚才还有一名带着孩子的绅士\x01",
            "来这里参观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "在这种时候竟然还有兴致\x01",
            "特意来参观……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "呵呵呵，好奇心旺盛\x01",
            "是这里市民们的特点啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1EA7")

    label("loc_1E4B")


    ChrTalk(    #104
        0x9,
        (
            "在这里的屋顶上\x01",
            "可以清楚地看见浮游物体哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "刚才还有一名绅士带着孩子\x01",
            "来这里参观呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA7")

    Jump("loc_1EFE")

    label("loc_1EAA")


    ChrTalk(    #106
        0x9,
        (
            "中央工房更要发挥\x01",
            "自己的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "为了让研究工作重新展开，\x01",
            "我们也要努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFE")

    Jump("loc_288C")

    label("loc_1F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 7)), scpexpr(EXPR_END)), "loc_1F3D")

    ChrTalk(    #108
        0x9,
        (
            "提妲\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        "那么，请小心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2155")

    label("loc_1F3D")


    ChrTalk(    #110
        0x9,
        "哎呀，各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "我听说了哦！\x01",
            "你们要离开蔡斯了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1000F嗯，这次是要去王都呢。\x02\x03",

            "听说王国军那边\x01",
            "发来委托了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #113
        0x9,
        "呼～还真是忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "工作虽然重要，但请各位\x01",
            "还是要注意身体啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        "年轻人可不能太勉强自己。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1016F哈哈，谢谢啦。\x01",
            "我们会注意的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B8")

    ChrTalk(    #117
        0x9,
        (
            "那么，提妲\x01",
            "就拜托大家照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "提妲，\x01",
            "你也不要太乱来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x107,
        "#061F是的，我知道啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D7")

    label("loc_20B8")


    ChrTalk(    #120
        0x9,
        (
            "提妲也\x01",
            "就拜托大家照顾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_20F8")

    ChrTalk(    #121
        0x106,
        "#050F嗯，放心吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2111")

    label("loc_20F8")


    ChrTalk(    #122
        0x103,
        "#020F呵呵，没问题。\x02",
    )

    CloseMessageWindow()

    label("loc_2111")


    ChrTalk(    #123
        0x101,
        "#1011F那么先这样，海泽尔小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "嗯，到王都\x01",
            "也要小心啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x163F)

    label("loc_2155")

    Jump("loc_288C")

    label("loc_2158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21D5")

    ChrTalk(    #125
        0x9,
        (
            "亚尔摩村那边\x01",
            "已经联系过了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x9,
        (
            "玛多克工房长已经\x01",
            "把事情经过说明了，\x01",
            "他们一定会协助你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2255")

    label("loc_21D5")


    ChrTalk(    #127
        0x9,
        (
            "亚尔摩村那边\x01",
            "已经联系过了，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "玛多克工房长已经\x01",
            "把事情经过说明了，\x01",
            "他们一定会协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        "那么，请大家多小心吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2255")

    Jump("loc_23A1")

    label("loc_2258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22AA")

    ChrTalk(    #130
        0x9,
        (
            "拉赛尔博士\x01",
            "在５层的演算室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x9,
        (
            "请乘坐\x01",
            "左边的电梯上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_22AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_2300")

    ChrTalk(    #132
        0x9,
        (
            "拉赛尔博士刚才\x01",
            "风风火火就赶回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x9,
        (
            "看来是又想起\x01",
            "什么新实验了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_2300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2342")

    ChrTalk(    #134
        0x9,
        (
            "拉赛尔博士\x01",
            "好像去协会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x9,
        (
            "大概是去\x01",
            "等你们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A1")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_23A1")

    ChrTalk(    #136
        0x9,
        (
            "现在还没有接到地震\x01",
            "的受灾报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "市区这边应该没出什么事，\x01",
            "总算是可以放心了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A1")

    Jump("loc_288C")

    label("loc_23A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2456")
    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #138
        0x9,
        "啊，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1018F啊，海泽尔小姐。\x01",
            "好久不见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x106,
        "#051F啊！好久不见了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #141
        0x9,
        (
            "二位都还和从前一样，\x01",
            "真是太好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D7")

    label("loc_2456")

    TurnDirection(0x9, 0x101, 0)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #142
        0x9,
        "啊～还以为是谁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1018F啊，海泽尔小姐。\x01",
            "好久不见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        "还和从前一样，真是太好了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_24D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(    #145
        0x9,
        (
            "对了，拉赛尔博士\x01",
            "在演算室等着你们呢，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x9,
        (
            "他让我在你们回来之后\x01",
            "通知你们一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1018F啊，对了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #148
        0x9,
        "演算室就在５层。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x9,
        (
            "请乘坐\x01",
            "左边的电梯上去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1006F谢谢啦，是５层吗，\x01",
            "那么这就去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2889")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_26D3")

    ChrTalk(    #151
        0x9,
        (
            "不过，原来如此……\x01",
            "果然是如此吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1011F哎，什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #153
        0x9,
        (
            "嗯～雾香小姐\x01",
            "说过要请求支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "我就知道来的\x01",
            "会是你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1006F啊，是这样呀。\x02\x03",

            "那么，在蔡斯的期间\x01",
            "请继续关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x9,
        "嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x9,
        "那么，加油工作吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        "#1000F嗯，海泽尔小姐也是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2889")

    label("loc_26D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2779")
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #159
        0x9,
        (
            "对了，拉赛尔博士\x01",
            "好像是去协会了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "似乎是要在那里\x01",
            "等你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1004F啊，是吗。\x02\x03",

            "#1006F谢啦，那就赶快\x01",
            "去协会看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        "工作要加油啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2889")

    label("loc_2779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2889")

    ChrTalk(    #163
        0x9,
        (
            "不过，原来如此……\x01",
            "果然是如此吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1011F哎，什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #165
        0x9,
        (
            "嗯～雾香小姐\x01",
            "说过要请求支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        (
            "我就知道来的\x01",
            "会是你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1006F啊，是这样呀。\x02\x03",

            "那么，在蔡斯的期间\x01",
            "请继续关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        "嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        "那么，加油工作吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1000F嗯，海泽尔也是！\x02",
    )

    CloseMessageWindow()

    label("loc_2889")

    OP_A2(0x1429)

    label("loc_288C")

    TalkEnd(0x9)
    Return()

    # Function_5_1AD4 end

    def Function_6_2890(): pass

    label("Function_6_2890")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_29AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_28FE")

    ChrTalk(    #171
        0xFE,
        (
            "呼，工房船似乎顺利\x01",
            "出发了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "这样一来『埃尔赛尤』终于\x01",
            "可以拥有自己的双翼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A7")

    label("loc_28FE")


    ChrTalk(    #173
        0xFE,
        (
            "呼，工房船似乎顺利\x01",
            "出发了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "这样一来『埃尔赛尤』终于\x01",
            "可以拥有自己的双翼了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "新型引擎的开发\x01",
            "比预想的要迟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "『埃尔赛尤』大概\x01",
            "早就迫不及待了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_29A7")

    Jump("loc_2CA8")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2AA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A11")

    ChrTalk(    #177
        0xFE,
        (
            "好了，我也要准备修理一下\x01",
            "城里的时钟了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "那些什么新型引擎\x01",
            "实在是搞不清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AA4")

    label("loc_2A11")


    ChrTalk(    #179
        0xFE,
        (
            "『埃尔赛尤』的工事\x01",
            "好像已经开始准备了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "不过这次没有我什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "我这老家伙现在只剩下理论了，\x01",
            "还是那些现役的小子更能派上用场啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2AA4")

    Jump("loc_2CA8")

    label("loc_2AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2AFB")

    ChrTalk(    #182
        0xFE,
        (
            "特意来学习新型导力器\x01",
            "的基础理论……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "这才是像样的职业人。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2AFB")


    ChrTalk(    #184
        0xFE,
        (
            "那小子不但是我的弟子，\x01",
            "更是一名合格的职业人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "特意从洛连特过来\x01",
            "进行新型导力技术的研修。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "嗯，不愧是我的弟子啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2B7C")

    Jump("loc_2CA8")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2CA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C0A")

    ChrTalk(    #187
        0xFE,
        (
            "最近的年轻研究员们\x01",
            "太不争气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "我年轻的时候\x01",
            "就算周围着火\x01",
            "也都会继续研究的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "拉赛尔那家伙\x01",
            "实在是了不起啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA8")

    label("loc_2C0A")


    ChrTalk(    #190
        0xFE,
        (
            "真是一群没用的小子，\x01",
            "一点地震就给吓成那副德性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "我年轻的时候\x01",
            "就算周围着火\x01",
            "也都会继续研究的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "看看拉赛尔吧，\x01",
            "他的头发都快被研究\x01",
            "累得掉光了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2CA8")

    TalkEnd(0xA)
    Return()

    # Function_6_2890 end

    def Function_7_2CAC(): pass

    label("Function_7_2CAC")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 2)), scpexpr(EXPR_END)), "loc_30B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D21")

    ChrTalk(    #193
        0xFE,
        (
            "我准备再过一阵子\x01",
            "就回洛连特了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "下次再来我店时\x01",
            "会让你好好看看我的成果！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2A")

    label("loc_2D21")

    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #195
        0xFE,
        (
            "对了，艾丝蒂尔你\x01",
            "准备什么时候回洛连特呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#1015F接下来我们要先去王都，\x01",
            "回洛连特大概还要过一阵子了吧。\x02\x03",

            "#1000F佛莱迪呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "最近就要回去了，\x01",
            "研修已经快结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "下次再来我的店时\x01",
            "会让你好好看看我的成果！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1001F哈哈，那真是不错啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2E2A")

    Jump("loc_306B")

    label("loc_2E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2E9F")

    ChrTalk(    #200
        0xFE,
        (
            "新型的战术导力器\x01",
            "增加了１个结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "虽然性能因此而大大提升了，\x01",
            "但结晶回路的组合却也更麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306B")

    label("loc_2E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_300A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2F35")

    ChrTalk(    #202
        0xFE,
        (
            "我从父亲那里学到了\x01",
            "七耀石的加工技术……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "向伊格尔老师学习到了\x01",
            "结晶回路的理论知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "这些东西都是我人生中\x01",
            "最宝贵的财富。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2F35")


    ChrTalk(    #205
        0xFE,
        (
            "伊格尔先生是我\x01",
            "以前的老师。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        (
            "也算是有缘，这次的研修\x01",
            "又要麻烦他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "我从父亲那里学到了\x01",
            "七耀石的加工技术……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "向伊格尔老师学习到了\x01",
            "结晶回路的理论知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "这些东西都是我人生中\x01",
            "最宝贵的财富。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3007")

    Jump("loc_306B")

    label("loc_300A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_306B")

    ChrTalk(    #210
        0xFE,
        (
            "利贝尔王国是很少\x01",
            "发生地震的哦，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "无论是在洛连特还是蔡斯，\x01",
            "以前好像都从没发生过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_306B")

    Jump("loc_30B4")

    label("loc_306E")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #212
        0xFE,
        (
            "做的好像很不错，\x01",
            "今天真是放心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "那么，工作加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_30B4")

    Jump("loc_36CB")

    label("loc_30B7")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #214
        0xFE,
        "啊，那个……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3112")

    ChrTalk(    #215
        0xFE,
        "这不是艾丝蒂尔吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_3112")


    ChrTalk(    #216
        0xFE,
        (
            "艾、艾丝蒂尔！\x01",
            "而且连雪拉扎德也在？！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313D")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #217
        0x101,
        (
            "#1004F佛莱迪！？\x02\x03",

            "为、为什么佛莱迪\x01",
            "会在这里呀？！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_31F7")

    ChrTalk(    #218
        0x106,
        "#052F熟人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#1000F嗯，你应该在\x01",
            "洛连特的工房才是啊。\x02\x03",

            "#1004F店里没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)
    Jump("loc_3235")

    label("loc_31F7")


    ChrTalk(    #220
        0x103,
        (
            "#020F呵呵，世界还真是小啊。\x02\x03",

            "洛连特的店不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    label("loc_3235")


    ChrTalk(    #221
        0xFE,
        (
            "啊，把工房交给爸爸以后，\x01",
            "我就来中央工房研修了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "希望能在这里学到最新的\x01",
            "导力技术知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1011F嘿～还有这样的研修啊。\x02\x03",

            "#1015F说起来的话，佛莱迪\x01",
            "好像以前也在这里学习过吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #224
        0xFE,
        (
            "嗯～年轻的时候曾经在这里\x01",
            "学习过基础知识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "哈～其实现在学习的一样也是\x01",
            "新型的基础知识了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_348D")

    ChrTalk(    #226
        0xFE,
        (
            "不过…\x01",
            "约修亚没和你在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#1003F啊、啊，嗯……\x02\x03",

            "#1015F发生了一点事情呢，\x01",
            "现在我们暂时分别行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "是吗，那可真遗憾。\x01",
            "我还挺想约修亚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "不过，今天能遇到艾丝蒂尔\x01",
            "就已经很高兴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "可以在这里给你爸爸\x01",
            "买些礼物哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "……那么，加油工作吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#1006F嗯，佛莱迪\x01",
            "也加油研修吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C5")

    label("loc_348D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3590")

    ChrTalk(    #233
        0xFE,
        (
            "不过…\x01",
            "你们看起来好像很忙啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#1002F啊，嗯！有些\x01",
            "很紧急的调查。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3513")

    ChrTalk(    #235
        0x106,
        (
            "#050F就是那样啦，\x02\x03",

            "不好意思，先走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3540")

    label("loc_3513")


    ChrTalk(    #236
        0x103,
        (
            "#020F就是那样了哦，\x02\x03",

            "抱歉，我们先走了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3540")

    TurnDirection(0xFE, 0xF7, 400)

    ChrTalk(    #237
        0xFE,
        "啊～这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "那么，工作加油吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1006F嗯，努力研修吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C5")

    label("loc_3590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_36C5")

    ChrTalk(    #240
        0xFE,
        (
            "不过…\x01",
            "约修亚没和你在一起吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1003F啊、啊，嗯……\x02\x03",

            "#1015F发生了一点事情呢，\x01",
            "现在我们暂时分别行动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "是吗，那可真遗憾。\x01",
            "我还挺想约修亚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "不过，今天能遇到艾丝蒂尔\x01",
            "就已经很高兴了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "可以在这里给你爸爸\x01",
            "买些礼物哦，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "……那么，加油工作吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1006F嗯，佛莱迪\x01",
            "也加油研修吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C5")

    OP_A2(0x142A)
    OP_A2(0x3)

    label("loc_36CB")

    TalkEnd(0xB)
    Return()

    # Function_7_2CAC end

    def Function_8_36CF(): pass

    label("Function_8_36CF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_37E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_373B")

    ChrTalk(    #247
        0xFE,
        (
            "那个引擎的贩卖权，\x01",
            "要想办法争取来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "要是得到的话，\x01",
            "比交给国家要有效率多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E6")

    label("loc_373B")


    ChrTalk(    #249
        0xFE,
        (
            "听说新型的引擎\x01",
            "也是这里制造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "那个引擎的贩卖权，\x01",
            "要想办法争取来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "要是得到的话，\x01",
            "比交给国家要有效率多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "不但税金会增加，\x01",
            "而且推广也会更迅速。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_37E6")

    Jump("loc_3A50")

    label("loc_37E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_38C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_384B")

    ChrTalk(    #253
        0xFE,
        (
            "这里的研究室\x01",
            "创造过很多\x01",
            "惊世的发明呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "如果有时间的话\x01",
            "真想去参观一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_384B")


    ChrTalk(    #255
        0xFE,
        (
            "这里也许还有很多\x01",
            "惊世的发明呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "如果有时间的话\x01",
            "真想去参观一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "肯定有很多没有公布于世\x01",
            "的东西吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_38BF")

    Jump("loc_3A50")

    label("loc_38C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_391E")

    ChrTalk(    #258
        0xFE,
        "在商业世界中信用是最重要的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "在看见真东西之前，\x01",
            "一定要保证信用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399E")

    label("loc_391E")


    ChrTalk(    #260
        0xFE,
        (
            "相机和家庭用品\x01",
            "该怎么办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "问题是导力器都是现货。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "西蒙，地下工厂\x01",
            "的库存怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "要亲自去\x01",
            "确认才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_399E")

    Jump("loc_3A50")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A04")

    ChrTalk(    #264
        0xFE,
        (
            "不过，这次的地震。\x01",
            "倒是没有波及到柏斯啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "如果震过来的话\x01",
            "一定会吓死人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A50")

    label("loc_3A04")


    ChrTalk(    #266
        0xFE,
        (
            "西蒙如果感觉到地震的话，\x01",
            "从他的脚部就可以看出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "冷静，冷静。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3A50")

    TalkEnd(0xC)
    Return()

    # Function_8_36CF end

    def Function_9_3A54(): pass

    label("Function_9_3A54")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_3B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(    #268
        0xFE,
        (
            "因为王国的外交政策，\x01",
            "钱也比以前难赚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "不愧是米拉诺小姐……\x01",
            "想法都和别人不同。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B41")

    label("loc_3AC4")


    ChrTalk(    #270
        0xFE,
        "新、新型引擎的贩卖权……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "因为王国的外交政策，\x01",
            "钱也比以前难赚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "不愧是米拉诺小姐……\x01",
            "想法都和别人不同。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3B41")

    Jump("loc_3D11")

    label("loc_3B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_3BB4")

    ChrTalk(    #273
        0xFE,
        (
            "好、好像参观的时候\x01",
            "需要办相关手续呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "因为中央工房的被袭事件，\x01",
            "现在的标准比以前严格了很多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D11")

    label("loc_3BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3C11")

    ChrTalk(    #275
        0xFE,
        (
            "真想早点去\x01",
            "看看地下工厂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "要是能办理许可证的话\x01",
            "我马上就会去办。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C8B")

    label("loc_3C11")


    ChrTalk(    #277
        0xFE,
        (
            "是、是的，导力器\x01",
            "的库存已经确认完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "真想早点去\x01",
            "看看地下工厂啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "嗯，在得到许可之前\x01",
            "看来要稍等一阵了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3C8B")

    Jump("loc_3D11")

    label("loc_3C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_3D11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3CC4")

    ChrTalk(    #280
        0xFE,
        (
            "总、总觉得脚底下\x01",
            "好像有些摇晃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D11")

    label("loc_3CC4")


    ChrTalk(    #281
        0xFE,
        (
            "总、总觉得脚底下\x01",
            "好像有些摇晃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "没、没问题，\x01",
            "马上就可以冷静了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3D11")

    TalkEnd(0xD)
    Return()

    # Function_9_3A54 end

    def Function_10_3D15(): pass

    label("Function_10_3D15")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2D")
    OP_A2(0x7)

    label("loc_3D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇【爱的使者】高评价完成】\x01",          # 0
            "【◇【爱的使者】没有高评价完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DA7"),
        (1, "loc_3DAD"),
        (SWITCH_DEFAULT, "loc_3DB3"),
    )


    label("loc_3DA7")

    OP_A2(0x7)
    Jump("loc_3DB3")

    label("loc_3DAD")

    OP_A3(0x7)
    Jump("loc_3DB3")

    label("loc_3DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD5")
    Call(1, 0)
    Jump("loc_4767")

    label("loc_3DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3E39")

    ChrTalk(    #283
        0xFE,
        (
            "今后可能也还会有事情\x01",
            "要拜托各位的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "那么～工作请加油吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FF1")

    label("loc_3E39")


    ChrTalk(    #285
        0xFE,
        "呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "协会的招牌板竟然会在这里，\x01",
            "真是吓了我一跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        (
            "#1000F多谢协助啦。\x02\x03",

            "全亏了菲小姐的帮忙\x01",
            "才能发现。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #288
        0xFE,
        (
            "哈哈，那种小事\x01",
            "不必客气啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "不过，盗走招牌板的小偷\x01",
            "实在是很可怕啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "抓到他了没有？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015F现在想抓到他太难了…\x02\x03",

            "不过呢，总有一天\x01",
            "一定会抓到他的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "嗯，就是要有这种信心！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "今后可能也还会有事情\x01",
            "拜托你们啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1001F哈哈，多谢鼓励，\x02\x03",

            "努力工作吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "啊啊～你们也是哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x6C, 0x1, 0x2000)

    label("loc_3FF1")

    Jump("loc_4767")

    label("loc_3FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 3)), scpexpr(EXPR_END)), "loc_44AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_40E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4068")

    ChrTalk(    #296
        0xFE,
        (
            "我也要乘坐工房船\x01",
            "前往雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "要在那里进行『埃尔赛尤』\x01",
            "的改装工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40E6")

    label("loc_4068")


    ChrTalk(    #298
        0xFE,
        (
            "那么，差不多该\x01",
            "要赶快去飞船坪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "我也要乘坐工房船\x01",
            "前往雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "要在那里进行『埃尔赛尤』\x01",
            "的改装工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_40E6")

    Jump("loc_4393")

    label("loc_40E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_434F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_420E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4155")

    ChrTalk(    #301
        0xFE,
        (
            "好不容易才和布拉姆\x01",
            "重归于好，可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "最近实在太忙，\x01",
            "连约会的时间也没有。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_420B")

    label("loc_4155")


    ChrTalk(    #303
        0xFE,
        (
            "只是忙倒不算什么，\x01",
            "可连休假都没有实在太痛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "好不容易才和布拉姆重归于好，\x01",
            "现在却连在一起约会的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "等『埃尔赛尤』的工作结束之后\x01",
            "一定要申请休个长假……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_420B")

    Jump("loc_434C")

    label("loc_420E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4296")

    ChrTalk(    #306
        0xFE,
        (
            "只是忙的话倒也无所谓，\x01",
            "可连休假都没有实在太痛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        (
            "但要是偶尔可以像诞辰庆典时那样\x01",
            "再和鲁迪一起去哪里玩玩就好了…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434C")

    label("loc_4296")


    ChrTalk(    #308
        0xFE,
        (
            "只是忙的话倒也无所谓，\x01",
            "可连休假都没有实在太痛苦了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "等『埃尔赛尤』的工作结束之后\x01",
            "真想有几天休假啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        (
            "但要是偶尔可以像诞辰庆典时那样\x01",
            "再和鲁迪一起去哪里玩玩就好了…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_434C")

    Jump("loc_4393")

    label("loc_434F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4393")

    ChrTalk(    #311
        0xFE,
        (
            "这里的地下工厂\x01",
            "似乎没有受到地震的影响\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "天线很正常，\x02",
    )

    CloseMessageWindow()

    label("loc_4393")

    Jump("loc_44AC")

    label("loc_4396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_43D3")

    ChrTalk(    #313
        0xFE,
        "不是很着急吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "那……大家都\x01",
            "加油工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44AC")

    label("loc_43D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_4449")

    ChrTalk(    #315
        0xFE,
        (
            "虽然还是和以前一样忙得要死，\x01",
            "但也只有这样才会有充实的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "呼，说实话，\x01",
            "我也希望偶尔可以歇一歇。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44AC")

    label("loc_4449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_44AC")

    ChrTalk(    #317
        0xFE,
        (
            "即便是这样\x01",
            "地震还真是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "工厂虽然没有什么异常情况，\x01",
            "但上层的各位还是很担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44AC")

    Jump("loc_4767")

    label("loc_44AF")


    ChrTalk(    #319
        0xFE,
        "哎呀，是你们啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "好久不见，最近还好吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1018F啊，菲小姐！\x02\x03",

            "菲小姐最近怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #322
        0xFE,
        (
            "哈哈，我还是和以前一样\x01",
            "每天忙得要死。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4590")

    ChrTalk(    #323
        0xFE,
        (
            "多亏你们\x01",
            "我和布拉姆重新和好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "总之，感觉还算是很充实啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_45BF")

    label("loc_4590")


    ChrTalk(    #325
        0xFE,
        (
            "这里的输出也很顺利，\x01",
            "地下工厂没有休息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45BF")


    ChrTalk(    #326
        0xFE,
        (
            "你们也在\x01",
            "这里工作吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_4689")

    ChrTalk(    #327
        0x101,
        (
            "#1006F嗯，是啊！\x02\x03",

            "#1015F嗯，现在有些\x01",
            "比较紧急的调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "啊，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "打扰你们真不好意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1016F嗯，抱歉啊。\x02\x03",

            "#1006F那我就先走啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        "好，加油吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4761")

    label("loc_4689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_4761")

    ChrTalk(    #332
        0x101,
        (
            "#1006F嗯，是啊！\x02\x03",

            "暂时会待在蔡斯，\x01",
            "有需要帮忙的话不用客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "那多谢了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        (
            "如果有什么需要的话\x01",
            "和协会联络就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "那我还要工作，\x01",
            "先去忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x101,
        (
            "#1011F噢，在工作吗？\x02\x03",

            "#1000F嗯，菲小姐，再见啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4761")

    OP_A2(0x142B)
    OP_A2(0x8)

    label("loc_4767")

    TalkEnd(0xE)
    Return()

    # Function_10_3D15 end

    def Function_11_476B(): pass

    label("Function_11_476B")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_47FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_47F8")

    ChrTalk(    #337
        0xFE,
        (
            "总之过去是没发生过\x01",
            "这种地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        (
            "也就是说，这次的地震\x01",
            "应该有特殊的原因。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        (
            "比如未知的火山开始活动\x01",
            "等等原因……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FC")

    label("loc_47F8")

    Call(0, 13)

    label("loc_47FC")

    TalkEnd(0xF)
    Return()

    # Function_11_476B end

    def Function_12_4800(): pass

    label("Function_12_4800")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_484F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_484B")

    ChrTalk(    #340
        0xFE,
        "特殊的原因吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        (
            "哪里特殊？\x01",
            "是否可以解说一下？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_484F")

    label("loc_484B")

    Call(0, 13)

    label("loc_484F")

    TalkEnd(0x10)
    Return()

    # Function_12_4800 end

    def Function_13_4853(): pass

    label("Function_13_4853")

    OP_4A(0xF, 255)
    OP_4A(0x10, 255)

    ChrTalk(    #342
        0x10,
        (
            "之前和利贝尔通讯的人\x01",
            "进行过联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x10,
        (
            "震源已经\x01",
            "确定了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xF,
        "没，还没有查明。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xF,
        (
            "说实话，这次的地震\x01",
            "相当奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xF,
        (
            "即使是我们这些科学家\x01",
            "也难以探明其原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_A2(0xA)
    OP_A2(0xB)
    Return()

    # Function_13_4853 end

    def Function_14_4910(): pass

    label("Function_14_4910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4EAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_492C")
    OP_A2(0x7)

    label("loc_492C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇【爱的使者】高评价完成】\x01",          # 0
            "【◇【爱的使者】没有高评价完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_49A6"),
        (1, "loc_49AC"),
        (SWITCH_DEFAULT, "loc_49B2"),
    )


    label("loc_49A6")

    OP_A2(0x7)
    Jump("loc_49B2")

    label("loc_49AC")

    OP_A3(0x7)
    Jump("loc_49B2")

    label("loc_49B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_4A7F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A25")

    ChrTalk(    #347
        0xFE,
        (
            "地下工厂\x01",
            "还没有恢复的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        (
            "是完全自动化的，\x01",
            "导力器无法运作的话\x01",
            "就什么都做不了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4A79")

    label("loc_4A25")


    ChrTalk(    #349
        0xFE,
        (
            "地下工厂\x01",
            "还没有恢复的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "哎，毕竟是靠导力驱动的设施，\x01",
            "这也是当然的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A79")

    TalkEnd(0xFE)
    Jump("loc_4EA8")

    label("loc_4A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_END)), "loc_4CA6")
    TalkBegin(0xFE)

    ChrTalk(    #351
        0xFE,
        "汽油到手了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        (
            "其实我连一次都没有\x01",
            "去过温泉呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B35")

    ChrTalk(    #353
        0xFE,
        (
            "虽然听说那里的热水\x01",
            "泡起来很舒服，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xFE,
        (
            "唉，亚尔摩的温泉\x01",
            "也不能治愈失恋的创伤吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4B8B")

    label("loc_4B35")


    ChrTalk(    #355
        0xFE,
        (
            "我还一次\x01",
            "都没有去过温泉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        (
            "唉，作为伤心旅行的场所，\x01",
            "也许那里再适合不过了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B8B")

    Jump("loc_4CA0")

    label("loc_4B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C41")

    ChrTalk(    #357
        0xFE,
        (
            "不如等菲前辈回来之后\x01",
            "试着约她一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        "那、那可是露天的温泉浴……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #359
        0xFE,
        "……嘿、嘿嘿嘿嘿㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x101,
        "#1019F（目、目的太明显了吧～）\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4CA0")

    label("loc_4C41")


    ChrTalk(    #361
        0xFE,
        (
            "不如等菲前辈回来之后\x01",
            "试着约她一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        "那、那可是露天的温泉浴……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        "嘿嘿嘿……㈱\x02",
    )

    CloseMessageWindow()

    label("loc_4CA0")

    TalkEnd(0xFE)
    Jump("loc_4EA8")

    label("loc_4CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CBA")
    Call(0, 17)
    Return()

    label("loc_4CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_END)), "loc_4DA3")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4D")

    ChrTalk(    #364
        0xFE,
        (
            "要去卢安的话\x01",
            "卡鲁迪亚隧道是条近路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "不过隧道现在一团漆黑，\x01",
            "非常危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "要想从那里通行的话\x01",
            "一定要非常小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4D9D")

    label("loc_4D4D")


    ChrTalk(    #367
        0xFE,
        (
            "不过隧道现在一团漆黑，\x01",
            "非常危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        (
            "要想从那里通行的话\x01",
            "一定要非常小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D9D")

    TalkEnd(0xFE)
    Jump("loc_4EA8")

    label("loc_4DA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4F")

    ChrTalk(    #369
        0xFE,
        (
            "菲前辈和博士一起\x01",
            "去什么地方办事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        (
            "听说是王国军的邀请，\x01",
            "不过看起来好像慌慌张张的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        (
            "说老实话，这种时候没有前辈在身边…\x01",
            "心里还真是不踏实啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_4EA5")

    label("loc_4E4F")


    ChrTalk(    #372
        0xFE,
        (
            "菲前辈和博士一起\x01",
            "去什么地方办事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        (
            "这种时候前辈不在旁边\x01",
            "真是很不踏实啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EA5")

    TalkEnd(0xFE)

    label("loc_4EA8")

    Jump("loc_51F1")

    label("loc_4EAB")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC3")
    OP_A2(0x7)

    label("loc_4EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F49")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇【爱的使者】高评价完成】\x01",          # 0
            "【◇【爱的使者】没有高评价完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F3D"),
        (1, "loc_4F43"),
        (SWITCH_DEFAULT, "loc_4F49"),
    )


    label("loc_4F3D")

    OP_A2(0x7)
    Jump("loc_4F49")

    label("loc_4F43")

    OP_A3(0x7)
    Jump("loc_4F49")

    label("loc_4F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5080")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_4FBA")

    ChrTalk(    #374
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "要在那边进行作业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_507D")

    label("loc_4FBA")


    ChrTalk(    #376
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "要在那边进行作业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "好了～前辈不在的时候\x01",
            "我就要一个人努力工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "在新的邂逅来临之前，\x01",
            "工作就是我的恋人！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_507D")

    Jump("loc_51EE")

    label("loc_5080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5117")

    ChrTalk(    #380
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "呜，我正准备向前辈提出\x01",
            "正式交往的请求呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "可恶的『埃尔赛尤』……\x01",
            "竟敢把我和前辈拆散～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51EE")

    label("loc_5117")


    ChrTalk(    #383
        0xFE,
        (
            "菲前辈乘坐工房的飞船\x01",
            "去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "为了装配『埃尔赛尤』的引擎，\x01",
            "前辈要去要塞进行作业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "但、但我今天本来还要\x01",
            "向前辈提出正式交往的请求呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "可、可恶的『埃尔赛尤』……\x01",
            "竟敢把我和前辈拆散～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_51EE")

    TalkEnd(0x11)

    label("loc_51F1")

    Return()

    # Function_14_4910 end

    def Function_15_51F2(): pass

    label("Function_15_51F2")

    Return()

    # Function_15_51F2 end

    def Function_16_51F3(): pass

    label("Function_16_51F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D2")

    ChrTalk(    #387
        0xFE,
        (
            "街道的灯已经全部熄灭了，\x01",
            "现在哪条路也都很难走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0xFE,
        (
            "特别是卡鲁迪亚隧道\x01",
            "普通人连出行都成了问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xFE,
        (
            "但是要去卢安的话\x01",
            "也只能走那里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "呼，呼……\x01",
            "要是有护卫委托的话该怎么办呢…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_5338")

    label("loc_52D2")


    ChrTalk(    #391
        0xFE,
        (
            "卡鲁迪亚隧道一片漆黑\x01",
            "普通人连出行都成了问题啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "呼，呼……\x01",
            "要是有护卫委托的话该怎么办呢…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5338")

    TalkEnd(0xFE)
    Return()

    # Function_16_51F3 end

    def Function_17_533C(): pass

    label("Function_17_533C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5361")
    Call(0, 28)
    Call(0, 29)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_5361")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5499")

    ChrTalk(    #393
        0x107,
        "#560F#5P那个…鲁迪哥哥。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #394
        0x11,
        (
            "#4P啊～这不是提妲吗，\x01",
            "艾丝蒂尔也在一起啊，\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#1025F#5P嗯，是这样……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5521")

    label("loc_5499")


    ChrTalk(    #396
        0x101,
        "#1025F#5P那个…鲁迪。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #397
        0x11,
        (
            "#4P啊～这不是艾丝蒂尔吗。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x102,
        "#1040F#5P是的，其实……\x02",
    )

    CloseMessageWindow()

    label("loc_5521")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #399
        (
            "\x07\x05向鲁迪说明了水泵装置的事情，\x01",
            "并请求将这里储备的汽油分一些来。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #400
        0x11,
        (
            "#4P啊～那可真不得了，\x02\x03",

            "亚尔摩温泉我也经常去的，\x01",
            "很想帮你们，可是……\x02\x03",

            "真不好意思，\x01",
            "这里储备的汽油也用完了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5641")

    ChrTalk(    #401
        0x107,
        "#063F#5P这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x101,
        "#1007F#5P这可麻烦了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_567F")

    label("loc_5641")


    ChrTalk(    #403
        0x101,
        "#1026F#5P竟、竟然会这样……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x102,
        "#1043F#5P这可麻烦了……\x02",
    )

    CloseMessageWindow()

    label("loc_567F")

    SetChrPos(0x12, -114100, 0, -100940, 270)
    ClearChrFlags(0x12, 0x80)

    NpcTalk(    #405
        0x12,
        "男性的声音",
        "#6P……谁在那里说话啊？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56E4")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5722")

    label("loc_56E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5722")

    label("loc_570B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5722")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5749")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5787")

    label("loc_5749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5770")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5787")

    label("loc_5770")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5787")

    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_57E1():

        label("loc_57E1")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_57E1")

    QueueWorkItem2(0xF8, 1, lambda_57E1)
    Sleep(50)

    def lambda_57F7():

        label("loc_57F7")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_57F7")

    QueueWorkItem2(0xF9, 1, lambda_57F7)
    Sleep(60)

    def lambda_580D():

        label("loc_580D")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_580D")

    QueueWorkItem2(0x101, 1, lambda_580D)
    Sleep(50)

    def lambda_5823():

        label("loc_5823")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5823")

    QueueWorkItem2(0x102, 1, lambda_5823)
    Sleep(60)

    def lambda_5839():

        label("loc_5839")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_5839")

    QueueWorkItem2(0x11, 1, lambda_5839)

    def lambda_584A():
        OP_6D(-119650, -4000, -107120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_584A)

    def lambda_5862():
        OP_67(0, 6350, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5862)

    def lambda_587A():
        OP_6E(286, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_587A)
    SetChrPos(0x12, -117860, -2000, -100950, 0)
    OP_8E(0x12, 0xFFFE32E8, 0xFFFFF060, 0xFFFE61D2, 0x7D0, 0x0)
    OP_8C(0x12, 225, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_596C")

    ChrTalk(    #406
        0x107,
        "#560F#6P啊，工房长伯伯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x12,
        (
            "#802F#5P是提妲啊……\x01",
            "艾丝蒂尔也在一起啊，\x02\x03",

            "#803F听到地下有人说话，\x01",
            "我还在想是谁呢……\x02\x03",

            "#800F又发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F6")

    label("loc_596C")


    ChrTalk(    #408
        0x101,
        "#1004F#6P啊～工房长先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x12,
        (
            "#802F#5P啊，这不是艾丝蒂尔吗。\x02\x03",

            "#803F听到地下有人说话，\x01",
            "我还在想是谁呢……\x02\x03",

            "#800F又发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59F6")

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
            "#803F#5P原来如此，是这样啊。\x02\x03",

            "#806F说起汽油的话…\x01",
            "我记得１个月前还从\x01",
            "共和国订购过的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        "#1004F#6P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x102,
        (
            "#1042F#4P１个月之前的话……\x01",
            "那现在应该已经送到了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x11,
        (
            "#4P可、可是工房长…\x01",
            "我这里并没有收到那种东西啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x12,
        (
            "#803F#5P啊，等一下……\x02\x03",

            "#802F我想起来了，因为并不是太急用的\x01",
            "东西，所以是用的海上寄送。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C02")

    ChrTalk(    #415
        0x108,
        (
            "#070F#6P那就是说没有用飞船送，\x01",
            "而是使用了普通的海船吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C5C")

    ChrTalk(    #416
        0x106,
        (
            "#052F#6P海上寄送的话……\x02\x03",

            "那就是不使用飞船，\x01",
            "而使用普通的海船是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CB1")

    ChrTalk(    #417
        0x103,
        (
            "#023F#6P海运的话……\x02\x03",

            "那就是不使用飞船，\x01",
            "那就是使用普通的海船吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CB1")


    ChrTalk(    #418
        0x12,
        (
            "#803F#5P嗯，正是如此。\x02\x03",

            "#806F所以据我推算，\x01",
            "应该才刚刚送到……\x02\x03",

            "#800F嗯，也许现在\x01",
            "正在卢安\x01",
            "卸货吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x102,
        (
            "#1042F#4P原来如此……\x02\x03",

            "因为导力停止现象，\x01",
            "连运输业也受了不小的影响啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x101,
        (
            "#1006F#6P这么说的话，只要去\x01",
            "卢安的码头应该就可以拿到了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x12,
        (
            "#800F#5P嗯，应该没问题的。\x02\x03",

            "#803F啊，大家稍等一下……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #422
        (
            "\x07\x05玛多克工房长拿出纸和笔，\x01",
            "写了一封书信，并签上了自己的名字。\x02",
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
        "\x1F\x0B\x04\x07\x00收下了。\x02",
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
            "#800F#5P把这封介绍信交给卢安码头\x01",
            "的负责人就可以了。\x02\x03",

            "如果汽油已经送到的话，\x01",
            "看到我的信他就会给你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1006F#6P谢谢您了，工房长！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F73")

    ChrTalk(    #426
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "真是谢谢了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F73")


    ChrTalk(    #427
        0x102,
        "#1054F#4P真不好意思，麻烦您了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x12,
        (
            "#801F#5P什么话嘛，我虽然没博士去得勤，\x01",
            "但也算是温泉的常客了。\x02\x03",

            "身为蔡斯地区的代表，\x01",
            "这种事也是我的义务啊。\x02\x03",

            "#800F好了……\x01",
            "我要先回办公室去了。\x02\x03",

            "还有一大堆文件\x01",
            "都没有处理呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x101,
        "#1015F#6P是、是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60A2")

    ChrTalk(    #430
        0x107,
        (
            "#063F#6P那个……\x01",
            "请您别太勉强啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C8")

    label("loc_60A2")


    ChrTalk(    #431
        0x102,
        (
            "#1043F#4P……请别太\x01",
            "勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60C8")


    ChrTalk(    #432
        0x12,
        (
            "#801F#5P哈哈，等你们把水泵修好以后\x01",
            "我也会去泡温泉的。\x02\x03",

            "那就先失礼了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2010)
    OP_28(0xC2, 0x1, 0x200)
    OP_28(0xC2, 0x1, 0x400)

    def lambda_6128():

        label("loc_6128")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_6128")

    QueueWorkItem2(0xF8, 1, lambda_6128)

    def lambda_6139():

        label("loc_6139")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_6139")

    QueueWorkItem2(0xF9, 1, lambda_6139)

    def lambda_614A():

        label("loc_614A")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_614A")

    QueueWorkItem2(0x101, 1, lambda_614A)

    def lambda_615B():

        label("loc_615B")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_615B")

    QueueWorkItem2(0x102, 1, lambda_615B)

    def lambda_616C():

        label("loc_616C")

        TurnDirection(0xFE, 0x12, 400)
        OP_48()
        Jump("loc_616C")

    QueueWorkItem2(0x11, 1, lambda_616C)
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

    # Function_17_533C end

    def Function_18_61C0(): pass

    label("Function_18_61C0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61D7")
    Call(0, 28)
    Call(0, 29)

    label("loc_61D7")

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

    def lambda_6238():
        OP_6D(620, 0, -7820, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6238)

    def lambda_6250():
        OP_6E(285, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6250)
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
        "#1004F#6P呜哇……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6313")

    ChrTalk(    #434
        0x106,
        (
            "#052F#4P这是……\x01",
            "这比想象中还要漆黑啊。\x02\x03",

            "虽然已经安装上了油灯，\x01",
            "可还是没起什么作用啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_6313")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6384")

    ChrTalk(    #435
        0x103,
        (
            "#023F#4P这是……\x01",
            "比预想中还要黑暗啊。\x02\x03",

            "虽然已经安装上了油灯，\x01",
            "虽然做了些补救措施，可还是…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_6384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63F0")

    ChrTalk(    #436
        0x108,
        (
            "#073F#4P这是……\x01",
            "比想象中还要黑暗啊。\x02\x03",

            "虽然已经安装上了油灯，\x01",
            "虽然做了一些应急措施，但…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_642C")

    ChrTalk(    #437
        0x107,
        (
            "#063F#4P工房的各位\x01",
            "不知道是否还好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64AD")

    label("loc_642C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_646C")

    ChrTalk(    #438
        0x108,
        (
            "#072F#4P像现在这种状况\x01",
            "确实没办法工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64AD")

    label("loc_646C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64AD")

    ChrTalk(    #439
        0x103,
        (
            "#522F#4P现在这种状况的话\x01",
            "根本就没办法工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64AD")


    ChrTalk(    #440
        0x101,
        (
            "#1015F#6P而且……不用说，\x01",
            "导力梯肯定也不能使用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x102,
        (
            "#1035F#4P是啊。\x02\x03",

            "#1043F要想去其他楼层的话\x01",
            "就只能走紧急通路那里的楼梯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2037)
    EventEnd(0x0)
    Return()

    # Function_18_61C0 end

    def Function_19_653B(): pass

    label("Function_19_653B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -760, 0, -11540, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6562():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6562)
    OP_8E(0xFE, 0xFFFFFE16, 0x0, 0xFFFFE142, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_19_653B end

    def Function_20_659A(): pass

    label("Function_20_659A")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 320, 0, -11560, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_65C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_65C1)
    OP_8E(0xFE, 0x1F4, 0x0, 0xFFFFE0DE, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_20_659A end

    def Function_21_65F9(): pass

    label("Function_21_65F9")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -760, 0, -11540, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6620():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6620)
    OP_8E(0xFE, 0xFFFFFC04, 0x0, 0xFFFFDBA2, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6667")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_66A5")

    label("loc_6667")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_66A5")

    label("loc_668E")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_66A5")

    Return()

    # Function_21_65F9 end

    def Function_22_66A6(): pass

    label("Function_22_66A6")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 320, 0, -11560, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_66CD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66CD)
    OP_8E(0xFE, 0x14A, 0x0, 0xFFFFDB48, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6714")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6752")

    label("loc_6714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6752")

    label("loc_673B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6752")

    Return()

    # Function_22_66A6 end

    def Function_23_6753(): pass

    label("Function_23_6753")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_676A")
    Call(0, 28)
    Call(0, 29)

    label("loc_676A")

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

    def lambda_67CB():
        OP_6D(-225780, 0, 16880, 4500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_67CB)

    def lambda_67E3():
        OP_67(0, 6990, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67E3)

    def lambda_67FB():
        OP_6B(2520, 4500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_67FB)
    Sleep(2000)
    OP_43(0x101, 0x1, 0x0, 0x18)
    Sleep(600)
    OP_43(0x102, 0x1, 0x0, 0x19)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x0, 0x1A)
    Sleep(600)
    OP_43(0xF9, 0x1, 0x0, 0x1B)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #442
        0x101,
        "#1004F#4P哇……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6889")

    ChrTalk(    #443
        0x106,
        (
            "#052F#6P这是…\x01",
            "比想象中还要黑暗啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FC")

    label("loc_6889")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68C3")

    ChrTalk(    #444
        0x103,
        (
            "#023F#6P这……\x01",
            "比预想中还要黑暗啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68FC")

    label("loc_68C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68FC")

    ChrTalk(    #445
        0x108,
        (
            "#073F#6P这个……\x01",
            "比想象中还要黑暗啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_693A")

    ChrTalk(    #446
        0x107,
        (
            "#063F#6P工房中的各位\x01",
            "不知道是否还好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B9")

    label("loc_693A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_697C")

    ChrTalk(    #447
        0x108,
        (
            "#075F#6P像现在这样的状况\x01",
            "确实没办法工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69B9")

    label("loc_697C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69B9")

    ChrTalk(    #448
        0x103,
        (
            "#522F#6P这种状况的话\x01",
            "根本就没办法工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69B9")


    ChrTalk(    #449
        0x101,
        (
            "#1015F#4P而且……不用说，\x01",
            "导力梯肯定也不能使用了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x102,
        (
            "#1035F#6P是啊。\x02\x03",

            "#1043F要想去其他楼层的话\x01",
            "就只能走紧急通路那里的楼梯了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2037)
    EventEnd(0x0)
    Return()

    # Function_23_6753 end

    def Function_24_6A47(): pass

    label("Function_24_6A47")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6A6E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6A6E)
    OP_8E(0xFE, 0xFFFC8EE8, 0x0, 0x3BE2, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_24_6A47 end

    def Function_25_6AAD(): pass

    label("Function_25_6AAD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6AD4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6AD4)
    OP_8E(0xFE, 0xFFFC8EDE, 0x0, 0x3FFB, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_25_6AAD end

    def Function_26_6B13(): pass

    label("Function_26_6B13")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230500, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6B3A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6B3A)
    OP_8E(0xFE, 0xFFFC848E, 0x0, 0x3E4E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFC8A4C, 0x0, 0x3ADE, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9C")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BDA")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BC3")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BDA")

    label("loc_6BC3")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6BDA")

    Return()

    # Function_26_6B13 end

    def Function_27_6BDB(): pass

    label("Function_27_6BDB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -230000, -250, 15940, 90)
    ClearChrFlags(0xFE, 0x80)

    def lambda_6C02():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_6C02)
    OP_8E(0xFE, 0xFFFC848E, 0x0, 0x3E4E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFC89AC, 0x0, 0x4024, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C64")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6CA2")

    label("loc_6C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C8B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6CA2")

    label("loc_6C8B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6CA2")

    Return()

    # Function_27_6BDB end

    def Function_28_6CA3(): pass

    label("Function_28_6CA3")

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
        (0, "loc_6D1D"),
        (1, "loc_6D23"),
        (SWITCH_DEFAULT, "loc_6D29"),
    )


    label("loc_6D1D")

    OP_A2(0x1200)
    Jump("loc_6D29")

    label("loc_6D23")

    OP_A2(0x1201)
    Jump("loc_6D29")

    label("loc_6D29")

    Return()

    # Function_28_6CA3 end

    def Function_29_6D2A(): pass

    label("Function_29_6D2A")

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

    # Function_29_6D2A end

    def Function_30_6D83(): pass

    label("Function_30_6D83")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #451
        (
            "\x07\x05左·中央工房电梯\x01",
            "右·地下导力器工厂\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_6D83 end

    def Function_31_6DD9(): pass

    label("Function_31_6DD9")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #452
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_31_6DD9 end

    SaveToFile()

Try(main)
