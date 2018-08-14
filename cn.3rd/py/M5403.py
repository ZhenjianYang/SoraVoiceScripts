from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        "Function_3_779",          # 03, 3
        "Function_4_89F",          # 04, 4
        "Function_5_9F6",          # 05, 5
        "Function_6_B1C",          # 06, 6
        "Function_7_C42",          # 07, 7
        "Function_8_D68",          # 08, 8
        "Function_9_E8E",          # 09, 9
        "Function_10_FB4",         # 0A, 10
        "Function_11_10DA",        # 0B, 11
        "Function_12_1200",        # 0C, 12
        "Function_13_1326",        # 0D, 13
        "Function_14_144C",        # 0E, 14
        "Function_15_15A1",        # 0F, 15
        "Function_16_16C1",        # 10, 16
        "Function_17_16E7",        # 11, 17
        "Function_18_170D",        # 12, 18
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_738")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_6C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_6AC")

    label("loc_6AC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDC)
    Jump("loc_735")

    label("loc_6C7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_716")

    label("loc_716")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_735")

    Jump("loc_76B")

    label("loc_738")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_76B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_653 end

    def Function_3_779(): pass

    label("Function_3_779")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x478, 1)"), scpexpr(EXPR_END)), "loc_7ED")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x78\x04\x07\x00。\x02",
    )

    Jump("loc_7D2")

    label("loc_7D2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDD)
    Jump("loc_85B")

    label("loc_7ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x78\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x78\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_83C")

    label("loc_83C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_85B")

    Jump("loc_891")

    label("loc_85E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_891")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_779 end

    def Function_4_89F(): pass

    label("Function_4_89F")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C8")
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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BDE)
    Jump("loc_9E4")

    label("loc_9C8")


    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_9E4")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_89F end

    def Function_5_9F6(): pass

    label("Function_5_9F6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x147, 1)"), scpexpr(EXPR_END)), "loc_A6A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\x47\x01\x07\x00。\x02",
    )

    Jump("loc_A4F")

    label("loc_A4F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BDF)
    Jump("loc_AD8")

    label("loc_A6A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\x47\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x47\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_AB9")

    label("loc_AB9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_AD8")

    Jump("loc_B0E")

    label("loc_ADB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B0E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_9F6 end

    def Function_6_B1C(): pass

    label("Function_6_B1C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C01")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_B90")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_B75")

    label("loc_B75")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE0)
    Jump("loc_BFE")

    label("loc_B90")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_BDF")

    label("loc_BDF")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_BFE")

    Jump("loc_C34")

    label("loc_C01")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C34")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B1C end

    def Function_7_C42(): pass

    label("Function_7_C42")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D27")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A9, 1)"), scpexpr(EXPR_END)), "loc_CB6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xA9\x01\x07\x00。\x02",
    )

    Jump("loc_C9B")

    label("loc_C9B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE1)
    Jump("loc_D24")

    label("loc_CB6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xA9\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA9\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_D05")

    label("loc_D05")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_D24")

    Jump("loc_D5A")

    label("loc_D27")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D5A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C42 end

    def Function_8_D68(): pass

    label("Function_8_D68")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_DDC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_DC1")

    label("loc_DC1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE2)
    Jump("loc_E4A")

    label("loc_DDC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_E2B")

    label("loc_E2B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2D, 60)
    OP_70(0x2D, 0x0)

    label("loc_E4A")

    Jump("loc_E80")

    label("loc_E4D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E80")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_D68 end

    def Function_9_E8E(): pass

    label("Function_9_E8E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F73")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_F02")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_EE7")

    label("loc_EE7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE3)
    Jump("loc_F70")

    label("loc_F02")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_F51")

    label("loc_F51")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_F70")

    Jump("loc_FA6")

    label("loc_F73")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FA6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_E8E end

    def Function_10_FB4(): pass

    label("Function_10_FB4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1099")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1028")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_100D")

    label("loc_100D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE4)
    Jump("loc_1096")

    label("loc_1028")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1077")

    label("loc_1077")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_1096")

    Jump("loc_10CC")

    label("loc_1099")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10CC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_FB4 end

    def Function_11_10DA(): pass

    label("Function_11_10DA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x30, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x617, 1)"), scpexpr(EXPR_END)), "loc_114E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x00得到了\x1F\x17\x06\x07\x00。\x02",
    )

    Jump("loc_1133")

    label("loc_1133")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE5)
    Jump("loc_11BC")

    label("loc_114E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "宝箱里装有\x1F\x17\x06\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x17\x06\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_119D")

    label("loc_119D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x30, 60)
    OP_70(0x30, 0x0)

    label("loc_11BC")

    Jump("loc_11F2")

    label("loc_11BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_11F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_10DA end

    def Function_12_1200(): pass

    label("Function_12_1200")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x31, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1274")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    Jump("loc_1259")

    label("loc_1259")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE6)
    Jump("loc_12E2")

    label("loc_1274")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFA\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_12C3")

    label("loc_12C3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x31, 60)
    OP_70(0x31, 0x0)

    label("loc_12E2")

    Jump("loc_1318")

    label("loc_12E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1318")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1200 end

    def Function_13_1326(): pass

    label("Function_13_1326")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_140B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x32, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_139A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x00得到了\x1F\x06\x02\x07\x00。\x02",
    )

    Jump("loc_137F")

    label("loc_137F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE7)
    Jump("loc_1408")

    label("loc_139A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "宝箱里装有\x1F\x06\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x06\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_13E9")

    label("loc_13E9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x32, 60)
    OP_70(0x32, 0x0)

    label("loc_1408")

    Jump("loc_143E")

    label("loc_140B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_143E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1326 end

    def Function_14_144C(): pass

    label("Function_14_144C")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1575")
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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BE8)
    Jump("loc_158F")

    label("loc_1575")


    AnonymousTalk(    #36
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_158F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_144C end

    def Function_15_15A1(): pass

    label("Function_15_15A1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1682")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_1613")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    Jump("loc_15F8")

    label("loc_15F8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BE9)
    Jump("loc_167F")

    label("loc_1613")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x04\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1660")

    label("loc_1660")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_167F")

    Jump("loc_16B3")

    label("loc_1682")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_16B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_15A1 end

    def Function_16_16C1(): pass

    label("Function_16_16C1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240149, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_16_16C1 end

    def Function_17_16E7(): pass

    label("Function_17_16E7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014A, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_17_16E7 end

    def Function_18_170D(): pass

    label("Function_18_170D")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A2(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_18_170D end

    SaveToFile()

Try(main)
