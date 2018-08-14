from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5502   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5502.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH14540 ._CH',             # 00
        'ED6_DT29/CH14541 ._CH',             # 01
        'ED6_DT29/CH14860 ._CH',             # 02
        'ED6_DT29/CH14861 ._CH',             # 03
        'ED6_DT29/CH15000 ._CH',             # 04
        'ED6_DT29/CH15000 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14860P._CP',             # 02
        'ED6_DT29/CH14861P._CP',             # 03
        'ED6_DT29/CH15000P._CP',             # 04
        'ED6_DT29/CH15000P._CP',             # 05
    )

    DeclMonster(
        X                   = -13470,
        Z                   = 0,
        Y                   = 140030,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28680,
        Z                   = 0,
        Y                   = 140220,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28890,
        Z                   = -2000,
        Y                   = 164010,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -49000,
        Z                   = -2000,
        Y                   = 186310,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42420,
        Z                   = -2000,
        Y                   = 155960,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x192,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11290,
        Z                   = 0,
        Y                   = 136290,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28580,
        Z                   = 0,
        Y                   = 189650,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13930,
        Z                   = 0,
        Y                   = 177410,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -39160,
        TriggerZ            = 0,
        TriggerY            = 171820,
        TriggerRange        = 1000,
        ActorX              = -39000,
        ActorZ              = 3000,
        ActorY              = 173000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1160,
        TriggerZ            = 0,
        TriggerY            = 144370,
        TriggerRange        = 1700,
        ActorX              = -1160,
        ActorZ              = 2500,
        ActorY              = 144370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 169110,
        TriggerRange        = 1700,
        ActorX              = -13210,
        ActorZ              = 2500,
        ActorY              = 169110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4340,
        TriggerZ            = 0,
        TriggerY            = 181980,
        TriggerRange        = 1700,
        ActorX              = 4340,
        ActorZ              = 2500,
        ActorY              = 181980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30880,
        TriggerZ            = 0,
        TriggerY            = 150510,
        TriggerRange        = 1700,
        ActorX              = -30880,
        ActorZ              = 2500,
        ActorY              = 150510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11070,
        TriggerZ            = 0,
        TriggerY            = 153710,
        TriggerRange        = 1000,
        ActorX              = 11070,
        ActorZ              = 1000,
        ActorY              = 153210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6620,
        TriggerZ            = 0,
        TriggerY            = 158960,
        TriggerRange        = 1000,
        ActorX              = -6120,
        ActorZ              = 1000,
        ActorY              = 158960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36970,
        TriggerZ            = 0,
        TriggerY            = 185460,
        TriggerRange        = 1000,
        ActorX              = -37010,
        ActorZ              = 1000,
        ActorY              = 184950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28170,
        TriggerZ            = 0,
        TriggerY            = 192710,
        TriggerRange        = 1000,
        ActorX              = -28170,
        ActorZ              = 1000,
        ActorY              = 192710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15870,
        TriggerZ            = -2000,
        TriggerY            = 171140,
        TriggerRange        = 1000,
        ActorX              = -15870,
        ActorZ              = -1000,
        ActorY              = 171140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -46110,
        TriggerZ            = -2000,
        TriggerY            = 192500,
        TriggerRange        = 1000,
        ActorX              = -46110,
        ActorZ              = -1000,
        ActorY              = 192500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -40490,
        TriggerZ            = 0,
        TriggerY            = 151090,
        TriggerRange        = 1000,
        ActorX              = -40490,
        ActorZ              = 1000,
        ActorY              = 151090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_37E",          # 01, 1
        "Function_2_585",          # 02, 2
        "Function_3_5F9",          # 03, 3
        "Function_4_7A4",          # 04, 4
        "Function_5_862",          # 05, 5
        "Function_6_912",          # 06, 6
        "Function_7_A38",          # 07, 7
        "Function_8_B5E",          # 08, 8
        "Function_9_C84",          # 09, 9
        "Function_10_DAA",         # 0A, 10
        "Function_11_ED0",         # 0B, 11
        "Function_12_FF6",         # 0C, 12
        "Function_13_111C",        # 0D, 13
        "Function_14_13C0",        # 0E, 14
        "Function_15_1664",        # 0F, 15
        "Function_16_1917",        # 10, 16
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_37D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_37D")

    Return()

    # Function_0_36A end

    def Function_1_37E(): pass

    label("Function_1_37E")

    OP_BE(0x0, 0x1, 0x3, 0x190, 0x0, 0x3, -1900, 0, 0, 0, 0, 0)
    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0xAA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3DE")
    OP_82(0xAB, 0x0)
    Jump("loc_3E1")

    label("loc_3DE")

    OP_82(0xAC, 0x0)

    label("loc_3E1")

    OP_72(0x2800, 0x0)
    ExitThread()
    OP_72(0x2801, 0x0)
    ExitThread()
    OP_72(0x2802, 0x0)
    ExitThread()
    OP_72(0x2803, 0x0)
    ExitThread()
    OP_72(0x2804, 0x0)
    ExitThread()
    OP_72(0x2805, 0x0)
    ExitThread()
    OP_72(0x2806, 0x0)
    ExitThread()
    OP_72(0x2808, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 0)), scpexpr(EXPR_END)), "loc_426")
    OP_6F(0x0, 120)
    OP_6F(0x5, 60)

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 1)), scpexpr(EXPR_END)), "loc_434")
    OP_6F(0x5, 160)

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 2)), scpexpr(EXPR_END)), "loc_449")
    OP_6F(0x2, 120)
    OP_6F(0x1, 60)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 3)), scpexpr(EXPR_END)), "loc_457")
    OP_6F(0x1, 160)

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 4)), scpexpr(EXPR_END)), "loc_465")
    OP_6F(0x4, 60)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 5)), scpexpr(EXPR_END)), "loc_47A")
    OP_6F(0x3, 120)
    OP_6F(0x4, 160)

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 6)), scpexpr(EXPR_END)), "loc_48F")
    OP_6F(0x6, 60)
    OP_6F(0x8, 260)

    label("loc_48F")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB")
    OP_6F(0xA, 0)
    Jump("loc_4B2")

    label("loc_4AB")

    OP_6F(0xA, 60)

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C4")
    OP_6F(0xB, 0)
    Jump("loc_4CB")

    label("loc_4C4")

    OP_6F(0xB, 60)

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DD")
    OP_6F(0xC, 0)
    Jump("loc_4E4")

    label("loc_4DD")

    OP_6F(0xC, 60)

    label("loc_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6")
    OP_6F(0xD, 0)
    Jump("loc_4FD")

    label("loc_4F6")

    OP_6F(0xD, 60)

    label("loc_4FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F")
    OP_6F(0xE, 0)
    Jump("loc_516")

    label("loc_50F")

    OP_6F(0xE, 60)

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528")
    OP_6F(0xF, 0)
    Jump("loc_52F")

    label("loc_528")

    OP_6F(0xF, 60)

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    OP_6F(0x10, 0)
    Jump("loc_548")

    label("loc_541")

    OP_6F(0x10, 60)

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A")
    OP_64(0x5, 0x1)
    OP_71(0x40A, 0x0)
    ExitThread()

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C")
    OP_64(0x6, 0x1)
    OP_71(0x40B, 0x0)
    ExitThread()

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E")
    OP_64(0x7, 0x1)
    OP_71(0x40C, 0x0)
    ExitThread()

    label("loc_57E")

    OP_72(0x405, 0x0)
    ExitThread()
    Return()

    # Function_1_37E end

    def Function_2_585(): pass

    label("Function_2_585")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_5E2")

    label("loc_5E2")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_2_585 end

    def Function_3_5F9(): pass

    label("Function_3_5F9")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -38560, 0, 170190, 0)
    SetChrPos(0x1, -40150, 0, 170270, 0)
    SetChrPos(0x2, -38770, 0, 168450, 0)
    SetChrPos(0x3, -40390, 0, 168420, 0)
    OP_6D(-39230, 0, 171690, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF")
    OP_28(0xA, 0x4, 0x2)
    OP_82(0xAB, 0x2)
    PlayEffect(0xAC, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6CF")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05#40W 汝须将心愿寄托于白刃之少女\x01",
            "　　   引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_793")
    Call(0, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_790")
    Call(0, 4)

    label("loc_790")

    Jump("loc_793")

    label("loc_793")

    FadeToBright(300, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_5F9 end

    def Function_4_7A4(): pass

    label("Function_4_7A4")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0xAA, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x9)
    Sleep(500)

    def lambda_80D():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_80D)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    ClearMapFlags(0x100000)
    OP_23(0x85)
    OP_E3(0x0, 0x12, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7A4 end

    def Function_5_862(): pass

    label("Function_5_862")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -38560, 0, 170190, 0)
    SetChrPos(0x1, -40150, 0, 170270, 0)
    SetChrPos(0x2, -38770, 0, 168450, 0)
    SetChrPos(0x3, -40390, 0, 168420, 0)
    OP_6D(-39230, 0, 171690, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_5_862 end

    def Function_6_912(): pass

    label("Function_6_912")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_986")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\x74\x00\x07\x00。\x02",
    )

    Jump("loc_96B")

    label("loc_96B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298A)
    Jump("loc_9F4")

    label("loc_986")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\x74\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x74\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_9D5")

    label("loc_9D5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_9F4")

    Jump("loc_A2A")

    label("loc_9F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A2A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_912 end

    def Function_7_A38(): pass

    label("Function_7_A38")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x614, 1)"), scpexpr(EXPR_END)), "loc_AAC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x14\x06\x07\x00。\x02",
    )

    Jump("loc_A91")

    label("loc_A91")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298B)
    Jump("loc_B1A")

    label("loc_AAC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x14\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x14\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_AFB")

    label("loc_AFB")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_B1A")

    Jump("loc_B50")

    label("loc_B1D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B50")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A38 end

    def Function_8_B5E(): pass

    label("Function_8_B5E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C43")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x527, 1)"), scpexpr(EXPR_END)), "loc_BD2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\x27\x05\x07\x00。\x02",
    )

    Jump("loc_BB7")

    label("loc_BB7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298C)
    Jump("loc_C40")

    label("loc_BD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\x27\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x27\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_C21")

    label("loc_C21")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_C40")

    Jump("loc_C76")

    label("loc_C43")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C76")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_B5E end

    def Function_9_C84(): pass

    label("Function_9_C84")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D69")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_CF8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_CDD")

    label("loc_CDD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298D)
    Jump("loc_D66")

    label("loc_CF8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_D47")

    label("loc_D47")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_D66")

    Jump("loc_D9C")

    label("loc_D69")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C84 end

    def Function_10_DAA(): pass

    label("Function_10_DAA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x298, 1)"), scpexpr(EXPR_END)), "loc_E1E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\x98\x02\x07\x00。\x02",
    )

    Jump("loc_E03")

    label("loc_E03")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298E)
    Jump("loc_E8C")

    label("loc_E1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\x98\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x98\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_E6D")

    label("loc_E6D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_E8C")

    Jump("loc_EC2")

    label("loc_E8F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EC2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_DAA end

    def Function_11_ED0(): pass

    label("Function_11_ED0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_F44")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x6E\x01\x07\x00。\x02",
    )

    Jump("loc_F29")

    label("loc_F29")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298F)
    Jump("loc_FB2")

    label("loc_F44")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x6E\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6E\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_F93")

    label("loc_F93")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_FB2")

    Jump("loc_FE8")

    label("loc_FB5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FE8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_ED0 end

    def Function_12_FF6(): pass

    label("Function_12_FF6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A2, 1)"), scpexpr(EXPR_END)), "loc_106A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xA2\x01\x07\x00。\x02",
    )

    Jump("loc_104F")

    label("loc_104F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2990)
    Jump("loc_10D8")

    label("loc_106A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xA2\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA2\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_10B9")

    label("loc_10B9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_10D8")

    Jump("loc_110E")

    label("loc_10DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_110E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_FF6 end

    def Function_13_111C(): pass

    label("Function_13_111C")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FC")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    Jump("loc_11A3")

    label("loc_11A3")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121A")
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2968)
    Sleep(500)
    OP_6D(3880, 0, 135860, 1000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_12F9")

    label("loc_121A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F9")
    OP_6F(0x5, 100)
    OP_70(0x5, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2969)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CF")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(11070, 0, 153210, 1200)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, 11070, 0, 153210, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_A2(0x2972)
    OP_65(0x5, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_12F9")

    label("loc_12CF")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05什么也没有发生。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_12F9")

    Jump("loc_13B8")

    label("loc_12FC")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_131F")

    label("loc_131F")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 0)), scpexpr(EXPR_END)), "loc_1398")
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_6D(3880, 0, 135860, 1000)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x2968)
    Jump("loc_13B8")

    label("loc_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 1)), scpexpr(EXPR_END)), "loc_13B8")
    OP_6F(0x5, 160)
    OP_70(0x5, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x2969)

    label("loc_13B8")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_13_111C end

    def Function_14_13C0(): pass

    label("Function_14_13C0")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A0")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    Jump("loc_1447")

    label("loc_1447")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BE")
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x296A)
    Sleep(500)
    OP_6D(-12270, 0, 174500, 1000)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_159D")

    label("loc_14BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159D")
    OP_6F(0x1, 100)
    OP_70(0x1, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x296B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1573")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(-6120, 0, 158960, 1000)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, -6120, 0, 158960, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_A2(0x2973)
    OP_65(0x6, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_159D")

    label("loc_1573")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05什么也没有发生。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_159D")

    Jump("loc_165C")

    label("loc_15A0")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_15C3")

    label("loc_15C3")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 2)), scpexpr(EXPR_END)), "loc_163C")
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_6D(-12270, 0, 174500, 1000)
    OP_6F(0x2, 120)
    OP_70(0x2, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x296A)
    Jump("loc_165C")

    label("loc_163C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 3)), scpexpr(EXPR_END)), "loc_165C")
    OP_6F(0x1, 160)
    OP_70(0x1, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A3(0x296B)

    label("loc_165C")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_14_13C0 end

    def Function_15_1664(): pass

    label("Function_15_1664")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1849")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉到右边\x01",      # 0
            "拉到左边\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    Jump("loc_16EB")

    label("loc_16EB")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DE")
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x296C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(-37010, 0, 184950, 2500)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, -37010, 0, 184950, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_A2(0x2974)
    OP_65(0x7, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_17DB")

    label("loc_17B1")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05什么也没有发生。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_17DB")

    Jump("loc_1846")

    label("loc_17DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1846")
    OP_6F(0x4, 100)
    OP_70(0x4, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x296D)
    Sleep(500)
    OP_6D(-8090, -60, 183030, 1000)
    Sleep(300)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_1846")

    Jump("loc_190F")

    label("loc_1849")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_186C")

    label("loc_186C")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 4)), scpexpr(EXPR_END)), "loc_18AD")
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A3(0x296C)
    Jump("loc_190F")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 5)), scpexpr(EXPR_END)), "loc_190F")
    OP_6F(0x4, 160)
    OP_70(0x4, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    Sleep(500)
    OP_6D(-8090, -60, 183030, 1000)
    Sleep(300)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x296D)

    label("loc_190F")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_15_1664 end

    def Function_16_1917(): pass

    label("Function_16_1917")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05有一个看似可以拉动的控制杆。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")

    Menu(
        0,
        10,
        100,
        1,
        (
            "拉下控制杆\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    Jump("loc_197A")

    label("loc_197A")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C7")
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x104)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x8)
    OP_A2(0x296E)

    label("loc_19C7")

    Jump("loc_1A3A")

    label("loc_19CA")


    Menu(
        0,
        10,
        100,
        1,
        (
            "恢复到起始位置\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    Jump("loc_19ED")

    label("loc_19ED")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3A")
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_6F(0x8, 260)
    OP_70(0x8, 0x0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x8)
    OP_A3(0x296E)

    label("loc_1A3A")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_16_1917 end

    SaveToFile()

Try(main)
