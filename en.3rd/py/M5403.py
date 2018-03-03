from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5403   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5403.x',
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
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH15030 ._CH',             # 00
        'ED6_DT29/CH15030 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH15030P._CP',             # 00
        'ED6_DT29/CH15030P._CP',             # 01
    )

    DeclMonster(
        X                   = -920,
        Z                   = 0,
        Y                   = -37620,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1080,
        Z                   = 0,
        Y                   = 3080,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -800,
        Z                   = 0,
        Y                   = 32110,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82120,
        Z                   = 0,
        Y                   = 3530,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75960,
        Z                   = 0,
        Y                   = -135970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -126010,
        Z                   = 0,
        Y                   = 6020,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86970,
        Z                   = 0,
        Y                   = 6010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x295,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 0,
        Y                   = -1000,
        Z                   = 82020,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = 4960,
        TriggerZ            = 0,
        TriggerY            = 77000,
        TriggerRange        = 1000,
        ActorX              = 4960,
        ActorZ              = 1000,
        ActorY              = 77000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9080,
        TriggerZ            = 4000,
        TriggerY            = -125000,
        TriggerRange        = 1000,
        ActorX              = 9080,
        ActorZ              = 5000,
        ActorY              = -125000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42690,
        TriggerZ            = 0,
        TriggerY            = -31970,
        TriggerRange        = 1000,
        ActorX              = -42030,
        ActorZ              = 1000,
        ActorY              = -31970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 35680,
        TriggerZ            = 0,
        TriggerY            = -35010,
        TriggerRange        = 1000,
        ActorX              = 35060,
        ActorZ              = 1000,
        ActorY              = -35010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41170,
        TriggerZ            = 0,
        TriggerY            = 60740,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 60890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41200,
        TriggerZ            = 0,
        TriggerY            = 59640,
        TriggerRange        = 1000,
        ActorX              = 41740,
        ActorZ              = 1000,
        ActorY              = 59710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41220,
        TriggerZ            = 0,
        TriggerY            = 58190,
        TriggerRange        = 1000,
        ActorX              = 41930,
        ActorZ              = 1000,
        ActorY              = 58370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41190,
        TriggerZ            = 0,
        TriggerY            = 56900,
        TriggerRange        = 1000,
        ActorX              = 42060,
        ActorZ              = 1000,
        ActorY              = 57120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38140,
        TriggerZ            = 0,
        TriggerY            = 62850,
        TriggerRange        = 1000,
        ActorX              = 38130,
        ActorZ              = 1000,
        ActorY              = 63510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 38390,
        TriggerZ            = 0,
        TriggerY            = 55260,
        TriggerRange        = 1000,
        ActorX              = 38380,
        ActorZ              = 1000,
        ActorY              = 54650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 15510,
        TriggerRange        = 1000,
        ActorX              = 42260,
        ActorZ              = 0,
        ActorY              = 15480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41600,
        TriggerZ            = 0,
        TriggerY            = 12030,
        TriggerRange        = 1000,
        ActorX              = 42210,
        ActorZ              = 0,
        ActorY              = 11950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 41590,
        TriggerZ            = 0,
        TriggerY            = 8540,
        TriggerRange        = 1000,
        ActorX              = 42300,
        ActorZ              = 0,
        ActorY              = 8510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -43620,
        TriggerZ            = 0,
        TriggerY            = 17790,
        TriggerRange        = 1000,
        ActorX              = -43660,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39950,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -39990,
        ActorZ              = 0,
        ActorY              = 18410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36240,
        TriggerZ            = 0,
        TriggerY            = 17800,
        TriggerRange        = 1000,
        ActorX              = -36280,
        ActorZ              = 0,
        ActorY              = 18510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3DE",          # 00, 0
        "Function_1_3DF",          # 01, 1
        "Function_2_653",          # 02, 2
        "Function_3_7A7",          # 03, 3
        "Function_4_903",          # 04, 4
        "Function_5_A89",          # 05, 5
        "Function_6_BC9",          # 06, 6
        "Function_7_D07",          # 07, 7
        "Function_8_E2A",          # 08, 8
        "Function_9_F51",          # 09, 9
        "Function_10_1096",        # 0A, 10
        "Function_11_11EA",        # 0B, 11
        "Function_12_130D",        # 0C, 12
        "Function_13_1428",        # 0D, 13
        "Function_14_1562",        # 0E, 14
        "Function_15_16DC",        # 0F, 15
        "Function_16_1811",        # 10, 16
        "Function_17_1837",        # 11, 17
        "Function_18_185D",        # 12, 18
    )


    def Function_0_3DE(): pass

    label("Function_0_3DE")

    Return()

    # Function_0_3DE end

    def Function_1_3DF(): pass

    label("Function_1_3DF")

    OP_71(0x428, 0x0)
    ExitThread()
    OP_6F(0x3, 100)
    OP_72(0x203, 0x0)
    ExitThread()
    OP_BE(0x3, 0x1, 0x2, 0x3E8, 0x0, 0x2, 80690, -1000, 8260, 83470, 2000, 5400)
    OP_6F(0x4, 100)
    OP_72(0x204, 0x0)
    ExitThread()
    OP_BE(0x4, 0x1, 0x2, 0x3E8, 0x0, 0x2, -128000, -1000, 7600, -123800, 2000, 10360)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_71(0x200, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_71(0x201, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_71(0x202, 0x0)
    ExitThread()
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_72(0x805, 0x0)
    ExitThread()
    OP_6F(0x5, 0)
    OP_71(0x205, 0x0)
    ExitThread()
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_506")
    OP_6F(0x24, 0)
    Jump("loc_50D")

    label("loc_506")

    OP_6F(0x24, 60)

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F")
    OP_6F(0x25, 0)
    Jump("loc_526")

    label("loc_51F")

    OP_6F(0x25, 60)

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538")
    OP_6F(0x29, 0)
    Jump("loc_53F")

    label("loc_538")

    OP_6F(0x29, 60)

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551")
    OP_6F(0x2A, 0)
    Jump("loc_558")

    label("loc_551")

    OP_6F(0x2A, 60)

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A")
    OP_6F(0x2B, 0)
    Jump("loc_571")

    label("loc_56A")

    OP_6F(0x2B, 60)

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_583")
    OP_6F(0x2C, 0)
    Jump("loc_58A")

    label("loc_583")

    OP_6F(0x2C, 60)

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59C")
    OP_6F(0x2D, 0)
    Jump("loc_5A3")

    label("loc_59C")

    OP_6F(0x2D, 60)

    label("loc_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B5")
    OP_6F(0x2E, 0)
    Jump("loc_5BC")

    label("loc_5B5")

    OP_6F(0x2E, 60)

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE")
    OP_6F(0x2F, 0)
    Jump("loc_5D5")

    label("loc_5CE")

    OP_6F(0x2F, 60)

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7")
    OP_6F(0x30, 0)
    Jump("loc_5EE")

    label("loc_5E7")

    OP_6F(0x30, 60)

    label("loc_5EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600")
    OP_6F(0x31, 0)
    Jump("loc_607")

    label("loc_600")

    OP_6F(0x31, 60)

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_619")
    OP_6F(0x32, 0)
    Jump("loc_620")

    label("loc_619")

    OP_6F(0x32, 60)

    label("loc_620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_632")
    OP_6F(0x33, 0)
    Jump("loc_639")

    label("loc_632")

    OP_6F(0x33, 60)

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B")
    OP_6F(0x34, 0)
    Jump("loc_652")

    label("loc_64B")

    OP_6F(0x34, 60)

    label("loc_652")

    Return()

    # Function_1_3DF end

    def Function_2_653(): pass

    label("Function_2_653")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_6C1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x06\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDC)
    Jump("loc_729")

    label("loc_6C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x06\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x06\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_729")

    Jump("loc_799")

    label("loc_72C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05I get the feeling we've already met... Say, you got a twin by any chance?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x4D, 0x0)

    label("loc_799")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_653 end

    def Function_3_7A7(): pass

    label("Function_3_7A7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_880")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x478, 1)"), scpexpr(EXPR_END)), "loc_815")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x78\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDD)
    Jump("loc_87D")

    label("loc_815")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x78\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x78\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_87D")

    Jump("loc_8F5")

    label("loc_880")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05No worries! I won't tell anyone about your theft. After all, chests do not\x01",
            "speak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x4E, 0x0)

    label("loc_8F5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7A7 end

    def Function_4_903(): pass

    label("Function_4_903")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A13")
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

    AnonymousTalk(    #6
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
    OP_A2(0x2BDE)
    Jump("loc_A72")

    label("loc_A13")


    AnonymousTalk(    #7
        (
            "\x07\x05This chest has cursed you with the insatiable urge to check all the other\x01",
            "empty chests.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_A72")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x4F, 0x0)
    Return()

    # Function_4_903 end

    def Function_5_A89(): pass

    label("Function_5_A89")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B62")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x147, 1)"), scpexpr(EXPR_END)), "loc_AF7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\x47\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDF)
    Jump("loc_B5F")

    label("loc_AF7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\x47\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x47\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_B5F")

    Jump("loc_BBB")

    label("loc_B62")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Why are you leaving me open? I'm starting to be cold!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x50, 0x0)

    label("loc_BBB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A89 end

    def Function_6_BC9(): pass

    label("Function_6_BC9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_C37")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE0)
    Jump("loc_C9F")

    label("loc_C37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_C9F")

    Jump("loc_CF9")

    label("loc_CA2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05There's a note: 'Beware the carnivorous bookshelf.'\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x51, 0x0)

    label("loc_CF9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_BC9 end

    def Function_7_D07(): pass

    label("Function_7_D07")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A9, 1)"), scpexpr(EXPR_END)), "loc_D75")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05Found \x1F\xA9\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE1)
    Jump("loc_DDD")

    label("loc_D75")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Found \x1F\xA9\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA9\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_DDD")

    Jump("loc_E1C")

    label("loc_DE0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05Wood are you looking at?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x52, 0x0)

    label("loc_E1C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_D07 end

    def Function_8_E2A(): pass

    label("Function_8_E2A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F03")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_E98")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE2)
    Jump("loc_F00")

    label("loc_E98")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2D, 60)
    OP_70(0x2D, 0x0)

    label("loc_F00")

    Jump("loc_F43")

    label("loc_F03")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05hash tag treasure chest life\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x53, 0x0)

    label("loc_F43")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_E2A end

    def Function_9_F51(): pass

    label("Function_9_F51")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_FBF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\xF7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE3)
    Jump("loc_1027")

    label("loc_FBF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05Found \x1F\xF7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_1027")

    Jump("loc_1088")

    label("loc_102A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05A cascade of freshly-hatched spiders pours from the chest.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x54, 0x0)

    label("loc_1088")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_F51 end

    def Function_10_1096(): pass

    label("Function_10_1096")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1104")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE4)
    Jump("loc_116C")

    label("loc_1104")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_116C")

    Jump("loc_11DC")

    label("loc_116F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05It's you! It's really you! I'm such a huge fan!! Will you sign my chest?!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x55, 0x0)

    label("loc_11DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1096 end

    def Function_11_11EA(): pass

    label("Function_11_11EA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x30, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x617, 1)"), scpexpr(EXPR_END)), "loc_1258")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Found \x1F\x17\x06\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE5)
    Jump("loc_12C0")

    label("loc_1258")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x07\x05Found \x1F\x17\x06\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x17\x06\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x30, 60)
    OP_70(0x30, 0x0)

    label("loc_12C0")

    Jump("loc_12FF")

    label("loc_12C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Hey! I stole this first!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x56, 0x0)

    label("loc_12FF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_11EA end

    def Function_12_130D(): pass

    label("Function_12_130D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x31, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_137B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Found \x1F\xFA\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE6)
    Jump("loc_13E3")

    label("loc_137B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x05Found \x1F\xFA\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFA\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x31, 60)
    OP_70(0x31, 0x0)

    label("loc_13E3")

    Jump("loc_141A")

    label("loc_13E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05Look behind you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x57, 0x0)

    label("loc_141A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_130D end

    def Function_13_1428(): pass

    label("Function_13_1428")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1501")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x32, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_1496")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Found \x1F\x06\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE7)
    Jump("loc_14FE")

    label("loc_1496")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05Found \x1F\x06\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x06\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x32, 60)
    OP_70(0x32, 0x0)

    label("loc_14FE")

    Jump("loc_1554")

    label("loc_1501")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05Were you the one who made me feel empty inside?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x58, 0x0)

    label("loc_1554")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1428 end

    def Function_14_1562(): pass

    label("Function_14_1562")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1672")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x33, 0x1E)
    OP_73(0x33)
    OP_6F(0x33, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #35
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
    OP_A2(0x2BE8)
    Jump("loc_16C5")

    label("loc_1672")


    AnonymousTalk(    #36
        "\x07\x05Guess what my favorite tree is? Chestnut! Get it? Hahaha... I hate my life.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_16C5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x59, 0x0)
    Return()

    # Function_14_1562 end

    def Function_15_16DC(): pass

    label("Function_15_16DC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_174A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE9)
    Jump("loc_17B2")

    label("loc_174A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05Found \x1F\x04\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x04\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_17B2")

    Jump("loc_1803")

    label("loc_17B5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05Please do not disturb the sleeping mimics.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x5A, 0x0)

    label("loc_1803")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_16DC end

    def Function_16_1811(): pass

    label("Function_16_1811")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240149, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_16_1811 end

    def Function_17_1837(): pass

    label("Function_17_1837")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014A, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_17_1837 end

    def Function_18_185D(): pass

    label("Function_18_185D")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A2(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_18_185D end

    SaveToFile()

Try(main)
