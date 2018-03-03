from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5402   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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
        'ED6_DT29/CH15020 ._CH',             # 00
        'ED6_DT29/CH15021 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH15020P._CP',             # 00
        'ED6_DT29/CH15021P._CP',             # 01
    )

    DeclMonster(
        X                   = -930,
        Z                   = 0,
        Y                   = 20350,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 91770,
        Z                   = 0,
        Y                   = 23560,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 145970,
        Z                   = 0,
        Y                   = -97810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91300,
        Z                   = 0,
        Y                   = 23120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -144320,
        Z                   = 0,
        Y                   = -55930,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x299,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 110,
        Y                   = -1000,
        Z                   = 82080,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = 1610,
        TriggerZ            = 0,
        TriggerY            = -19170,
        TriggerRange        = 1000,
        ActorX              = 2500,
        ActorZ              = 3000,
        ActorY              = -19000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5030,
        TriggerZ            = 0,
        TriggerY            = 76990,
        TriggerRange        = 1000,
        ActorX              = 5030,
        ActorZ              = 1000,
        ActorY              = 76990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 17980,
        TriggerRange        = 1000,
        ActorX              = -49910,
        ActorZ              = 0,
        ActorY              = 18010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 14500,
        TriggerRange        = 1000,
        ActorX              = -49920,
        ActorZ              = 0,
        ActorY              = 14540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -49300,
        TriggerZ            = 0,
        TriggerY            = 21480,
        TriggerRange        = 1000,
        ActorX              = -49960,
        ActorZ              = 0,
        ActorY              = 21520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41020,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 41020,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38540,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 38540,
        ActorZ              = 0,
        ActorY              = -23040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43460,
        TriggerZ            = 0,
        TriggerY            = -23700,
        TriggerRange        = 1000,
        ActorX              = 43550,
        ActorZ              = 0,
        ActorY              = -23000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -48700,
        TriggerZ            = 0,
        TriggerY            = -27980,
        TriggerRange        = 1000,
        ActorX              = -48040,
        ActorZ              = 0,
        ActorY              = -27980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 23490,
        TriggerRange        = 1000,
        ActorX              = 48450,
        ActorZ              = 0,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47790,
        TriggerZ            = 0,
        TriggerY            = 19970,
        TriggerRange        = 1000,
        ActorX              = 48410,
        ActorZ              = 0,
        ActorY              = 19980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 47800,
        TriggerZ            = 0,
        TriggerY            = 16490,
        TriggerRange        = 1000,
        ActorX              = 48460,
        ActorZ              = 0,
        ActorY              = 16460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_316",          # 00, 0
        "Function_1_32A",          # 01, 1
        "Function_2_505",          # 02, 2
        "Function_3_5CD",          # 03, 3
        "Function_4_700",          # 04, 4
        "Function_5_826",          # 05, 5
        "Function_6_98B",          # 06, 6
        "Function_7_AEA",          # 07, 7
        "Function_8_C12",          # 08, 8
        "Function_9_D86",          # 09, 9
        "Function_10_EC3",         # 0A, 10
        "Function_11_101B",        # 0B, 11
        "Function_12_1173",        # 0C, 12
        "Function_13_11CC",        # 0D, 13
        "Function_14_14F1",        # 0E, 14
        "Function_15_15A7",        # 0F, 15
        "Function_16_1652",        # 10, 16
        "Function_17_1678",        # 11, 17
    )


    def Function_0_316(): pass

    label("Function_0_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_329")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_329")

    Return()

    # Function_0_316 end

    def Function_1_32A(): pass

    label("Function_1_32A")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_33D")
    OP_82(0x81, 0x0)
    Jump("loc_340")

    label("loc_33D")

    OP_82(0x82, 0x0)

    label("loc_340")

    OP_6F(0x1, 100)
    OP_72(0x201, 0x0)
    ExitThread()
    OP_BE(0x1, 0x1, 0x2, 0x3E8, 0x0, 0x2, -5600, -1000, -27500, 3600, 2000, -24500)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_71(0x200, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_71(0x202, 0x0)
    ExitThread()
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_72(0x803, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_71(0x203, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_72(0x804, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_71(0x204, 0x0)
    ExitThread()
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C")
    OP_6F(0x1A, 0)
    Jump("loc_423")

    label("loc_41C")

    OP_6F(0x1A, 60)

    label("loc_423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435")
    OP_6F(0x1B, 0)
    Jump("loc_43C")

    label("loc_435")

    OP_6F(0x1B, 60)

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E")
    OP_6F(0x1C, 0)
    Jump("loc_455")

    label("loc_44E")

    OP_6F(0x1C, 60)

    label("loc_455")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    OP_6F(0x1D, 0)
    Jump("loc_46E")

    label("loc_467")

    OP_6F(0x1D, 60)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480")
    OP_6F(0x1E, 0)
    Jump("loc_487")

    label("loc_480")

    OP_6F(0x1E, 60)

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    OP_6F(0x1F, 0)
    Jump("loc_4A0")

    label("loc_499")

    OP_6F(0x1F, 60)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2")
    OP_6F(0x20, 0)
    Jump("loc_4B9")

    label("loc_4B2")

    OP_6F(0x20, 60)

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB")
    OP_6F(0x27, 0)
    Jump("loc_4D2")

    label("loc_4CB")

    OP_6F(0x27, 60)

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E4")
    OP_6F(0x28, 0)
    Jump("loc_4EB")

    label("loc_4E4")

    OP_6F(0x28, 60)

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD")
    OP_6F(0x29, 0)
    Jump("loc_504")

    label("loc_4FD")

    OP_6F(0x29, 60)

    label("loc_504")

    Return()

    # Function_1_32A end

    def Function_2_505(): pass

    label("Function_2_505")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x1E)
    OP_73(0x1A)
    OP_6F(0x1A, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #0
        "\x07\x05Obtained \x07\x025000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BD0)
    Jump("loc_5B6")

    label("loc_571")


    AnonymousTalk(    #1
        "\x07\x05Mirror, mirror on the wall, where's my loot? Who took it all?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5B6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x43, 0x0)
    Return()

    # Function_2_505 end

    def Function_3_5CD(): pass

    label("Function_3_5CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D6, 1)"), scpexpr(EXPR_END)), "loc_63B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Found \x1F\xD6\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD1)
    Jump("loc_6A3")

    label("loc_63B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Found \x1F\xD6\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xD6\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_6A3")

    Jump("loc_6F2")

    label("loc_6A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05I-I... I can't think of anything to say!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x44, 0x0)

    label("loc_6F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5CD end

    def Function_4_700(): pass

    label("Function_4_700")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x149, 1)"), scpexpr(EXPR_END)), "loc_76E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\x49\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD2)
    Jump("loc_7D6")

    label("loc_76E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Found \x1F\x49\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x49\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_7D6")

    Jump("loc_818")

    label("loc_7D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Hey! Nice to see you again!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x45, 0x0)

    label("loc_818")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_700 end

    def Function_5_826(): pass

    label("Function_5_826")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x140, 1)"), scpexpr(EXPR_END)), "loc_894")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\x40\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD3)
    Jump("loc_8FC")

    label("loc_894")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\x40\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x40\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_8FC")

    Jump("loc_97D")

    label("loc_8FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05My brethren warned me of your arrival. You are 'The One Who Checks All\x01",
            "Chests Twice,' yes?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x46, 0x0)

    label("loc_97D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_826 end

    def Function_6_98B(): pass

    label("Function_6_98B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x1E)
    OP_73(0x1E)
    OP_6F(0x1E, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #11
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BD4)
    Jump("loc_AD3")

    label("loc_A9B")


    AnonymousTalk(    #12
        "\x07\x05Have I ever told you the definition of insanity?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_AD3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x47, 0x0)
    Return()

    # Function_6_98B end

    def Function_7_AEA(): pass

    label("Function_7_AEA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_B58")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05Found \x1F\xFB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD5)
    Jump("loc_BC0")

    label("loc_B58")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05Found \x1F\xFB\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFB\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_BC0")

    Jump("loc_C04")

    label("loc_BC3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05At least buy me dinner first!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x48, 0x0)

    label("loc_C04")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AEA end

    def Function_8_C12(): pass

    label("Function_8_C12")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E3, 1)"), scpexpr(EXPR_END)), "loc_C80")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Found \x1F\xE3\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD6)
    Jump("loc_CE8")

    label("loc_C80")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05Found \x1F\xE3\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xE3\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_CE8")

    Jump("loc_D78")

    label("loc_CEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05If a treasure chest is opened in a forest and there's no adventurer there\x01",
            "to check it, is it still empty?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x49, 0x0)

    label("loc_D78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C12 end

    def Function_9_D86(): pass

    label("Function_9_D86")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_DF4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05Found \x1F\xFC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD7)
    Jump("loc_E5C")

    label("loc_DF4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Found \x1F\xFC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_E5C")

    Jump("loc_EB5")

    label("loc_E5F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05By the way, where did you find the key to open me?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x4A, 0x0)

    label("loc_EB5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D86 end

    def Function_10_EC3(): pass

    label("Function_10_EC3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D3, 1)"), scpexpr(EXPR_END)), "loc_F31")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Found \x1F\xD3\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BD8)
    Jump("loc_F99")

    label("loc_F31")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05Found \x1F\xD3\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xD3\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_F99")

    Jump("loc_100D")

    label("loc_F9C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05There is one thing I wanna know at this time: is Oliver being an idiot again?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x4B, 0x0)

    label("loc_100D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_EC3 end

    def Function_11_101B(): pass

    label("Function_11_101B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x1E)
    OP_73(0x29)
    OP_6F(0x29, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #25
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x200\x01",
            "#57IWater Sepith x200\x01",
            "#58IFire Sepith x200\x01",
            "#59IWind Sepith x200\x01",
            "#62ITime Sepith x200\x01",
            "#60ISpace Sepith x200\x01",
            "#61IMirage Sepith x200.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BD9)
    Jump("loc_115C")

    label("loc_112B")


    AnonymousTalk(    #26
        "\x07\x05I have no vocal cords, and I must scream.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_115C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x4C, 0x0)
    Return()

    # Function_11_101B end

    def Function_12_1173(): pass

    label("Function_12_1173")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
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

    # Function_12_1173 end

    def Function_13_11CC(): pass

    label("Function_13_11CC")

    TalkBegin(0xFF)
    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -370, 0, -18710, 90)
    SetChrPos(0x1, -250, 0, -20250, 90)
    SetChrPos(0x2, -2290, 0, -18790, 90)
    SetChrPos(0x3, -2260, 0, -20480, 90)
    OP_6D(240, 0, -19190, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(4520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A5")
    OP_28(0x19, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_12A5")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_132C")

    AnonymousTalk(    #28
        (
            "\x07\x05#40WThe path has already been opened...\x01",
            "#500W \x01",
            "#40WOpen the door, and step inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_132C")


    AnonymousTalk(    #29
        (
            "\x07\x05#40WThe darkness is lit by septium's light,\x01",
            "and that light shall act as a guide to\x01",
            "all who have lost their way.\x01",
            "#500W \x01",
            "#40WPresent for me all of the mystical gems\x01",
            "that contain that light.\x01",
            "Only then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1446")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1443")
    Call(0, 14)

    label("loc_1443")

    Jump("loc_14E5")

    label("loc_1446")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x295, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x297, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x299, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x29F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2C5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x2CC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E5")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")
    Call(0, 14)

    label("loc_14E2")

    Jump("loc_14E5")

    label("loc_14E5")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_13_11CC end

    def Function_14_14F1(): pass

    label("Function_14_14F1")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2A, 0)
    OP_70(0x2A, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2A)
    Sleep(500)

    def lambda_155A():
        OP_6B(3840, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_155A)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_14F1 end

    def Function_15_15A7(): pass

    label("Function_15_15A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -370, 0, -18710, 90)
    SetChrPos(0x1, -250, 0, -20250, 90)
    SetChrPos(0x2, -2290, 0, -18790, 90)
    SetChrPos(0x3, -2260, 0, -20480, 90)
    OP_6D(240, 0, -19190, 0)
    OP_67(0, 6300, -10000, 0)
    OP_6B(4520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_15_15A7 end

    def Function_16_1652(): pass

    label("Function_16_1652")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240146, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_16_1652 end

    def Function_17_1678(): pass

    label("Function_17_1678")

    OP_A2(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_17_1678 end

    SaveToFile()

Try(main)
