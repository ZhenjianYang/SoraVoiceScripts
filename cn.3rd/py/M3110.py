from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3110   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3110.x',
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
        'ED6_DT07/CH00330 ._CH',             # 00
        'ED6_DT07/CH00331 ._CH',             # 01
        'ED6_DT07/CH00430 ._CH',             # 02
        'ED6_DT07/CH00431 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00330P._CP',             # 00
        'ED6_DT07/CH00331P._CP',             # 01
        'ED6_DT07/CH00430P._CP',             # 02
        'ED6_DT07/CH00431P._CP',             # 03
    )

    DeclMonster(
        X                   = -117810,
        Z                   = 0,
        Y                   = -4690,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -139310,
        Z                   = 0,
        Y                   = 2420,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27330,
        Z                   = 0,
        Y                   = 2970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14900,
        Z                   = 0,
        Y                   = -44370,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 69270,
        Z                   = 0,
        Y                   = -22860,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 20910,
        TriggerZ            = 0,
        TriggerY            = 262330,
        TriggerRange        = 1000,
        ActorX              = 21000,
        ActorZ              = 3000,
        ActorY              = 263000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -95810,
        TriggerZ            = 0,
        TriggerY            = 3940,
        TriggerRange        = 1000,
        ActorX              = -95810,
        ActorZ              = 1000,
        ActorY              = 3940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -106270,
        TriggerZ            = 0,
        TriggerY            = 4200,
        TriggerRange        = 1000,
        ActorX              = -106270,
        ActorZ              = 1000,
        ActorY              = 4200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -121890,
        TriggerZ            = 0,
        TriggerY            = 3090,
        TriggerRange        = 1000,
        ActorX              = -121890,
        ActorZ              = 1000,
        ActorY              = 3090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -129830,
        TriggerZ            = 0,
        TriggerY            = 2950,
        TriggerRange        = 1000,
        ActorX              = -129830,
        ActorZ              = 1000,
        ActorY              = 2950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_21E",          # 01, 1
        "Function_2_32F",          # 02, 2
        "Function_3_455",          # 03, 3
        "Function_4_57B",          # 04, 4
        "Function_5_6A1",          # 05, 5
        "Function_6_7C7",          # 06, 6
        "Function_7_7EA",          # 07, 7
        "Function_8_80D",          # 08, 8
        "Function_9_830",          # 09, 9
        "Function_10_853",         # 0A, 10
        "Function_11_876",         # 0B, 11
        "Function_12_899",         # 0C, 12
        "Function_13_90D",         # 0D, 13
        "Function_14_AB2",         # 0E, 14
        "Function_15_B68",         # 0F, 15
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_21D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_21D")

    Return()

    # Function_0_20A end

    def Function_1_21E(): pass

    label("Function_1_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_232")
    OP_72(0x101A, 0x0)
    ExitThread()
    OP_6F(0x1A, 80)

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_246")
    OP_72(0x101B, 0x0)
    ExitThread()
    OP_6F(0x1B, 80)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25A")
    OP_72(0x101C, 0x0)
    ExitThread()
    OP_6F(0x1C, 80)

    label("loc_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_26E")
    OP_72(0x101D, 0x0)
    ExitThread()
    OP_6F(0x1D, 80)

    label("loc_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_282")
    OP_72(0x101E, 0x0)
    ExitThread()
    OP_6F(0x1E, 80)

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_296")
    OP_72(0x101F, 0x0)
    ExitThread()
    OP_6F(0x1F, 80)

    label("loc_296")

    OP_1C(0x1A, 0x0, 0x6)
    OP_1C(0x1B, 0x0, 0x7)
    OP_1C(0x1C, 0x0, 0x8)
    OP_1C(0x1D, 0x0, 0x9)
    OP_1C(0x1E, 0x0, 0xA)
    OP_1C(0x1F, 0x0, 0xB)
    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2C7")
    OP_82(0x81, 0x0)
    Jump("loc_2CA")

    label("loc_2C7")

    OP_82(0x82, 0x0)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC")
    OP_6F(0x29, 0)
    Jump("loc_2E3")

    label("loc_2DC")

    OP_6F(0x29, 60)

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    OP_6F(0x2A, 0)
    Jump("loc_2FC")

    label("loc_2F5")

    OP_6F(0x2A, 60)

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E")
    OP_6F(0x2B, 0)
    Jump("loc_315")

    label("loc_30E")

    OP_6F(0x2B, 60)

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_6F(0x2C, 0)
    Jump("loc_32E")

    label("loc_327")

    OP_6F(0x2C, 60)

    label("loc_32E")

    Return()

    # Function_1_21E end

    def Function_2_32F(): pass

    label("Function_2_32F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_414")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x335, 1)"), scpexpr(EXPR_END)), "loc_3A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x35\x03\x07\x00。\x02",
    )

    Jump("loc_388")

    label("loc_388")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B84)
    Jump("loc_411")

    label("loc_3A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x35\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x35\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3F2")

    label("loc_3F2")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_411")

    Jump("loc_447")

    label("loc_414")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_447")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_32F end

    def Function_3_455(): pass

    label("Function_3_455")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A4, 1)"), scpexpr(EXPR_END)), "loc_4C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA4\x01\x07\x00。\x02",
    )

    Jump("loc_4AE")

    label("loc_4AE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B85)
    Jump("loc_537")

    label("loc_4C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA4\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA4\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_518")

    label("loc_518")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_537")

    Jump("loc_56D")

    label("loc_53A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_56D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_455 end

    def Function_4_57B(): pass

    label("Function_4_57B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_660")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_5EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_5D4")

    label("loc_5D4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B86)
    Jump("loc_65D")

    label("loc_5EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_63E")

    label("loc_63E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2B, 60)
    OP_70(0x2B, 0x0)

    label("loc_65D")

    Jump("loc_693")

    label("loc_660")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_693")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_57B end

    def Function_5_6A1(): pass

    label("Function_5_6A1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_786")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x29B, 1)"), scpexpr(EXPR_END)), "loc_715")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x9B\x02\x07\x00。\x02",
    )

    Jump("loc_6FA")

    label("loc_6FA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B87)
    Jump("loc_783")

    label("loc_715")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x9B\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x9B\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_764")

    label("loc_764")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2C, 60)
    OP_70(0x2C, 0x0)

    label("loc_783")

    Jump("loc_7B9")

    label("loc_786")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6A1 end

    def Function_6_7C7(): pass

    label("Function_6_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E9")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x0)
    OP_72(0x21A, 0x0)
    ExitThread()
    OP_72(0x101A, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_7E9")

    Return()

    # Function_6_7C7 end

    def Function_7_7EA(): pass

    label("Function_7_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80C")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x1)
    OP_72(0x21B, 0x0)
    ExitThread()
    OP_72(0x101B, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_80C")

    Return()

    # Function_7_7EA end

    def Function_8_80D(): pass

    label("Function_8_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F")
    TalkBegin(0xFF)
    Sleep(500)
    OP_A2(0x2)
    OP_72(0x21C, 0x0)
    ExitThread()
    OP_72(0x101C, 0x0)
    ExitThread()
    TalkEnd(0xFF)

    label("loc_82F")

    Return()

    # Function_8_80D end

    def Function_9_830(): pass

    label("Function_9_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21D, 0x0)
    ExitThread()
    OP_72(0x101D, 0x0)
    ExitThread()
    OP_A2(0x3)
    TalkEnd(0xFF)

    label("loc_852")

    Return()

    # Function_9_830 end

    def Function_10_853(): pass

    label("Function_10_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21E, 0x0)
    ExitThread()
    OP_72(0x101E, 0x0)
    ExitThread()
    OP_A2(0x4)
    TalkEnd(0xFF)

    label("loc_875")

    Return()

    # Function_10_853 end

    def Function_11_876(): pass

    label("Function_11_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898")
    TalkBegin(0xFF)
    Sleep(500)
    OP_72(0x21F, 0x0)
    ExitThread()
    OP_72(0x101F, 0x0)
    ExitThread()
    OP_A2(0x5)
    TalkEnd(0xFF)

    label("loc_898")

    Return()

    # Function_11_876 end

    def Function_12_899(): pass

    label("Function_12_899")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
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

    Jump("loc_8F6")

    label("loc_8F6")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_12_899 end

    def Function_13_90D(): pass

    label("Function_13_90D")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 21610, 0, 260060, 0)
    SetChrPos(0x1, 20020, 0, 260000, 0)
    SetChrPos(0x2, 21370, 0, 258140, 0)
    SetChrPos(0x3, 19670, 0, 258010, 0)
    OP_6D(19670, 0, 258010, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3910, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3")
    OP_28(0xE, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_9E3")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #13
        (
            "\x07\x05#40W　汝须将忏悔改过之忧国剑客\x01",
            "　　  引领至吾面前。\x01",
            "#500W \x01",
            "#40W　 如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA6")
    Call(0, 12)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3")
    Call(0, 14)

    label("loc_AA3")

    Jump("loc_AA6")

    label("loc_AA6")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_13_90D end

    def Function_14_AB2(): pass

    label("Function_14_AB2")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x28, 0)
    OP_70(0x28, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x28)
    Sleep(500)

    def lambda_B1B():
        OP_6B(3280, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B1B)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x14, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_AB2 end

    def Function_15_B68(): pass

    label("Function_15_B68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 21610, 0, 260060, 0)
    SetChrPos(0x1, 20020, 0, 260000, 0)
    SetChrPos(0x2, 21370, 0, 258140, 0)
    SetChrPos(0x3, 19670, 0, 258010, 0)
    OP_6D(19670, 0, 258010, 0)
    OP_67(0, 4600, -10000, 0)
    OP_6B(3910, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_15_B68 end

    SaveToFile()

Try(main)
