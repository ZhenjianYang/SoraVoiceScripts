from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        "Function_3_4C8",          # 03, 3
        "Function_4_5EE",          # 04, 4
        "Function_5_714",          # 05, 5
        "Function_6_756",          # 06, 6
        "Function_7_790",          # 07, 7
        "Function_8_80F",          # 08, 8
        "Function_9_97E",          # 09, 9
        "Function_10_A1B",         # 0A, 10
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x325, 1)"), scpexpr(EXPR_END)), "loc_416")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x25\x03\x07\x00。\x02",
    )

    Jump("loc_3FB")

    label("loc_3FB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2980)
    Jump("loc_484")

    label("loc_416")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x25\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x25\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_465")

    label("loc_465")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_484")

    Jump("loc_4BA")

    label("loc_487")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3A2 end

    def Function_3_4C8(): pass

    label("Function_3_4C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A3, 1)"), scpexpr(EXPR_END)), "loc_53C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA3\x01\x07\x00。\x02",
    )

    Jump("loc_521")

    label("loc_521")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29C1)
    Jump("loc_5AA")

    label("loc_53C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA3\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA3\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_58B")

    label("loc_58B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_5AA")

    Jump("loc_5E0")

    label("loc_5AD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4C8 end

    def Function_4_5EE(): pass

    label("Function_4_5EE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x538, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_662")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    Jump("loc_647")

    label("loc_647")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29C2)
    Jump("loc_6D0")

    label("loc_662")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x02\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6B1")

    label("loc_6B1")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x16, 60)
    OP_70(0x16, 0x0)

    label("loc_6D0")

    Jump("loc_706")

    label("loc_6D3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_706")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5EE end

    def Function_5_714(): pass

    label("Function_5_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_723")
    Call(0, 6)
    Jump("loc_755")

    label("loc_723")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05导力已经连通。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_755")

    Return()

    # Function_5_714 end

    def Function_6_756(): pass

    label("Function_6_756")

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

    # Function_6_756 end

    def Function_7_790(): pass

    label("Function_7_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x05导力没有连通。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_80E")

    label("loc_7CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC")
    Call(0, 8)
    Jump("loc_80E")

    label("loc_7DC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05门已经被打开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_80E")

    Return()

    # Function_7_790 end

    def Function_8_80F(): pass

    label("Function_8_80F")

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

    # Function_8_80F end

    def Function_9_97E(): pass

    label("Function_9_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x325, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D9")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        (
            "\x07\x05有插卡用的槽。\x01",
            "似乎需要认证用的卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Jump("loc_A1A")

    label("loc_9D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E8")
    Call(0, 10)
    Jump("loc_A1A")

    label("loc_9E8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        "\x07\x05门已经被打开。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_A1A")

    Return()

    # Function_9_97E end

    def Function_10_A1B(): pass

    label("Function_10_A1B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(4019, 0, 108800, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(3050, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABF")
    SetChrPos(0x109, 2650, 0, 107730, 0)
    SetChrPos(0x102, 1340, 0, 107670, 0)
    SetChrPos(0x103, 2820, 0, 106390, 0)
    SetChrPos(0x10A, 1530, 0, 106250, 0)
    Jump("loc_B03")

    label("loc_ABF")

    SetChrPos(0x109, 2650, 0, 107730, 0)
    SetChrPos(0x102, 1340, 0, 107670, 0)
    SetChrPos(0xF0, 2820, 0, 106390, 0)
    SetChrPos(0xF1, 1530, 0, 106250, 0)

    label("loc_B03")

    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x33, 1)
    OP_70(0x33, 0x1)
    Sleep(500)

    def lambda_B31():
        OP_6D(2110, 750, 112590, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B31)

    def lambda_B49():
        OP_67(0, 5090, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B49)

    def lambda_B61():
        OP_6B(3440, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B61)

    def lambda_B71():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_B71)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    OP_22(0x6B, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1297")
    OP_A2(0x290C)
    Fade(500)
    OP_6D(3340, 0, 108000, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(44000, 0)
    OP_6E(264, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAD")
    TurnDirection(0x10A, 0x103, 400)
    Sleep(300)

    ChrTalk(    #14
        0x10A,
        (
            "#1317F#6P雪、雪拉前辈……\x02\x03",

            "这里……\x01",
            "结构是不是改变了？\x02",
        )
    )

    Jump("loc_C82")

    label("loc_C82")

    CloseMessageWindow()
    TurnDirection(0x103, 0x10A, 400)
    Sleep(300)

    ChrTalk(    #15
        0x103,
        (
            "#1534F#11P是吗……\x01",
            "你也这么认为啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CC5)
    Sleep(100)
    OP_8C(0x102, 135, 400)
    Sleep(300)

    ChrTalk(    #16
        0x102,
        "#1504F#5P结构改变了……？\x02",
    )

    CloseMessageWindow()

    def lambda_D0A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_D0A)
    Sleep(100)
    OP_8C(0x103, 0, 400)
    Sleep(300)

    ChrTalk(    #17
        0x10A,
        (
            "#812F#6P嗯……\x01",
            "我感觉走廊和房间的组成\x01",
            "完全不一样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        (
            "#1520F#12P嗯，不过也说不定是\x01",
            "你们用过以后改建或扩建过了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F96")

    ChrTalk(    #19
        0x10A,
        "#1317F#6P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_DEF():
        TurnDirection(0xFE, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DEF)
    Sleep(100)

    def lambda_E02():
        TurnDirection(0xFE, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E02)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    TurnDirection(0xF1, 0x10A, 400)
    Jump("loc_E3C")

    label("loc_E27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3C")
    TurnDirection(0xF0, 0x10A, 400)

    label("loc_E3C")

    Sleep(200)

    ChrTalk(    #20
        0x109,
        (
            "#1079F#5P嗯……？\x01",
            "怎么了，亚妮拉丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        (
            "#813F#6P呃，嗯……\x02\x03",

            "#812F从刚才开始\x01",
            "就一直觉得有点不对劲……\x02\x03",

            "这里的结构，\x01",
            "好像和训练时不一样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1504F#5P结构改变了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#1316F#6P嗯……\x01",
            "我感觉走廊和房间的组成\x01",
            "完全不一样了。\x02\x03",

            "#810F啊，不过也可能是我们用过之后\x01",
            "又改建或者扩建过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_F96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116B")

    ChrTalk(    #24
        0x103,
        "#1522F#6P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_FD8():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FD8)
    Sleep(100)

    def lambda_FEB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEB)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1010")
    TurnDirection(0xF1, 0x103, 400)
    Jump("loc_1025")

    label("loc_1010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1025")
    TurnDirection(0xF0, 0x103, 400)

    label("loc_1025")

    Sleep(200)

    ChrTalk(    #25
        0x109,
        (
            "#1079F#5P大姐……？\x01",
            "怎么了？\x02",
        )
    )

    Jump("loc_105E")

    label("loc_105E")

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#1526F#6P啊，嗯。\x01",
            "我想不会是自己搞错了……\x02\x03",

            "#1522F这里和以前我来的时候相比\x01",
            "结构好像变了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        "#1504F#5P结构改变了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#1525F#6P我是说，\x01",
            "走廊和房间的组成完全不一样了。\x02\x03",

            "#1527F嗯，也可能是我使用过后\x01",
            "被改建或者扩建过了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(    #29
        0x109,
        (
            "#1065F#5P……封印区域的结构\x01",
            "不是也完全改变了嘛。\x02\x03",

            "#1063F不管怎么说\x01",
            "大概都是敌人做的手脚吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125A")

    label("loc_11EB")


    ChrTalk(    #30
        0x109,
        (
            "#1065F#5P……封印区域的结构\x01",
            "不是也完全改变了嘛。\x02\x03",

            "#1063F不管怎么说\x01",
            "大概都是敌人做的手脚吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125A")


    ChrTalk(    #31
        0x102,
        (
            "#1502F#5P嗯嗯……\x01",
            "看来有必要谨慎前进呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Jump("loc_12E1")

    label("loc_1297")

    Fade(500)
    OP_6D(2850, 0, 107890, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    OP_0D()

    label("loc_12E1")

    OP_A2(0x2952)
    EventEnd(0x0)
    Return()

    # Function_10_A1B end

    SaveToFile()

Try(main)
