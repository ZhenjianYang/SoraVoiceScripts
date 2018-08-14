from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5511   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5511.x',
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
        X                   = 138610,
        Z                   = 0,
        Y                   = 49750,
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
        X                   = 198330,
        Z                   = 0,
        Y                   = 57380,
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
        X                   = 202790,
        Z                   = 0,
        Y                   = 152770,
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
        X                   = 110930,
        Z                   = 0,
        Y                   = 147490,
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
        TriggerX            = 198380,
        TriggerZ            = 0,
        TriggerY            = -10,
        TriggerRange        = 1000,
        ActorX              = 198380,
        ActorZ              = 1000,
        ActorY              = -10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 209090,
        TriggerZ            = 250,
        TriggerY            = 58470,
        TriggerRange        = 1000,
        ActorX              = 209260,
        ActorZ              = 1600,
        ActorY              = 57980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 199150,
        TriggerZ            = 0,
        TriggerY            = 64190,
        TriggerRange        = 1000,
        ActorX              = 199150,
        ActorZ              = 1000,
        ActorY              = 64190,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93310,
        TriggerZ            = 250,
        TriggerY            = 169080,
        TriggerRange        = 1000,
        ActorX              = 93860,
        ActorZ              = 1600,
        ActorY              = 169250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103110,
        TriggerZ            = 0,
        TriggerY            = 169990,
        TriggerRange        = 1000,
        ActorX              = 103110,
        ActorZ              = 1000,
        ActorY              = 169990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 151580,
        TriggerZ            = 0,
        TriggerY            = 200060,
        TriggerRange        = 1000,
        ActorX              = 151580,
        ActorZ              = 1000,
        ActorY              = 200060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 99000,
        TriggerZ            = 0,
        TriggerY            = 100000,
        TriggerRange        = 1000,
        ActorX              = 99000,
        ActorZ              = 1000,
        ActorY              = 100000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_51F",          # 02, 2
        "Function_3_645",          # 03, 3
        "Function_4_76B",          # 04, 4
        "Function_5_891",          # 05, 5
        "Function_6_9ED",          # 06, 6
        "Function_7_A28",          # 07, 7
        "Function_8_B20",          # 08, 8
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Return()

    # Function_0_246 end

    def Function_1_247(): pass

    label("Function_1_247")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    OP_7B()
    OP_72(0x202C, 0x0)
    ExitThread()
    OP_72(0x82C, 0x0)
    ExitThread()
    OP_6F(0x2C, 0)
    OP_72(0x202A, 0x0)
    ExitThread()
    OP_72(0x82A, 0x0)
    ExitThread()
    OP_6F(0x2A, 0)
    OP_72(0x802, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    Jump("loc_3BB")

    label("loc_2C6")

    OP_C4(0x1, 0x1)
    OP_78(0xFF, 0xFF, 0xFF)
    OP_7B()
    OP_72(0x202C, 0x0)
    ExitThread()
    OP_72(0x82C, 0x0)
    ExitThread()
    OP_6F(0x2C, 1)
    OP_72(0x202A, 0x0)
    ExitThread()
    OP_72(0x82A, 0x0)
    ExitThread()
    OP_6F(0x2A, 240)
    OP_72(0x42E, 0x0)
    ExitThread()
    OP_72(0x42F, 0x0)
    ExitThread()
    OP_72(0x81D, 0x0)
    ExitThread()
    OP_6F(0x1D, 1)
    OP_70(0x1D, 0x1)
    OP_72(0x81E, 0x0)
    ExitThread()
    OP_6F(0x1E, 1)
    OP_70(0x1E, 0x1)
    OP_72(0x81F, 0x0)
    ExitThread()
    OP_6F(0x1F, 1)
    OP_70(0x1F, 0x1)
    OP_72(0x820, 0x0)
    ExitThread()
    OP_6F(0x20, 1)
    OP_70(0x20, 0x1)
    OP_72(0x821, 0x0)
    ExitThread()
    OP_6F(0x21, 1)
    OP_70(0x21, 0x1)
    OP_72(0x822, 0x0)
    ExitThread()
    OP_6F(0x22, 1)
    OP_70(0x22, 0x1)
    OP_72(0x823, 0x0)
    ExitThread()
    OP_6F(0x23, 1)
    OP_70(0x23, 0x1)
    OP_72(0x824, 0x0)
    ExitThread()
    OP_6F(0x24, 1)
    OP_70(0x24, 0x1)
    OP_72(0x825, 0x0)
    ExitThread()
    OP_6F(0x25, 1)
    OP_70(0x25, 0x1)
    OP_64(0x2, 0x1)

    label("loc_3BB")

    Jump("loc_4D3")

    label("loc_3BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_434")
    OP_C4(0x0, 0x1)
    OP_78(0x0, 0x0, 0x0)
    OP_7B()
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 0)
    OP_72(0x202B, 0x0)
    ExitThread()
    OP_72(0x82B, 0x0)
    ExitThread()
    OP_6F(0x2B, 0)
    OP_72(0x806, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    Jump("loc_4C5")

    label("loc_434")

    OP_C4(0x1, 0x1)
    OP_78(0xFF, 0xFF, 0xFF)
    OP_7B()
    OP_72(0x202D, 0x0)
    ExitThread()
    OP_72(0x82D, 0x0)
    ExitThread()
    OP_6F(0x2D, 1)
    OP_72(0x202B, 0x0)
    ExitThread()
    OP_72(0x82B, 0x0)
    ExitThread()
    OP_6F(0x2B, 240)
    OP_72(0x430, 0x0)
    ExitThread()
    OP_72(0x431, 0x0)
    ExitThread()
    OP_72(0x826, 0x0)
    ExitThread()
    OP_6F(0x26, 1)
    OP_70(0x26, 0x1)
    OP_72(0x827, 0x0)
    ExitThread()
    OP_6F(0x27, 1)
    OP_70(0x27, 0x1)
    OP_72(0x828, 0x0)
    ExitThread()
    OP_6F(0x28, 1)
    OP_70(0x28, 0x1)
    OP_72(0x829, 0x0)
    ExitThread()
    OP_6F(0x29, 1)
    OP_70(0x29, 0x1)
    OP_64(0x4, 0x1)

    label("loc_4C5")

    Jump("loc_4D3")

    label("loc_4C8")

    OP_C4(0x1, 0x1)
    OP_78(0xFF, 0xFF, 0xFF)
    OP_7B()

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5")
    OP_6F(0x1C, 0)
    Jump("loc_4EC")

    label("loc_4E5")

    OP_6F(0x1C, 60)

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE")
    OP_6F(0x1A, 0)
    Jump("loc_505")

    label("loc_4FE")

    OP_6F(0x1A, 60)

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517")
    OP_6F(0x1B, 0)
    Jump("loc_51E")

    label("loc_517")

    OP_6F(0x1B, 60)

    label("loc_51E")

    Return()

    # Function_1_247 end

    def Function_2_51F(): pass

    label("Function_2_51F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1C, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x150, 1)"), scpexpr(EXPR_END)), "loc_593")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x50\x01\x07\x00。\x02",
    )

    Jump("loc_578")

    label("loc_578")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2982)
    Jump("loc_601")

    label("loc_593")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x50\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x50\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5E2")

    label("loc_5E2")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1C, 60)
    OP_70(0x1C, 0x0)

    label("loc_601")

    Jump("loc_637")

    label("loc_604")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_637")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_51F end

    def Function_3_645(): pass

    label("Function_3_645")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_6B9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_69E")

    label("loc_69E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29D1)
    Jump("loc_727")

    label("loc_6B9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_708")

    label("loc_708")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1A, 60)
    OP_70(0x1A, 0x0)

    label("loc_727")

    Jump("loc_75D")

    label("loc_72A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_75D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_645 end

    def Function_4_76B(): pass

    label("Function_4_76B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1B, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17A, 1)"), scpexpr(EXPR_END)), "loc_7DF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x7A\x01\x07\x00。\x02",
    )

    Jump("loc_7C4")

    label("loc_7C4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29D2)
    Jump("loc_84D")

    label("loc_7DF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x7A\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7A\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_82E")

    label("loc_82E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1B, 60)
    OP_70(0x1B, 0x0)

    label("loc_84D")

    Jump("loc_883")

    label("loc_850")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_883")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_76B end

    def Function_5_891(): pass

    label("Function_5_891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BA")
    EventBegin(0x0)
    OP_6F(0x2A, 0)
    OP_70(0x2A, 0xF0)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x2C, 1)
    OP_70(0x2C, 0x1)
    Sleep(500)
    Fade(500)
    OP_72(0x42E, 0x0)
    ExitThread()
    OP_72(0x42F, 0x0)
    ExitThread()
    OP_72(0x81D, 0x0)
    ExitThread()
    OP_6F(0x1D, 1)
    OP_70(0x1D, 0x1)
    OP_72(0x81E, 0x0)
    ExitThread()
    OP_6F(0x1E, 1)
    OP_70(0x1E, 0x1)
    OP_72(0x81F, 0x0)
    ExitThread()
    OP_6F(0x1F, 1)
    OP_70(0x1F, 0x1)
    OP_72(0x820, 0x0)
    ExitThread()
    OP_6F(0x20, 1)
    OP_70(0x20, 0x1)
    OP_72(0x821, 0x0)
    ExitThread()
    OP_6F(0x21, 1)
    OP_70(0x21, 0x1)
    OP_72(0x822, 0x0)
    ExitThread()
    OP_6F(0x22, 1)
    OP_70(0x22, 0x1)
    OP_72(0x823, 0x0)
    ExitThread()
    OP_6F(0x23, 1)
    OP_70(0x23, 0x1)
    OP_72(0x824, 0x0)
    ExitThread()
    OP_6F(0x24, 1)
    OP_70(0x24, 0x1)
    OP_72(0x825, 0x0)
    ExitThread()
    OP_6F(0x25, 1)
    OP_70(0x25, 0x1)
    OP_C4(0x1, 0x1)
    OP_78(0xFF, 0xFF, 0xFF)
    OP_7B()
    OP_0D()
    OP_64(0x2, 0x1)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_A2(0x2954)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_9EC")

    label("loc_9BA")

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

    label("loc_9EC")

    Return()

    # Function_5_891 end

    def Function_6_9ED(): pass

    label("Function_6_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27")
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

    label("loc_A27")

    Return()

    # Function_6_9ED end

    def Function_7_A28(): pass

    label("Function_7_A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AED")
    EventBegin(0x0)
    OP_6F(0x2B, 0)
    OP_70(0x2B, 0xF0)
    OP_22(0x64, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x2D, 1)
    OP_70(0x2D, 0x1)
    Sleep(500)
    Fade(500)
    OP_72(0x430, 0x0)
    ExitThread()
    OP_72(0x431, 0x0)
    ExitThread()
    OP_72(0x826, 0x0)
    ExitThread()
    OP_6F(0x26, 1)
    OP_70(0x26, 0x1)
    OP_72(0x827, 0x0)
    ExitThread()
    OP_6F(0x27, 1)
    OP_70(0x27, 0x1)
    OP_72(0x828, 0x0)
    ExitThread()
    OP_6F(0x28, 1)
    OP_70(0x28, 0x1)
    OP_72(0x829, 0x0)
    ExitThread()
    OP_6F(0x29, 1)
    OP_70(0x29, 0x1)
    OP_C4(0x1, 0x1)
    OP_78(0xFF, 0xFF, 0xFF)
    OP_7B()
    OP_0D()
    OP_64(0x4, 0x1)
    OP_71(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_A2(0x2955)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_B1F")

    label("loc_AED")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05导力已经连通。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_B1F")

    Return()

    # Function_7_A28 end

    def Function_8_B20(): pass

    label("Function_8_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5A")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #12
        "\x07\x05导力没有连通。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)

    label("loc_B5A")

    Return()

    # Function_8_B20 end

    SaveToFile()

Try(main)
