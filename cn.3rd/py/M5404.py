from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5404   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5404.x',
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
        X                   = 7140,
        Z                   = 0,
        Y                   = 80150,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x294,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -360,
        Z                   = 0,
        Y                   = 4840,
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
        Y                   = -16090,
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
        X                   = -850,
        Z                   = 0,
        Y                   = -73020,
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
        X                   = 190090,
        Z                   = 0,
        Y                   = -193630,
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
        X                   = 40960,
        Z                   = 0,
        Y                   = -16180,
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
        X                   = -45030,
        Z                   = 0,
        Y                   = 2790,
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
        X                   = -124880,
        Z                   = 0,
        Y                   = -55130,
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
        X                   = -1030,
        Y                   = -1000,
        Z                   = 133840,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 1980,
        Y                   = -1000,
        Z                   = -119660,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = -28000,
        Y                   = -3000,
        Z                   = 76300,
        Range               = -26800,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x14758,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 2150,
        TriggerZ            = 0,
        TriggerY            = -119880,
        TriggerRange        = 1000,
        ActorX              = 2150,
        ActorZ              = 500,
        ActorY              = -119880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5910,
        TriggerZ            = 0,
        TriggerY            = 88840,
        TriggerRange        = 1000,
        ActorX              = 5910,
        ActorZ              = 1000,
        ActorY              = 88840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14960,
        TriggerZ            = 0,
        TriggerY            = -120950,
        TriggerRange        = 1000,
        ActorX              = 14960,
        ActorZ              = 1000,
        ActorY              = -120950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75730,
        TriggerZ            = 0,
        TriggerY            = -20940,
        TriggerRange        = 1000,
        ActorX              = 75070,
        ActorZ              = 0,
        ActorY              = -20990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 67030,
        TriggerZ            = 0,
        TriggerY            = -90240,
        TriggerRange        = 1000,
        ActorX              = 66960,
        ActorZ              = 0,
        ActorY              = -89540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69990,
        TriggerZ            = 0,
        TriggerY            = -90250,
        TriggerRange        = 1000,
        ActorX              = 70020,
        ActorZ              = 0,
        ActorY              = -89630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 73000,
        TriggerZ            = 0,
        TriggerY            = -90250,
        TriggerRange        = 1000,
        ActorX              = 72970,
        ActorZ              = 0,
        ActorY              = -89680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72970,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 73000,
        ActorZ              = 0,
        ActorY              = -98360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 69940,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 69980,
        ActorZ              = 0,
        ActorY              = -98310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 66990,
        TriggerZ            = 0,
        TriggerY            = -97700,
        TriggerRange        = 1000,
        ActorX              = 67020,
        ActorZ              = 0,
        ActorY              = -98360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68510,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 68480,
        ActorZ              = 0,
        ActorY              = -131590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72000,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 71970,
        ActorZ              = 0,
        ActorY              = -131630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75450,
        TriggerZ            = 0,
        TriggerY            = -132200,
        TriggerRange        = 1000,
        ActorX              = 75410,
        ActorZ              = 0,
        ActorY              = -131590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 75480,
        TriggerZ            = 0,
        TriggerY            = -139800,
        TriggerRange        = 1000,
        ActorX              = 75510,
        ActorZ              = 0,
        ActorY              = -140420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72040,
        TriggerZ            = 0,
        TriggerY            = -139790,
        TriggerRange        = 1000,
        ActorX              = 71980,
        ActorZ              = 0,
        ActorY              = -140460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 68470,
        TriggerZ            = 0,
        TriggerY            = -139800,
        TriggerRange        = 1000,
        ActorX              = 68510,
        ActorZ              = 0,
        ActorY              = -140460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22130,
        TriggerZ            = 100,
        TriggerY            = 79890,
        TriggerRange        = 1000,
        ActorX              = 22800,
        ActorZ              = 3000,
        ActorY              = 80000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_45E",          # 00, 0
        "Function_1_472",          # 01, 1
        "Function_2_6B5",          # 02, 2
        "Function_3_7DB",          # 03, 3
        "Function_4_901",          # 04, 4
        "Function_5_A27",          # 05, 5
        "Function_6_B4D",          # 06, 6
        "Function_7_C73",          # 07, 7
        "Function_8_D99",          # 08, 8
        "Function_9_EBF",          # 09, 9
        "Function_10_FE5",         # 0A, 10
        "Function_11_110B",        # 0B, 11
        "Function_12_1231",        # 0C, 12
        "Function_13_1357",        # 0D, 13
        "Function_14_147D",        # 0E, 14
        "Function_15_15A3",        # 0F, 15
        "Function_16_1B39",        # 10, 16
        "Function_17_1B96",        # 11, 17
        "Function_18_1BBC",        # 12, 18
        "Function_19_1BE2",        # 13, 19
        "Function_20_1BFB",        # 14, 20
        "Function_21_1C14",        # 15, 21
        "Function_22_1C88",        # 16, 22
        "Function_23_1E4F",        # 17, 23
        "Function_24_1F05",        # 18, 24
    )


    def Function_0_45E(): pass

    label("Function_0_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_471")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_471")

    Return()

    # Function_0_45E end

    def Function_1_472(): pass

    label("Function_1_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")
    OP_72(0x101D, 0x0)
    ExitThread()
    Jump("loc_487")

    label("loc_483")

    OP_64(0x0, 0x1)

    label("loc_487")

    OP_6F(0x1, 100)
    OP_72(0x201, 0x0)
    ExitThread()
    OP_BE(0x0, 0x1, 0x2, 0x3E8, 0x0, 0x2, -5600, -1000, -1500, 3600, 2000, 1500)
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
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56B")
    OP_6F(0x0, 0)
    Jump("loc_572")

    label("loc_56B")

    OP_6F(0x0, 60)

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584")
    OP_6F(0x21, 0)
    Jump("loc_58B")

    label("loc_584")

    OP_6F(0x21, 60)

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D")
    OP_6F(0x22, 0)
    Jump("loc_5A4")

    label("loc_59D")

    OP_6F(0x22, 60)

    label("loc_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6")
    OP_6F(0x23, 0)
    Jump("loc_5BD")

    label("loc_5B6")

    OP_6F(0x23, 60)

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")
    OP_6F(0x24, 0)
    Jump("loc_5D6")

    label("loc_5CF")

    OP_6F(0x24, 60)

    label("loc_5D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E8")
    OP_6F(0x25, 0)
    Jump("loc_5EF")

    label("loc_5E8")

    OP_6F(0x25, 60)

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601")
    OP_6F(0x26, 0)
    Jump("loc_608")

    label("loc_601")

    OP_6F(0x26, 60)

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61A")
    OP_6F(0x27, 0)
    Jump("loc_621")

    label("loc_61A")

    OP_6F(0x27, 60)

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633")
    OP_6F(0x28, 0)
    Jump("loc_63A")

    label("loc_633")

    OP_6F(0x28, 60)

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C")
    OP_6F(0x29, 0)
    Jump("loc_653")

    label("loc_64C")

    OP_6F(0x29, 60)

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_665")
    OP_6F(0x2A, 0)
    Jump("loc_66C")

    label("loc_665")

    OP_6F(0x2A, 60)

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E")
    OP_6F(0x2B, 0)
    Jump("loc_685")

    label("loc_67E")

    OP_6F(0x2B, 60)

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    OP_6F(0x2C, 0)
    Jump("loc_69E")

    label("loc_697")

    OP_6F(0x2C, 60)

    label("loc_69E")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6B1")
    OP_82(0x81, 0x0)
    Jump("loc_6B4")

    label("loc_6B1")

    OP_82(0x82, 0x0)

    label("loc_6B4")

    Return()

    # Function_1_472 end

    def Function_2_6B5(): pass

    label("Function_2_6B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29F, 1)"), scpexpr(EXPR_END)), "loc_729")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x9F\x02\x07\x00。\x02",
    )

    Jump("loc_70E")

    label("loc_70E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BEC)
    Jump("loc_797")

    label("loc_729")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x9F\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9F\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_778")

    label("loc_778")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_797")

    Jump("loc_7CD")

    label("loc_79A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6B5 end

    def Function_3_7DB(): pass

    label("Function_3_7DB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_84F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_834")

    label("loc_834")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BED)
    Jump("loc_8BD")

    label("loc_84F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_89E")

    label("loc_89E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_8BD")

    Jump("loc_8F3")

    label("loc_8C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8F3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7DB end

    def Function_4_901(): pass

    label("Function_4_901")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x22, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x5DB, 1)"), scpexpr(EXPR_END)), "loc_975")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xDB\x05\x07\x00。\x02",
    )

    Jump("loc_95A")

    label("loc_95A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BEE)
    Jump("loc_9E3")

    label("loc_975")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xDB\x05\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xDB\x05\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_9C4")

    label("loc_9C4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x22, 60)
    OP_70(0x22, 0x0)

    label("loc_9E3")

    Jump("loc_A19")

    label("loc_9E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A19")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_901 end

    def Function_5_A27(): pass

    label("Function_5_A27")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x23, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_A9B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    Jump("loc_A80")

    label("loc_A80")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BEF)
    Jump("loc_B09")

    label("loc_A9B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFF\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_AEA")

    label("loc_AEA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x23, 60)
    OP_70(0x23, 0x0)

    label("loc_B09")

    Jump("loc_B3F")

    label("loc_B0C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B3F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A27 end

    def Function_6_B4D(): pass

    label("Function_6_B4D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C32")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x146, 1)"), scpexpr(EXPR_END)), "loc_BC1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\x46\x01\x07\x00。\x02",
    )

    Jump("loc_BA6")

    label("loc_BA6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF0)
    Jump("loc_C2F")

    label("loc_BC1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\x46\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x46\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_C10")

    label("loc_C10")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_C2F")

    Jump("loc_C65")

    label("loc_C32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C65")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B4D end

    def Function_7_C73(): pass

    label("Function_7_C73")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D58")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_CE7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_CCC")

    label("loc_CCC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF1)
    Jump("loc_D55")

    label("loc_CE7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_D36")

    label("loc_D36")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_D55")

    Jump("loc_D8B")

    label("loc_D58")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_C73 end

    def Function_8_D99(): pass

    label("Function_8_D99")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E0D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_DF2")

    label("loc_DF2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF2)
    Jump("loc_E7B")

    label("loc_E0D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_E5C")

    label("loc_E5C")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_E7B")

    Jump("loc_EB1")

    label("loc_E7E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_EB1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_D99 end

    def Function_9_EBF(): pass

    label("Function_9_EBF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_F33")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    Jump("loc_F18")

    label("loc_F18")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF3)
    Jump("loc_FA1")

    label("loc_F33")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFA\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_F82")

    label("loc_F82")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_FA1")

    Jump("loc_FD7")

    label("loc_FA4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FD7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_EBF end

    def Function_10_FE5(): pass

    label("Function_10_FE5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10CA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_1059")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_103E")

    label("loc_103E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF4)
    Jump("loc_10C7")

    label("loc_1059")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_10A8")

    label("loc_10A8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x28, 60)
    OP_70(0x28, 0x0)

    label("loc_10C7")

    Jump("loc_10FD")

    label("loc_10CA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_10FD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_FE5 end

    def Function_11_110B(): pass

    label("Function_11_110B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2CC, 1)"), scpexpr(EXPR_END)), "loc_117F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00得到了\x1F\xCC\x02\x07\x00。\x02",
    )

    Jump("loc_1164")

    label("loc_1164")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF5)
    Jump("loc_11ED")

    label("loc_117F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "宝箱里装有\x1F\xCC\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xCC\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_11CE")

    label("loc_11CE")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_11ED")

    Jump("loc_1223")

    label("loc_11F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1223")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_110B end

    def Function_12_1231(): pass

    label("Function_12_1231")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1316")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x161, 1)"), scpexpr(EXPR_END)), "loc_12A5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\x61\x01\x07\x00。\x02",
    )

    Jump("loc_128A")

    label("loc_128A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF6)
    Jump("loc_1313")

    label("loc_12A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "宝箱里装有\x1F\x61\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x61\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_12F4")

    label("loc_12F4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_1313")

    Jump("loc_1349")

    label("loc_1316")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1349")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1231 end

    def Function_13_1357(): pass

    label("Function_13_1357")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_13CB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_13B0")

    label("loc_13B0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF7)
    Jump("loc_1439")

    label("loc_13CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_141A")

    label("loc_141A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_1439")

    Jump("loc_146F")

    label("loc_143C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_146F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1357 end

    def Function_14_147D(): pass

    label("Function_14_147D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1562")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_14F1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    Jump("loc_14D6")

    label("loc_14D6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BF8)
    Jump("loc_155F")

    label("loc_14F1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFF\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1540")

    label("loc_1540")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_155F")

    Jump("loc_1595")

    label("loc_1562")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1595")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_147D end

    def Function_15_15A3(): pass

    label("Function_15_15A3")

    TalkBegin(0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #39
        (
            "\x07\x05现在，\x01",
            "这架升降梯的使用受到限制。\x02",
        )
    )

    Jump("loc_1604")

    label("loc_1604")

    CloseMessageWindow()

    AnonymousTalk(    #40
        (
            "\x07\x05需要使用时\x01",
            "请使用最新的安全卡\x01",
            "接受认证。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 5)), scpexpr(EXPR_END)), "loc_1B2C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_165F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B29")

    Menu(
        0,
        -1,
        150,
        1,
        (
            "使用安全卡\x01",      # 0
            "不使用\x01",          # 1
        )
    )

    Jump("loc_1690")

    label("loc_1690")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C0"),
        (SWITCH_DEFAULT, "loc_1B07"),
    )


    label("loc_16C0")

    EventBegin(0x0)
    FadeToBright(300, 0)
    Fade(500)
    OP_6D(2920, 0, -121270, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(224, 0)
    SetChrPos(0x109, 1610, 0, -122630, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1762")
    SetChrPos(0x102, 1860, 0, -120850, 0)
    SetChrPos(0xF0, 400, 0, -124100, 0)
    SetChrPos(0xF1, 2040, 0, -124090, 0)
    Jump("loc_17E7")

    label("loc_1762")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A6")
    SetChrPos(0x102, 1860, 0, -120850, 0)
    SetChrPos(0xEF, 400, 0, -124100, 0)
    SetChrPos(0xF1, 2040, 0, -124090, 0)
    Jump("loc_17E7")

    label("loc_17A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E7")
    SetChrPos(0x102, 1860, 0, -120850, 0)
    SetChrPos(0xEF, 400, 0, -124100, 0)
    SetChrPos(0xF0, 2040, 0, -124090, 0)

    label("loc_17E7")

    OP_0D()
    Sleep(300)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xAA, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("合成音")

    AnonymousTalk(    #41
        "\x07\x05──认证完毕。\x02",
    )

    Jump("loc_183A")

    label("loc_183A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0xF)
    OP_73(0x1D)
    Sleep(500)

    ChrTalk(    #42
        0x102,
        "#1505F#6P好……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_190B")

    ChrTalk(    #43
        0x101,
        (
            "#1004F#12P没、没想到刚才的卡\x01",
            "居然真的可以用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x110,
        (
            "#1306F#12P单纯的巧合……\x01",
            "还是必然呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_190B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(    #45
        0x101,
        (
            "#1004F#12P没、没想到刚才的卡\x01",
            "居然真的可以用……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_1958")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(    #46
        0x110,
        (
            "#263F#12P嘻嘻……\x01",
            "刚才那大哥哥的卡\x01",
            "居然真的可以用呢。\x02\x03",

            "#1306F这是巧合？\x01",
            "还是必然呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A36")

    label("loc_19D1")


    ChrTalk(    #47
        0x109,
        (
            "#1840F#6P唔……\x01",
            "没想到那个小哥的卡\x01",
            "居然真的可以用啊……\x02\x03",

            "#1067F……这么说来………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A36")


    ChrTalk(    #48
        0x102,
        "#1503F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 400)
    Sleep(300)

    ChrTalk(    #49
        0x102,
        (
            "#1513F#5P无论如何……\x01",
            "这样就能下到机库了。\x02\x03",

            "#1500F总之先去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        "#1060F#6P啊啊……是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B26)
    OP_64(0x0, 0x1)
    Sleep(300)
    EventEnd(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B26")

    label("loc_1B07")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B26")

    label("loc_1B26")

    Jump("loc_165F")

    label("loc_1B29")

    Jump("loc_1B35")

    label("loc_1B2C")

    FadeToBright(300, 0)

    label("loc_1B35")

    TalkEnd(0xFF)
    Return()

    # Function_15_15A3 end

    def Function_16_1B39(): pass

    label("Function_16_1B39")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x05门坚固地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_1B39 end

    def Function_17_1B96(): pass

    label("Function_17_1B96")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014B, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_17_1B96 end

    def Function_18_1BBC(): pass

    label("Function_18_1BBC")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014C, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_18_1BBC end

    def Function_19_1BE2(): pass

    label("Function_19_1BE2")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A2(0x2B6F)
    OP_A3(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_19_1BE2 end

    def Function_20_1BFB(): pass

    label("Function_20_1BFB")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A2(0x2B70)
    OP_A3(0x2B71)
    Return()

    # Function_20_1BFB end

    def Function_21_1C14(): pass

    label("Function_21_1C14")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
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

    Jump("loc_1C71")

    label("loc_1C71")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_21_1C14 end

    def Function_22_1C88(): pass

    label("Function_22_1C88")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 19350, 0, 80810, 90)
    SetChrPos(0x1, 19260, 0, 78990, 90)
    SetChrPos(0x2, 17480, 0, 81000, 90)
    SetChrPos(0x3, 17110, 0, 79100, 90)
    OP_6D(20860, 100, 79920, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6B(4860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")
    OP_28(0x16, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_1D5E")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #53
        (
            "\x07\x05#40W   无『武勋』者请离去……\x01",
            " 　　　若欲获得认可，\x01",
            "     除战斗别无他法……\x01\x01",
            "   当汝等胜过４００战时，\x01",
            "　   则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x18), scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E43")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E40")
    Call(0, 23)

    label("loc_1E40")

    Jump("loc_1E43")

    label("loc_1E43")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_22_1C88 end

    def Function_23_1E4F(): pass

    label("Function_23_1E4F")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x2D, 0)
    OP_70(0x2D, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2D)
    Sleep(500)

    def lambda_1EB8():
        OP_6B(3980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1EB8)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x21, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_1E4F end

    def Function_24_1F05(): pass

    label("Function_24_1F05")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 19350, 0, 80810, 90)
    SetChrPos(0x1, 19260, 0, 78990, 90)
    SetChrPos(0x2, 17480, 0, 81000, 90)
    SetChrPos(0x3, 17110, 0, 79100, 90)
    OP_6D(20860, 100, 79920, 0)
    OP_67(0, 8119, -10000, 0)
    OP_6B(4860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_24_1F05 end

    SaveToFile()

Try(main)
