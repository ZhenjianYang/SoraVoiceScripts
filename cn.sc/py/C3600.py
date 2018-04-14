from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3600   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 30,
        TriggerZ            = -7650,
        TriggerY            = -710,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -7650,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4990,
        TriggerZ            = -7200,
        TriggerY            = -5010,
        TriggerRange        = 1000,
        ActorX              = -5460,
        ActorZ              = -7200,
        ActorY              = -5470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -7190,
        TriggerZ            = -7200,
        TriggerY            = 10,
        TriggerRange        = 1000,
        ActorX              = -7810,
        ActorZ              = -7200,
        ActorY              = 10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4970,
        TriggerZ            = -7200,
        TriggerY            = 5030,
        TriggerRange        = 1000,
        ActorX              = -5440,
        ActorZ              = -7200,
        ActorY              = 5500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5020,
        TriggerZ            = -7200,
        TriggerY            = 4990,
        TriggerRange        = 1000,
        ActorX              = 5450,
        ActorZ              = -7200,
        ActorY              = 5430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = -7200,
        TriggerY            = 10,
        TriggerRange        = 1000,
        ActorX              = 7860,
        ActorZ              = -7200,
        ActorY              = 10,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4990,
        TriggerZ            = -7200,
        TriggerY            = -5020,
        TriggerRange        = 1000,
        ActorX              = 5520,
        ActorZ              = -7200,
        ActorY              = -5550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1C5",          # 01, 1
        "Function_2_27F",          # 02, 2
        "Function_3_37B",          # 03, 3
        "Function_4_492",          # 04, 4
        "Function_5_5A9",          # 05, 5
        "Function_6_6C0",          # 06, 6
        "Function_7_7D7",          # 07, 7
        "Function_8_8EE",          # 08, 8
        "Function_9_A05",          # 09, 9
        "Function_10_BDB",         # 0A, 10
        "Function_11_C46",         # 0B, 11
        "Function_12_CB1",         # 0C, 12
        "Function_13_D1C",         # 0D, 13
        "Function_14_D87",         # 0E, 14
        "Function_15_E6D",         # 0F, 15
        "Function_16_EF2",         # 10, 16
        "Function_17_F77",         # 11, 17
        "Function_18_FFC",         # 12, 18
        "Function_19_1081",        # 13, 19
        "Function_20_117C",        # 14, 20
        "Function_21_11F4",        # 15, 21
        "Function_22_12E7",        # 16, 22
        "Function_23_13DA",        # 17, 23
        "Function_24_1428",        # 18, 24
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1B6"),
        (101, "loc_1BD"),
        (SWITCH_DEFAULT, "loc_1C4"),
    )


    label("loc_1B6")

    Event(0, 9)
    Jump("loc_1C4")

    label("loc_1BD")

    Event(0, 19)
    Jump("loc_1C4")

    label("loc_1C4")

    Return()

    # Function_0_1A6 end

    def Function_1_1C5(): pass

    label("Function_1_1C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7")
    OP_6F(0x1, 0)
    Jump("loc_1DE")

    label("loc_1D7")

    OP_6F(0x1, 60)

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0")
    OP_6F(0x2, 0)
    Jump("loc_1F7")

    label("loc_1F0")

    OP_6F(0x2, 60)

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209")
    OP_6F(0x3, 0)
    Jump("loc_210")

    label("loc_209")

    OP_6F(0x3, 60)

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222")
    OP_6F(0x4, 0)
    Jump("loc_229")

    label("loc_222")

    OP_6F(0x4, 60)

    label("loc_229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B")
    OP_6F(0x5, 0)
    Jump("loc_242")

    label("loc_23B")

    OP_6F(0x5, 60)

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254")
    OP_6F(0x6, 0)
    Jump("loc_25B")

    label("loc_254")

    OP_6F(0x6, 60)

    label("loc_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    OP_6F(0x7, 0)
    Jump("loc_274")

    label("loc_26D")

    OP_6F(0x7, 60)

    label("loc_274")

    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0x14)
    Return()

    # Function_1_1C5 end

    def Function_2_27F(): pass

    label("Function_2_27F")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    AddSepith(0x2, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#58I火之耀晶片×３００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F20)
    Jump("loc_369")

    label("loc_34F")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_369")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_27F end

    def Function_3_37B(): pass

    label("Function_3_37B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_3EA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F22)
    Jump("loc_450")

    label("loc_3EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_450")

    Jump("loc_484")

    label("loc_453")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_484")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_37B end

    def Function_4_492(): pass

    label("Function_4_492")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_501")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F23)
    Jump("loc_567")

    label("loc_501")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_567")

    Jump("loc_59B")

    label("loc_56A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_59B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_492 end

    def Function_5_5A9(): pass

    label("Function_5_5A9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_618")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F24)
    Jump("loc_67E")

    label("loc_618")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_67E")

    Jump("loc_6B2")

    label("loc_681")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5A9 end

    def Function_6_6C0(): pass

    label("Function_6_6C0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_798")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_72F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xF8\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F25)
    Jump("loc_795")

    label("loc_72F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\xF8\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF8\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_795")

    Jump("loc_7C9")

    label("loc_798")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7C9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_6C0 end

    def Function_7_7D7(): pass

    label("Function_7_7D7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_846")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F26)
    Jump("loc_8AC")

    label("loc_846")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_8AC")

    Jump("loc_8E0")

    label("loc_8AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8E0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_7D7 end

    def Function_8_8EE(): pass

    label("Function_8_8EE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_95D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F27)
    Jump("loc_9C3")

    label("loc_95D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_9C3")

    Jump("loc_9F7")

    label("loc_9C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9F7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_8EE end

    def Function_9_A05(): pass

    label("Function_9_A05")

    EventBegin(0x0)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    OP_C8(0x200, 0x46, "C_PLAC22._CH", 0x0, 0x1F4)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0xA)
    Sleep(800)

    def lambda_B0C():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_B0C)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0xC)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 610, 600, -77870, 0)
    SetChrPos(0x1, 610, 600, -77870, 0)
    SetChrPos(0x2, 610, 600, -77870, 0)
    SetChrPos(0x3, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_9_A05 end

    def Function_10_BDB(): pass

    label("Function_10_BDB")


    def lambda_BE1():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE1)

    def lambda_BFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFB)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_C26():
        OP_8F(0xFE, 0x262, 0x258, 0xFFFECFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C26)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_BDB end

    def Function_11_C46(): pass

    label("Function_11_C46")


    def lambda_C4C():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C4C)

    def lambda_C66():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C66)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_C91():
        OP_8F(0xFE, 0xFFFFFE2A, 0x258, 0xFFFECEF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C91)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_C46 end

    def Function_12_CB1(): pass

    label("Function_12_CB1")


    def lambda_CB7():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CB7)

    def lambda_CD1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CD1)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_CFC():
        OP_8F(0xFE, 0x276, 0x2EE, 0xFFFECA32, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CFC)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_CB1 end

    def Function_13_D1C(): pass

    label("Function_13_D1C")


    def lambda_D22():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D22)

    def lambda_D3C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3C)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_D67():
        OP_8F(0xFE, 0xFFFFFDE4, 0x2EE, 0xFFFECA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D67)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_D1C end

    def Function_14_D87(): pass

    label("Function_14_D87")

    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(680, 750, -84120, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 680, 700, -81310, 180)
    SetChrPos(0x102, -330, 700, -81100, 180)
    SetChrPos(0xF8, 910, 750, -79600, 180)
    SetChrPos(0xF9, -270, 750, -79450, 180)
    OP_43(0x101, 0x0, 0x0, 0xF)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0x10)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x12)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R3104   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_14_D87 end

    def Function_15_E6D(): pass

    label("Function_15_E6D")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_EB2():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EB2)

    def lambda_ECC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_ECC)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_15_E6D end

    def Function_16_EF2(): pass

    label("Function_16_EF2")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F37():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F37)

    def lambda_F51():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F51)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_16_EF2 end

    def Function_17_F77(): pass

    label("Function_17_F77")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_FBC():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBC)

    def lambda_FD6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FD6)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_17_F77 end

    def Function_18_FFC(): pass

    label("Function_18_FFC")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1041():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1041)

    def lambda_105B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_105B)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_18_FFC end

    def Function_19_1081(): pass

    label("Function_19_1081")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x101, 500, 250, 84030, 180)
    SetChrPos(0x102, -500, 250, 84030, 180)
    SetChrPos(0xF8, 500, 250, 85030, 180)
    SetChrPos(0xF9, -500, 250, 85030, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 23)
    Fade(500)
    OP_6D(-130, 250, 82150, 0)
    SetChrPos(0x0, -130, 250, 82150, 180)
    SetChrPos(0x1, -130, 250, 82150, 180)
    SetChrPos(0x2, -130, 250, 82150, 180)
    SetChrPos(0x3, -130, 250, 82150, 180)
    EventEnd(0x0)
    Return()

    # Function_19_1081 end

    def Function_20_117C(): pass

    label("Function_20_117C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 84530, 0)
    SetChrPos(0x101, -500, 250, 85030, 0)
    SetChrPos(0x102, 500, 250, 85030, 0)
    SetChrPos(0xF8, -500, 250, 84030, 0)
    SetChrPos(0xF9, 500, 250, 84030, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    NewScene("ED6_DT21/C3601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_117C end

    def Function_21_11F4(): pass

    label("Function_21_11F4")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_21_11F4 end

    def Function_22_12E7(): pass

    label("Function_22_12E7")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_12E7 end

    def Function_23_13DA(): pass

    label("Function_23_13DA")


    def lambda_13E0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_13E0)

    def lambda_13F2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_13F2)

    def lambda_1404():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1404)

    def lambda_1416():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1416)
    Sleep(2500)
    Return()

    # Function_23_13DA end

    def Function_24_1428(): pass

    label("Function_24_1428")


    def lambda_142E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_142E)

    def lambda_1440():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1440)

    def lambda_1452():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1452)

    def lambda_1464():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1464)
    Sleep(2000)
    Return()

    # Function_24_1428 end

    SaveToFile()

Try(main)
