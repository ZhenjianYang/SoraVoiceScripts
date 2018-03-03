from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5509   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5509.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'ED6_DT29/CH14750 ._CH',             # 00
        'ED6_DT29/CH14751 ._CH',             # 01
        'ED6_DT29/CH14530 ._CH',             # 02
        'ED6_DT29/CH14531 ._CH',             # 03
        'ED6_DT29/CH14540 ._CH',             # 04
        'ED6_DT29/CH14541 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14750P._CP',             # 00
        'ED6_DT29/CH14751P._CP',             # 01
        'ED6_DT29/CH14530P._CP',             # 02
        'ED6_DT29/CH14531P._CP',             # 03
        'ED6_DT29/CH14540P._CP',             # 04
        'ED6_DT29/CH14541P._CP',             # 05
    )

    DeclMonster(
        X                   = 74300,
        Z                   = 0,
        Y                   = 101890,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 71450,
        Z                   = 0,
        Y                   = 71630,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 153660,
        Z                   = 0,
        Y                   = 72290,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 130419,
        Z                   = 0,
        Y                   = 96620,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x19C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 150220,
        TriggerZ            = 250,
        TriggerY            = 177090,
        TriggerRange        = 1000,
        ActorX              = 150840,
        ActorZ              = 1600,
        ActorY              = 177000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 99850,
        TriggerZ            = 0,
        TriggerY            = 152220,
        TriggerRange        = 1000,
        ActorX              = 100120,
        ActorZ              = 1500,
        ActorY              = 152220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2700,
        TriggerZ            = 0,
        TriggerY            = 108900,
        TriggerRange        = 1000,
        ActorX              = 2500,
        ActorZ              = 1300,
        ActorY              = 109010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 127010,
        TriggerZ            = 0,
        TriggerY            = 103400,
        TriggerRange        = 1000,
        ActorX              = 127010,
        ActorZ              = 1000,
        ActorY              = 103400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26000,
        TriggerZ            = 0,
        TriggerY            = 50000,
        TriggerRange        = 1000,
        ActorX              = -26000,
        ActorZ              = 1000,
        ActorY              = 50000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75000,
        TriggerZ            = 0,
        TriggerY            = 148000,
        TriggerRange        = 1000,
        ActorX              = 75000,
        ActorZ              = 1000,
        ActorY              = 148000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_223",          # 01, 1
        "Function_2_3A2",          # 02, 2
        "Function_3_504",          # 03, 3
        "Function_4_646",          # 04, 4
        "Function_5_789",          # 05, 5
        "Function_6_7ED",          # 06, 6
        "Function_7_827",          # 07, 7
        "Function_8_8C0",          # 08, 8
        "Function_9_A2F",          # 09, 9
        "Function_10_AF4",         # 0A, 10
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Return()

    # Function_0_222 end

    def Function_1_223(): pass

    label("Function_1_223")

    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286")
    OP_72(0x2011, 0x0)
    ExitThread()
    OP_72(0x811, 0x0)
    ExitThread()
    OP_6F(0x11, 0)
    OP_72(0x2012, 0x0)
    ExitThread()
    OP_72(0x812, 0x0)
    ExitThread()
    OP_6F(0x12, 0)
    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x810, 0x0)
    ExitThread()
    OP_6F(0x10, 2)
    OP_72(0x2013, 0x0)
    ExitThread()
    OP_72(0x813, 0x0)
    ExitThread()
    OP_6F(0x13, 0)
    Jump("loc_329")

    label("loc_286")

    OP_72(0x2011, 0x0)
    ExitThread()
    OP_72(0x811, 0x0)
    ExitThread()
    OP_6F(0x11, 1)
    OP_72(0x2012, 0x0)
    ExitThread()
    OP_72(0x812, 0x0)
    ExitThread()
    OP_6F(0x12, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0")
    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x810, 0x0)
    ExitThread()
    OP_6F(0x10, 0)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x2013, 0x0)
    ExitThread()
    OP_72(0x813, 0x0)
    ExitThread()
    OP_6F(0x13, 0)
    Jump("loc_329")

    label("loc_2F0")

    OP_72(0x2010, 0x0)
    ExitThread()
    OP_72(0x810, 0x0)
    ExitThread()
    OP_6F(0x10, 1)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 30)
    OP_72(0x2013, 0x0)
    ExitThread()
    OP_72(0x813, 0x0)
    ExitThread()
    OP_6F(0x13, 30)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 2)), scpexpr(EXPR_END)), "loc_356")
    OP_72(0x2033, 0x0)
    ExitThread()
    OP_72(0x833, 0x0)
    ExitThread()
    OP_6F(0x33, 1)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 60)

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368")
    OP_6F(0x15, 0)
    Jump("loc_36F")

    label("loc_368")

    OP_6F(0x15, 60)

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_381")
    OP_6F(0x14, 0)
    Jump("loc_388")

    label("loc_381")

    OP_6F(0x14, 60)

    label("loc_388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A")
    OP_6F(0x16, 0)
    Jump("loc_3A1")

    label("loc_39A")

    OP_6F(0x16, 60)

    label("loc_3A1")

    Return()

    # Function_1_223 end

    def Function_2_3A2(): pass

    label("Function_2_3A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x325, 1)"), scpexpr(EXPR_END)), "loc_410")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x25\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2980)
    Jump("loc_478")

    label("loc_410")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x25\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x25\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_478")

    Jump("loc_4F6")

    label("loc_47B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05We'd tell you to have a barrel of fun, but come on. We don't call 'em\x01",
            "treasure BARRELS.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x80, 0x0)

    label("loc_4F6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3A2 end

    def Function_3_504(): pass

    label("Function_3_504")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A3, 1)"), scpexpr(EXPR_END)), "loc_572")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA3\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29C1)
    Jump("loc_5DA")

    label("loc_572")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA3\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA3\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_5DA")

    Jump("loc_638")

    label("loc_5DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Hey again. Wait. Where's that guy you were with before?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x81, 0x0)

    label("loc_638")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_504 end

    def Function_4_646(): pass

    label("Function_4_646")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_6B4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x02\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29C2)
    Jump("loc_71C")

    label("loc_6B4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x02\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x02\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_71C")

    Jump("loc_77B")

    label("loc_71F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05There is no greater void than the one between your ears.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x82, 0x0)

    label("loc_77B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_646 end

    def Function_5_789(): pass

    label("Function_5_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")
    Call(0, 6)
    Jump("loc_7EC")

    label("loc_798")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05The flow of orbal energy has already been started.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_7EC")

    Return()

    # Function_5_789 end

    def Function_6_7ED(): pass

    label("Function_6_7ED")

    TalkBegin(0xFF)
    OP_6F(0x12, 0)
    OP_70(0x12, 0x1E)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x11, 1)
    OP_70(0x11, 0x1)
    OP_A2(0x2950)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_6_7ED end

    def Function_7_827(): pass

    label("Function_7_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x05No orbal energy is reaching here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_8BF")

    label("loc_875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_884")
    Call(0, 8)
    Jump("loc_8BF")

    label("loc_884")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05The gate is already open.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_8BF")

    Return()

    # Function_7_827 end

    def Function_8_8C0(): pass

    label("Function_8_8C0")

    EventBegin(0x0)
    Fade(500)
    OP_6D(100340, 110, 151960, 0)
    OP_67(0, 6740, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 99990, 0, 151470, 0)
    SetChrPos(0x1, 98650, 0, 150970, 45)
    SetChrPos(0x2, 100460, 0, 150350, 0)
    SetChrPos(0x3, 99300, 0, 149910, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x10, 1)
    OP_70(0x10, 0x1)
    Sleep(300)
    Fade(1000)
    OP_6D(92100, 450, 101130, 0)
    OP_67(0, 6090, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(277, 0)
    OP_0D()
    Sleep(100)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    Sleep(500)
    Fade(500)
    OP_6D(100340, 110, 151960, 0)
    OP_67(0, 6740, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_A2(0x2951)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_8_8C0 end

    def Function_9_A2F(): pass

    label("Function_9_A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x325, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        (
            "\x07\x05There's a slot to insert a card. Some kind of ID\x01",
            "seems to be required.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_AF3")

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB8")
    Call(0, 10)
    Jump("loc_AF3")

    label("loc_AB8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        "\x07\x05The gate is already open.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_AF3")

    Return()

    # Function_9_A2F end

    def Function_10_AF4(): pass

    label("Function_10_AF4")

    EventBegin(0x0)
    Fade(500)
    OP_6D(4019, 0, 108800, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B98")
    SetChrPos(0x109, 2650, 0, 107730, 0)
    SetChrPos(0x102, 1340, 0, 107670, 0)
    SetChrPos(0x103, 2820, 0, 106390, 0)
    SetChrPos(0x10A, 1530, 0, 106250, 0)
    Jump("loc_BDC")

    label("loc_B98")

    SetChrPos(0x109, 2650, 0, 107730, 0)
    SetChrPos(0x102, 1340, 0, 107670, 0)
    SetChrPos(0xF0, 2820, 0, 106390, 0)
    SetChrPos(0xF1, 1530, 0, 106250, 0)

    label("loc_BDC")

    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x33, 1)
    OP_70(0x33, 0x1)
    Sleep(500)

    def lambda_C0A():
        OP_6D(2110, 750, 112590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C0A)

    def lambda_C22():
        OP_67(0, 5090, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C22)

    def lambda_C3A():
        OP_6B(3440, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C3A)

    def lambda_C4A():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_C4A)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F2")
    OP_A2(0x290C)
    Fade(500)
    OP_6D(3340, 0, 108000, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(44000, 0)
    OP_6E(264, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB5")
    TurnDirection(0x10A, 0x103, 400)
    Sleep(300)

    ChrTalk(    #14
        0x10A,
        (
            "#1317F#6PSch-Schera...\x02\x03",

            "Is it just me, or is this place's layout waaay\x01",
            "different from the real version?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x10A, 400)
    Sleep(300)

    ChrTalk(    #15
        0x103,
        "#1534F#11PYou thought the same, too, huh?\x02",
    )

    CloseMessageWindow()

    def lambda_DB4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DB4)
    Sleep(100)
    OP_8C(0x102, 135, 400)
    Sleep(300)

    ChrTalk(    #16
        0x102,
        "#1504F#5PCompletely different, how?\x02",
    )

    CloseMessageWindow()

    def lambda_DFC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_DFC)
    Sleep(100)
    OP_8C(0x103, 0, 400)
    Sleep(300)

    ChrTalk(    #17
        0x10A,
        (
            "#812F#6PThe placement of the rooms and the corridors...\x01",
            "Everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#1520F#12PI suppose it's possible that it was remodeled\x01",
            "after Anelace used it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130B")

    label("loc_EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112C")

    ChrTalk(    #19
        0x10A,
        "#1317F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_EDB():
        TurnDirection(0xFE, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EDB)
    Sleep(100)

    def lambda_EEE():
        TurnDirection(0xFE, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EEE)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F13")
    TurnDirection(0xF1, 0x10A, 400)
    Jump("loc_F28")

    label("loc_F13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F28")
    TurnDirection(0xF0, 0x10A, 400)

    label("loc_F28")

    Sleep(200)

    ChrTalk(    #20
        0x109,
        "#1079F#5PHuh? What's up, Anelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        (
            "#813F#6PU-Umm...\x02\x03",

            "#812FI've felt like something was weird ever since we\x01",
            "got in here, and I think I finally know why.\x02\x03",

            "The layout of this building seems to be waaay\x01",
            "different from how it was when I used the real\x01",
            "thing for my training exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1504F#5PReally...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#1316F#6PYeah... Unless my memory's completely out\x01",
            "of whack, it's all been redone. The corridors,\x01",
            "the rooms... Everything.\x02\x03",

            "#810FIt's possible that it was remodeled after we\x01",
            "used it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130B")

    label("loc_112C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130B")

    ChrTalk(    #24
        0x103,
        "#1522F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_1152():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1152)
    Sleep(100)

    def lambda_1165():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1165)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    TurnDirection(0xF1, 0x103, 400)
    Jump("loc_119F")

    label("loc_118A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    TurnDirection(0xF0, 0x103, 400)

    label("loc_119F")

    Sleep(200)

    ChrTalk(    #25
        0x109,
        "#1079F#5PHuh? Something wrong, Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#1526F#6PYou could say that, yeah...\x02\x03",

            "#1522FThe layout of this building seems to be pretty\x01",
            "different to how it was when I was last here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1504F#5PReally...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#1525F#6PYeah. The placement of the rooms and the\x01",
            "corridors... Everything.\x02\x03",

            "#1527FIt's possible that it was remodeled after\x01",
            "I used it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E8")

    ChrTalk(    #29
        0x109,
        (
            "#1065F#5PWell, the sealed area's layout was completely\x01",
            "different from the real one's, too. It wouldn't\x01",
            "be the first time this has happened.\x02\x03",

            "#1063FProbably something our foes did intentionally,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_13E8")


    ChrTalk(    #30
        0x109,
        (
            "#1065F#5PWell, the sealed area's layout was completely\x01",
            "different from the real one's, too. It wouldn't\x01",
            "be the first time this has happened.\x02\x03",

            "#1063FProbably something our foes did intentionally,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B4")


    ChrTalk(    #31
        0x102,
        "#1502F#5PExactly. We'll have to be very careful.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jump("loc_153C")

    label("loc_14F2")

    Fade(500)
    OP_6D(2850, 0, 107890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    OP_0D()

    label("loc_153C")

    OP_A2(0x2952)
    EventEnd(0x0)
    Return()

    # Function_10_AF4 end

    SaveToFile()

Try(main)
