from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        "Function_3_5DE",          # 03, 3
        "Function_4_794",          # 04, 4
        "Function_5_852",          # 05, 5
        "Function_6_902",          # 06, 6
        "Function_7_A56",          # 07, 7
        "Function_8_BA3",          # 08, 8
        "Function_9_CF5",          # 09, 9
        "Function_10_E4E",         # 0A, 10
        "Function_11_F8A",         # 0B, 11
        "Function_12_10B0",        # 0C, 12
        "Function_13_11EE",        # 0D, 13
        "Function_14_148B",        # 0E, 14
        "Function_15_1728",        # 0F, 15
        "Function_16_19D4",        # 10, 16
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
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_2_585 end

    def Function_3_5DE(): pass

    label("Function_3_5DE")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4")
    OP_28(0xA, 0x4, 0x2)
    OP_82(0xAB, 0x2)
    PlayEffect(0xAC, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6B4")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05#40WBring to me the girl who entrusts \x01",
            "her feelings to her blade.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_783")
    Call(0, 2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_780")
    Call(0, 4)

    label("loc_780")

    Jump("loc_783")

    label("loc_783")

    FadeToBright(300, 0)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_3_5DE end

    def Function_4_794(): pass

    label("Function_4_794")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0xAA, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x9)
    Sleep(500)

    def lambda_7FD():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_7FD)
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

    # Function_4_794 end

    def Function_5_852(): pass

    label("Function_5_852")

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

    # Function_5_852 end

    def Function_6_902(): pass

    label("Function_6_902")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_970")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Found \x1F\x74\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298A)
    Jump("loc_9D8")

    label("loc_970")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Found \x1F\x74\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x74\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_9D8")

    Jump("loc_A48")

    label("loc_9DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Would you also like a coffee? By the way, that was a rhetorical question.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x70, 0x0)

    label("loc_A48")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_902 end

    def Function_7_A56(): pass

    label("Function_7_A56")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x614, 1)"), scpexpr(EXPR_END)), "loc_AC4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\x14\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298B)
    Jump("loc_B2C")

    label("loc_AC4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Found \x1F\x14\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x14\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_B2C")

    Jump("loc_B95")

    label("loc_B2F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Warning: Do not store children or other living creatures in chest.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x71, 0x0)

    label("loc_B95")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A56 end

    def Function_8_BA3(): pass

    label("Function_8_BA3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x527, 1)"), scpexpr(EXPR_END)), "loc_C11")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\x27\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298C)
    Jump("loc_C79")

    label("loc_C11")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\x27\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x27\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_C79")

    Jump("loc_CE7")

    label("loc_C7C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05I'm glad I'm not a pirate chest. Those ARRR usually buried underground.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x72, 0x0)

    label("loc_CE7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_BA3 end

    def Function_9_CF5(): pass

    label("Function_9_CF5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_D63")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Found \x1F\xFE\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298D)
    Jump("loc_DCB")

    label("loc_D63")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Found \x1F\xFE\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFE\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_DCB")

    Jump("loc_E40")

    label("loc_DCE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Ohhh, you found my treasure. What, you want a medal? Perhaps in\x01",
            "another chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x73, 0x0)

    label("loc_E40")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_CF5 end

    def Function_10_E4E(): pass

    label("Function_10_E4E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x298, 1)"), scpexpr(EXPR_END)), "loc_EBC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05Found \x1F\x98\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298E)
    Jump("loc_F24")

    label("loc_EBC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Found \x1F\x98\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x98\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_F24")

    Jump("loc_F7C")

    label("loc_F27")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Oh, gosh! I usually only open up to my therapist.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x74, 0x0)

    label("loc_F7C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_E4E end

    def Function_11_F8A(): pass

    label("Function_11_F8A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x531, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1063")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_FF8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05Found \x1F\x6E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x298F)
    Jump("loc_1060")

    label("loc_FF8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05Found \x1F\x6E\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6E\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xF, 60)
    OP_70(0xF, 0x0)

    label("loc_1060")

    Jump("loc_10A2")

    label("loc_1063")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05Chest will remember that...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x75, 0x0)

    label("loc_10A2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_F8A end

    def Function_12_10B0(): pass

    label("Function_12_10B0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x532, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1189")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x10, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A2, 1)"), scpexpr(EXPR_END)), "loc_111E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\xA2\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2990)
    Jump("loc_1186")

    label("loc_111E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\xA2\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA2\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x10, 60)
    OP_70(0x10, 0x0)

    label("loc_1186")

    Jump("loc_11E0")

    label("loc_1189")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Joke's on you. This treasure wasn't tax deductible.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x76, 0x0)

    label("loc_11E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_10B0 end

    def Function_13_11EE(): pass

    label("Function_13_11EE")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BE")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DD")
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
    Jump("loc_13BB")

    label("loc_12DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BB")
    OP_6F(0x5, 100)
    OP_70(0x5, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x2969)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1392")
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
    Jump("loc_13BB")

    label("loc_1392")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_13BB")

    Jump("loc_1483")

    label("loc_13BE")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 0)), scpexpr(EXPR_END)), "loc_1463")
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
    Jump("loc_1483")

    label("loc_1463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 1)), scpexpr(EXPR_END)), "loc_1483")
    OP_6F(0x5, 160)
    OP_70(0x5, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x2969)

    label("loc_1483")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_13_11EE end

    def Function_14_148B(): pass

    label("Function_14_148B")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165B")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157A")
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
    Jump("loc_1658")

    label("loc_157A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1658")
    OP_6F(0x1, 100)
    OP_70(0x1, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x296B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162F")
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
    Jump("loc_1658")

    label("loc_162F")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1658")

    Jump("loc_1720")

    label("loc_165B")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 2)), scpexpr(EXPR_END)), "loc_1700")
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
    Jump("loc_1720")

    label("loc_1700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 3)), scpexpr(EXPR_END)), "loc_1720")
    OP_6F(0x1, 160)
    OP_70(0x1, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A3(0x296B)

    label("loc_1720")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_14_148B end

    def Function_15_1728(): pass

    label("Function_15_1728")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FD")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1892")
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x296C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1866")
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
    Jump("loc_188F")

    label("loc_1866")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_188F")

    Jump("loc_18FA")

    label("loc_1892")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18FA")
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

    label("loc_18FA")

    Jump("loc_19CC")

    label("loc_18FD")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 4)), scpexpr(EXPR_END)), "loc_196A")
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A3(0x296C)
    Jump("loc_19CC")

    label("loc_196A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 5)), scpexpr(EXPR_END)), "loc_19CC")
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

    label("loc_19CC")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_15_1728 end

    def Function_16_19D4(): pass

    label("Function_16_19D4")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A80")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Lower Lever\x01",      # 0
            "Cancel\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A7D")
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x104)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x8)
    OP_A2(0x296E)

    label("loc_1A7D")

    Jump("loc_1AF9")

    label("loc_1A80")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF9")
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_6F(0x8, 260)
    OP_70(0x8, 0x0)
    OP_22(0x6C, 0x0, 0x64)
    OP_73(0x8)
    OP_A3(0x296E)

    label("loc_1AF9")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_16_19D4 end

    SaveToFile()

Try(main)
