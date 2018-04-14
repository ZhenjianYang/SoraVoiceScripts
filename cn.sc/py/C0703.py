from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0703   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0703.x',
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


    DeclEvent(
        X                   = -3400,
        Y                   = -2000,
        Z                   = 56200,
        Range               = 3400,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xE09C,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = 88300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = 89000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 400,
        TriggerY            = -88300,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 400,
        ActorY              = -89000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 290,
        TriggerZ            = 0,
        TriggerY            = 45880,
        TriggerRange        = 1000,
        ActorX              = 230,
        ActorZ              = 800,
        ActorY              = 46150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46950,
        TriggerZ            = 0,
        TriggerY            = -1000,
        TriggerRange        = 1000,
        ActorX              = 47050,
        ActorZ              = 800,
        ActorY              = -840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -46770,
        TriggerZ            = 0,
        TriggerY            = -750,
        TriggerRange        = 1000,
        ActorX              = -46750,
        ActorZ              = 800,
        ActorY              = -440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -47710,
        TriggerRange        = 1000,
        ActorX              = -60,
        ActorZ              = 800,
        ActorY              = -47460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_242",          # 02, 2
        "Function_3_359",          # 03, 3
        "Function_4_470",          # 04, 4
        "Function_5_8D9",          # 05, 5
        "Function_6_151D",         # 06, 6
        "Function_7_174B",         # 07, 7
        "Function_8_1BAF",         # 08, 8
        "Function_9_2048",         # 09, 9
        "Function_10_25E2",        # 0A, 10
        "Function_11_2669",        # 0B, 11
        "Function_12_26F8",        # 0C, 12
        "Function_13_27F3",        # 0D, 13
        "Function_14_286B",        # 0E, 14
        "Function_15_2966",        # 0F, 15
        "Function_16_2A0A",        # 10, 16
        "Function_17_2B17",        # 11, 17
        "Function_18_2B98",        # 12, 18
        "Function_19_2CA5",        # 13, 19
        "Function_20_2D26",        # 14, 20
        "Function_21_2E33",        # 15, 21
        "Function_22_2EB4",        # 16, 22
        "Function_23_2FC1",        # 17, 23
        "Function_24_3042",        # 18, 24
        "Function_25_3135",        # 19, 25
        "Function_26_3228",        # 1A, 26
        "Function_27_3276",        # 1B, 27
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1C2"),
        (101, "loc_1C9"),
        (102, "loc_1D0"),
        (103, "loc_1D7"),
        (104, "loc_1DE"),
        (105, "loc_1E5"),
        (SWITCH_DEFAULT, "loc_1EC"),
    )


    label("loc_1C2")

    Event(0, 12)
    Jump("loc_1EC")

    label("loc_1C9")

    Event(0, 14)
    Jump("loc_1EC")

    label("loc_1D0")

    Event(0, 16)
    Jump("loc_1EC")

    label("loc_1D7")

    Event(0, 18)
    Jump("loc_1EC")

    label("loc_1DE")

    Event(0, 20)
    Jump("loc_1EC")

    label("loc_1E5")

    Event(0, 22)
    Jump("loc_1EC")

    label("loc_1EC")

    Return()

    # Function_0_1A2 end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF")
    OP_6F(0x20, 0)
    Jump("loc_206")

    label("loc_1FF")

    OP_6F(0x20, 60)

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218")
    OP_6F(0x21, 0)
    Jump("loc_21F")

    label("loc_218")

    OP_6F(0x21, 60)

    label("loc_21F")

    Call(0, 4)
    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x11)
    OP_1B(0x3, 0x0, 0x13)
    OP_1B(0x4, 0x0, 0x15)
    OP_1B(0x5, 0x0, 0x17)
    Return()

    # Function_1_1ED end

    def Function_2_242(): pass

    label("Function_2_242")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x144, 1)"), scpexpr(EXPR_END)), "loc_2B1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x44\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F0A)
    Jump("loc_317")

    label("loc_2B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x44\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x44\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_317")

    Jump("loc_34B")

    label("loc_31A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_34B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_242 end

    def Function_3_359(): pass

    label("Function_3_359")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_431")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16E, 1)"), scpexpr(EXPR_END)), "loc_3C8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x6E\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F0C)
    Jump("loc_42E")

    label("loc_3C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x6E\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x6E\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_42E")

    Jump("loc_462")

    label("loc_431")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_462")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_359 end

    def Function_4_470(): pass

    label("Function_4_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 1)), scpexpr(EXPR_END)), "loc_4F1")
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_6F(0x8, 360)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    Jump("loc_568")

    label("loc_4F1")

    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_END)), "loc_5FA")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    Jump("loc_682")

    label("loc_5FA")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_END)), "loc_725")
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 360)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    Jump("loc_7BE")

    label("loc_725")

    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)

    label("loc_7BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_END)), "loc_850")
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_6F(0x18, 360)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    Jump("loc_8D8")

    label("loc_850")

    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)

    label("loc_8D8")

    Return()

    # Function_4_470 end

    def Function_5_8D9(): pass

    label("Function_5_8D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 6)), scpexpr(EXPR_END)), "loc_8E1")
    Return()

    label("loc_8E1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_906")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_906")

    Fade(500)
    OP_6D(-180, 400, 58250, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1120, 400, 57110, 180)
    SetChrPos(0x102, -190, 400, 57080, 180)
    SetChrPos(0xF8, 1030, 400, 58470, 180)
    SetChrPos(0xF9, -230, 400, 58410, 180)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        "#1004F#2P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_9C4():
        OP_6D(240, 400, 48840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9C4)

    def lambda_9DC():
        OP_67(0, 4080, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DC)

    def lambda_9F4():
        OP_6B(3600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F4)

    def lambda_A04():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A04)

    def lambda_A14():
        OP_6E(290, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A14)
    WaitChrThread(0x101, 0x0)

    def lambda_A29():
        OP_8E(0xFE, 0x41A, 0xC8, 0xC404, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A29)
    Sleep(300)

    def lambda_A49():
        OP_8E(0xFE, 0xFFFFFF38, 0xC8, 0xC3BE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A49)
    Sleep(100)

    def lambda_A69():
        OP_8E(0xFE, 0x3DE, 0x190, 0xC896, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A69)
    Sleep(300)

    def lambda_A89():
        OP_8E(0xFE, 0xFFFFFE7A, 0x190, 0xC8F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A89)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(-890, 0, 45660, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1040, 200, 43380, 0)
    SetChrPos(0x102, -180, 200, 43430, 0)
    SetChrPos(0xF8, 1360, 400, 41830, 0)
    SetChrPos(0xF9, -80, 400, 42080, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #7
        0x101,
        (
            "#1015F#6P这是……\x01",
            "好像是什么装置。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC7")

    ChrTalk(    #8
        0x109,
        (
            "#1064F唔～看起来\x01",
            "好像是什么终端。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFB")

    label("loc_BC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFB")

    ChrTalk(    #9
        0x107,
        (
            "#064F难不成\x01",
            "是什么装置的终端……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFB")


    ChrTalk(    #10
        0x102,
        "#1040F#5P……调查看看吧。\x02",
    )

    CloseMessageWindow()

    def lambda_C20():
        OP_6D(-140, 400, 46050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C20)
    OP_8F(0x102, 0xFA, 0x96, 0xB22A, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x102,
        (
            "#1035F#5P………………………………\x02\x03",

            "#1040F……是这个了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x8, 0x78)
    OP_70(0x8, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x9, 0x64)
    OP_B0(0xD, 0x64)
    OP_B0(0xE, 0x64)
    OP_70(0x9, 0xF0)
    Sleep(100)
    OP_70(0xD, 0xF0)
    Sleep(100)
    OP_70(0xE, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)

    def lambda_CE2():
        OP_6D(-970, 890, 46970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE2)

    def lambda_CFA():
        OP_67(0, 4420, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CFA)

    def lambda_D12():
        OP_6B(3790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D12)

    def lambda_D22():
        OP_6E(274, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D22)
    OP_B0(0xA, 0x64)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_70(0xA, 0x168)
    OP_70(0xB, 0x168)
    OP_70(0xC, 0x168)
    OP_73(0xA)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #12
        0x101,
        "#1004F哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        (
            "#1040F#5P看来是记录\x01",
            "情报的终端啊。\x02\x03",

            "确认内容看看吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #14
        (
            "\x07\x05#1S『关于封印机构（１／４）』\x01",
            "　\x01",
            "──我的名字是\x01",
            "赛雷斯托·Ｄ·奥赛雷丝。\x01",
            "是『封■■■』■■创始■\x01",
            "『封■计■■■■负责人。\x01",
            "　\x01",
            "■■，塔■■■■第二结■启动■■■\x01",
            "异次■封■■■■■环』■\x01",
            "■■■■■时■■■■■\x01",
            "留下■■■的■■■■■的载体■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #15
        (
            "\x07\x05#1S■读■这■■■息的■■人\x01",
            "■■■■■■■■■『环■■复活\x01",
            "■把此作为■■那将是■大幸■。\x01",
            "■■■看■期■■环』■■■\x01",
            "我请求■■新考虑■■■■■。\x01",
            "　\x01",
            "『■』■力量■■强大■\x01",
            "不是人类■■子能够处理的事■。\x01",
            "■纳■■之时\x01",
            "也■是■们造■■狱■日。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\xFD\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FD, 1)
    OP_A2(0x1E31)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A4")

    ChrTalk(    #17
        0x101,
        (
            "#1019F什么啊，除了最开始的部分\x01",
            "其它部分都无法辨认嘛。\x02\x03",

            "#1004F唔……\x01",
            "这个奥赛雷丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        (
            "#047F嗯……\x01",
            "是利贝尔王室的姓。\x02\x03",

            "#040F说不定是有缘之人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261")

    label("loc_10A4")


    ChrTalk(    #19
        0x101,
        (
            "#1019F什么啊，除了最开始的部分\x01",
            "其它部分都无法辨认嘛。\x02\x03",

            "#1004F唔……\x01",
            "这个奥赛雷丝。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1156")

    ChrTalk(    #20
        0x103,
        (
            "#023F说到奥赛雷丝\x01",
            "是利贝尔王室的姓啊。\x02\x03",

            "#020F说不定是有关系的人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261")

    label("loc_1156")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B0")

    ChrTalk(    #21
        0x106,
        (
            "#053F说到奥赛雷丝\x01",
            "是利贝尔王室的姓哦。\x02\x03",

            "#051F说不定是有关系的人那。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261")

    label("loc_11B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_120A")

    ChrTalk(    #22
        0x108,
        (
            "#073F记得奥赛雷丝\x01",
            "应该是利贝尔王室的姓。\x02\x03",

            "#070F说不定是有缘之人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1261")

    label("loc_120A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1261")

    ChrTalk(    #23
        0x109,
        (
            "#1060F说到奥赛雷丝\x01",
            "是利贝尔王室的姓呀。\x02\x03",

            "#1065F很可能是有缘之人呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1261")

    OP_8C(0x102, 180, 400)

    ChrTalk(    #24
        0x102,
        (
            "#1035F#2P……看来很可能\x01",
            "记载着重大的事情。\x02\x03",

            "#1043F要是能想办法读出来就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(    #25
        0x101,
        "#1007F嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x107,
        "#064F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1015F提妲，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x107,
        (
            "#061F啊，嗯。\x02\x03",

            "#560F这个水晶，和结晶回路\x01",
            "构造好像很相似啊。\x02\x03",

            "也许……\x01",
            "如果花点时间，说不定能复原。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1004F真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x107,
        (
            "#560F嗯、嗯。\x02\x03",

            "以前爷爷曾经用『卡佩尔』\x01",
            "复原过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1040F那么，这个水晶\x01",
            "就交给博士好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_1401")


    ChrTalk(    #32
        0x101,
        (
            "#1007F嗯……是啊。\x02\x03",

            "#1006F嗯，可能会有用\x01",
            "姑且保存起来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1440")

    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x8, 360)
    OP_6F(0x9, 0)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6D(580, 200, 43320, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 580, 200, 43320, 0)
    SetChrPos(0x1, 580, 200, 43320, 0)
    SetChrPos(0x2, 580, 200, 43320, 0)
    SetChrPos(0x3, 580, 200, 43320, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x1E06)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_5_8D9 end

    def Function_6_151D(): pass

    label("Function_6_151D")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #33
        (
            "\x07\x05#1S『关于封印机构（１／４）』\x01",
            "　\x01",
            "──我的名字是\x01",
            "赛雷斯托·Ｄ·奥赛雷丝。\x01",
            "是『封■■■』■■创始■\x01",
            "『封■计■■■■负责人。\x01",
            "　\x01",
            "■■，塔■■■■第二结■启动■■■\x01",
            "异次■封■■■■■环』■\x01",
            "■■■■■时■■■■■\x01",
            "留下■■■的■■■■■的载体■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #34
        (
            "\x07\x05#1S■读■这■■■息的■■人\x01",
            "■■■■■■■■■『环■■复活\x01",
            "■把此作为■■那将是■大幸■。\x01",
            "■■■看■期■■环』■■■\x01",
            "我请求■■新考虑■■■■■。\x01",
            "　\x01",
            "『■』■力量■■强大■\x01",
            "不是人类■■子能够处理的事■。\x01",
            "■纳■■之时\x01",
            "也■是■们造■■狱■日。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_6_151D end

    def Function_7_174B(): pass

    label("Function_7_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A49")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_70(0x0, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x4, 0x64)
    OP_B0(0x5, 0x64)
    OP_B0(0x6, 0x64)
    OP_B0(0x7, 0x64)
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1, 0x64)
    OP_B0(0x2, 0x64)
    OP_B0(0x3, 0x64)
    OP_70(0x1, 0x168)
    OP_70(0x2, 0x168)
    OP_70(0x3, 0x168)
    OP_73(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #35
        (
            "\x07\x05#1S『关于封印机构（２／４）』\x01",
            "　\x01",
            "本■■，为消■■『的■■\x01",
            "从而■■人的■■■■\x01",
            "■■立\x01",
            "　\x01",
            "在这里■■■■■大家■\x01",
            "■『环』■身\x01",
            "■全没有要■配■的■■\x01",
            "事■■起■■■\x01",
            "■■我们的■弱和对■■』的过分依■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #36
        (
            "\x07\x05#1S■大的至宝■■■■■■■■■■\x01",
            "■■过于■■\x01",
            "所以■女神的■悲和全能\x01",
            "丝■■■■■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x00得到了\x1F\xFE\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FE, 1)
    OP_A2(0x1E07)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6D(47020, 0, -2740, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 47020, 0, -2740, 0)
    SetChrPos(0x1, 47020, 0, -2740, 0)
    SetChrPos(0x2, 47020, 0, -2740, 0)
    SetChrPos(0x3, 47020, 0, -2740, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_1BAB")

    label("loc_1A49")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #38
        (
            "\x07\x05#1S『关于封印机构（２／４）』\x01",
            "　\x01",
            "本■■，为消■■『的■■\x01",
            "从而■■人的■■■■\x01",
            "■■立\x01",
            "　\x01",
            "在这里■■■■■大家■\x01",
            "■『环』■身\x01",
            "■全没有要■配■的■■\x01",
            "事■■起■■■\x01",
            "■■我们的■弱和对■■』的过分依■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #39
        (
            "\x07\x05#1S■大的至宝■■■■■■■■■■\x01",
            "■■过于■■\x01",
            "所以■女神的■悲和全能\x01",
            "丝■■■■■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1BAB")

    TalkEnd(0xFF)
    Return()

    # Function_7_174B end

    def Function_8_1BAF(): pass

    label("Function_8_1BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED3")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x14, 0x78)
    OP_70(0x14, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x12, 0x64)
    OP_B0(0x13, 0x64)
    OP_B0(0x15, 0x64)
    OP_B0(0x16, 0x64)
    OP_B0(0x17, 0x64)
    OP_70(0x12, 0xF0)
    Sleep(100)
    OP_70(0x13, 0xF0)
    Sleep(100)
    OP_70(0x15, 0xF0)
    Sleep(100)
    OP_70(0x16, 0xF0)
    Sleep(100)
    OP_70(0x17, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0xF, 0x64)
    OP_B0(0x10, 0x64)
    OP_B0(0x11, 0x64)
    OP_70(0xF, 0x168)
    OP_70(0x10, 0x168)
    OP_70(0x11, 0x168)
    OP_73(0xF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #40
        (
            "\x07\x05#1S『关于封印机构（３／４）』\x01",
            "　\x01",
            "■印机构■■■\x01",
            "完■■越■\x01",
            "所谓■民■主义■■\x01",
            "　\x01",
            "即使在我■■中，\x01",
            "■存在着■■\x01",
            "认为■当有效■■■有无■■■的『环■■意见\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        (
            "\x07\x05#1S■是，■『■■■■■■性之后\x01",
            "■■以势不可挡■■■\x01",
            "给社会■■■生活带■■■■■■\x01",
            "■可思议地，■仅仅■■物质■■■■\x01",
            "■■■括■精■层■的■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #42
        "\x07\x00得到了\x1F\xFF\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3FF, 1)
    OP_A2(0x1E08)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 360)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6D(-46490, 200, -3220, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -46490, 200, -3220, 0)
    SetChrPos(0x1, -46490, 200, -3220, 0)
    SetChrPos(0x2, -46490, 200, -3220, 0)
    SetChrPos(0x3, -46490, 200, -3220, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_2044")

    label("loc_1ED3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #43
        (
            "\x07\x05#1S『关于封印机构（３／４）』\x01",
            "　\x01",
            "■印机构■■■\x01",
            "完■■越■\x01",
            "所谓■民■主义■■\x01",
            "　\x01",
            "即使在我■■中，\x01",
            "■存在着■■\x01",
            "认为■当有效■■■有无■■■的『环■■意见\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #44
        (
            "\x07\x05#1S■是，■『■■■■■■性之后\x01",
            "■■以势不可挡■■■\x01",
            "给社会■■■生活带■■■■■■\x01",
            "■可思议地，■仅仅■■物质■■■■\x01",
            "■■■括■精■层■的■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2044")

    TalkEnd(0xFF)
    Return()

    # Function_8_1BAF end

    def Function_9_2048(): pass

    label("Function_9_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E1")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x18, 0x78)
    OP_70(0x18, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x1C, 0x64)
    OP_B0(0x1D, 0x64)
    OP_B0(0x1E, 0x64)
    OP_B0(0x1F, 0x64)
    OP_70(0x1C, 0xF0)
    Sleep(100)
    OP_70(0x1D, 0xF0)
    Sleep(100)
    OP_70(0x1E, 0xF0)
    Sleep(100)
    OP_70(0x1F, 0xF0)
    Sleep(500)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x19, 0x64)
    OP_B0(0x1A, 0x64)
    OP_B0(0x1B, 0x64)
    OP_70(0x19, 0x168)
    OP_70(0x1A, 0x168)
    OP_70(0x1B, 0x168)
    OP_73(0x19)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #45
        (
            "\x07\x05#1S『关于封印机构（４／４）』\x01",
            "　\x01",
            "■■『环』■■■福音』\x01",
            "■市民■■■■来幸■■的■想■实，\x01",
            "■■■至■■控制■■内■质。\x01",
            "　\x01",
            "■可■■时摄■这方面\x01",
            "■与■力无穷■■品和致■剂■■■致\x01",
            "然■■■的■，\x01",
            "这种■■■理方■并没■副■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #46
        (
            "\x07\x05#1S■■恩惠■给人类的真实■在\x01",
            "带来■样深■■■■啊■…\x01",
            "　\x01",
            "这种■■已经在■多市民■■■■现出■，\x01",
            "■■■■的时间太■■。\x01",
            "因此我们■■■意见的■■\x01",
            "在精神上■可能出现的一切困难■■了思■准备\x01",
            "■手■■了■■■■■』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #47
        "\x07\x00得到了\x1F\x00\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x400, 1)
    OP_A2(0x1E09)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x18, 360)
    OP_6F(0x19, 0)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6D(340, 200, -50000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 340, 200, -50000, 0)
    SetChrPos(0x1, 340, 200, -50000, 0)
    SetChrPos(0x2, 340, 200, -50000, 0)
    SetChrPos(0x3, 340, 200, -50000, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_25DE")

    label("loc_23E1")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #48
        (
            "\x07\x05#1S『关于封印机构（４／４）』\x01",
            "　\x01",
            "■■『环』■■■福音』\x01",
            "■市民■■■■来幸■■的■想■实，\x01",
            "■■■至■■控制■■内■质。\x01",
            "　\x01",
            "■可■■时摄■这方面\x01",
            "■与■力无穷■■品和致■剂■■■致\x01",
            "然■■■的■，\x01",
            "这种■■■理方■并没■副■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x05#1S■■恩惠■给人类的真实■在\x01",
            "带来■样深■■■■啊■…\x01",
            "　\x01",
            "这种■■已经在■多市民■■■■现出■，\x01",
            "■■■■的时间太■■。\x01",
            "因此我们■■■意见的■■\x01",
            "在精神上■可能出现的一切困难■■了思■准备\x01",
            "■手■■了■■■■■』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_25DE")

    TalkEnd(0xFF)
    Return()

    # Function_9_2048 end

    def Function_10_25E2(): pass

    label("Function_10_25E2")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_265C"),
        (1, "loc_2662"),
        (SWITCH_DEFAULT, "loc_2668"),
    )


    label("loc_265C")

    OP_A2(0x1200)
    Jump("loc_2668")

    label("loc_2662")

    OP_A2(0x1201)
    Jump("loc_2668")

    label("loc_2668")

    Return()

    # Function_10_25E2 end

    def Function_11_2669(): pass

    label("Function_11_2669")

    FadeToDark(0, 0, -1)
    OP_6D(-33260, 200, 68720, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_2669 end

    def Function_12_26F8(): pass

    label("Function_12_26F8")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x101, 500, 250, 81090, 180)
    SetChrPos(0x102, -500, 250, 81090, 180)
    SetChrPos(0xF8, 500, 250, 82090, 180)
    SetChrPos(0xF9, -500, 250, 82090, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(0, 300, 78810, 0)
    SetChrPos(0x0, 0, 300, 78810, 180)
    SetChrPos(0x1, 0, 300, 78810, 180)
    SetChrPos(0x2, 0, 300, 78810, 180)
    SetChrPos(0x3, 0, 300, 78810, 180)
    EventEnd(0x0)
    Return()

    # Function_12_26F8 end

    def Function_13_27F3(): pass

    label("Function_13_27F3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 81590, 0)
    SetChrPos(0x101, -500, 250, 82090, 0)
    SetChrPos(0x102, 500, 250, 82090, 0)
    SetChrPos(0xF8, -500, 250, 81090, 0)
    SetChrPos(0xF9, 500, 250, 81090, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_27F3 end

    def Function_14_286B(): pass

    label("Function_14_286B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15310, -9350, 15430, 0)
    SetChrPos(0x101, 15810, -9350, 14930, 180)
    SetChrPos(0x102, 14810, -9350, 14930, 180)
    SetChrPos(0xF8, 15810, -9350, 15930, 180)
    SetChrPos(0xF9, 14810, -9350, 15930, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(15150, -9300, 12650, 0)
    SetChrPos(0x0, 15150, -9300, 12650, 180)
    SetChrPos(0x1, 15150, -9300, 12650, 180)
    SetChrPos(0x2, 15150, -9300, 12650, 180)
    SetChrPos(0x3, 15150, -9300, 12650, 180)
    EventEnd(0x0)
    Return()

    # Function_14_286B end

    def Function_15_2966(): pass

    label("Function_15_2966")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15310, -9350, 15430, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 14810, -9350, 15930, 0)
    SetChrPos(0x102, 15810, -9350, 15930, 0)
    SetChrPos(0xF8, 14810, -9350, 14930, 0)
    SetChrPos(0xF9, 15810, -9350, 14930, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2966 end

    def Function_16_2A0A(): pass

    label("Function_16_2A0A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -15810, -9350, -14800, 0)
    SetChrPos(0x102, -14810, -9350, -14800, 0)
    SetChrPos(0xF8, -15810, -9350, -15800, 0)
    SetChrPos(0xF9, -14810, -9350, -15800, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 24)
    Call(0, 26)
    Fade(500)
    OP_6D(-15320, -9650, -10940, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -15320, -9650, -10940, 0)
    SetChrPos(0x1, -15320, -9650, -10940, 0)
    SetChrPos(0x2, -15320, -9650, -10940, 0)
    SetChrPos(0x3, -15320, -9650, -10940, 0)
    EventEnd(0x0)
    Return()

    # Function_16_2A0A end

    def Function_17_2B17(): pass

    label("Function_17_2B17")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-15300, -9350, -15300, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -14810, -9350, -15800, 180)
    SetChrPos(0x102, -15810, -9350, -15800, 180)
    SetChrPos(0xF8, -14810, -9350, -14800, 180)
    SetChrPos(0xF9, -15810, -9350, -14800, 180)
    OP_0D()
    Call(0, 24)
    Call(0, 27)
    NewScene("ED6_DT21/C0702   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2B17 end

    def Function_18_2B98(): pass

    label("Function_18_2B98")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -81000, 0)
    SetChrPos(0x102, 500, 250, -81000, 0)
    SetChrPos(0xF8, -500, 250, -82000, 0)
    SetChrPos(0xF9, 500, 250, -82000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(40, -50, -77230, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 40, -50, -77230, 0)
    SetChrPos(0x1, 40, -50, -77230, 0)
    SetChrPos(0x2, 40, -50, -77230, 0)
    SetChrPos(0x3, 40, -50, -77230, 0)
    EventEnd(0x0)
    Return()

    # Function_18_2B98 end

    def Function_19_2CA5(): pass

    label("Function_19_2CA5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, -81500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 500, 250, -82000, 180)
    SetChrPos(0x102, -500, 250, -82000, 180)
    SetChrPos(0xF8, 500, 250, -81000, 180)
    SetChrPos(0xF9, -500, 250, -81000, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2CA5 end

    def Function_20_2D26(): pass

    label("Function_20_2D26")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 14500, -5750, -15000, 0)
    SetChrPos(0x102, 15500, -5750, -15000, 0)
    SetChrPos(0xF8, 14500, -5750, -16000, 0)
    SetChrPos(0xF9, 15500, -5750, -16000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(15170, -6050, -11100, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 15170, -6050, -11100, 0)
    SetChrPos(0x1, 15170, -6050, -11100, 0)
    SetChrPos(0x2, 15170, -6050, -11100, 0)
    SetChrPos(0x3, 15170, -6050, -11100, 0)
    EventEnd(0x0)
    Return()

    # Function_20_2D26 end

    def Function_21_2E33(): pass

    label("Function_21_2E33")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15000, -5750, -15500, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, 15500, -5750, -16000, 180)
    SetChrPos(0x102, 14500, -5750, -16000, 180)
    SetChrPos(0xF8, 15500, -5750, -15000, 180)
    SetChrPos(0xF9, 14500, -5750, -15000, 180)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_21_2E33 end

    def Function_22_2EB4(): pass

    label("Function_22_2EB4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -14800, -5750, 15000, 180)
    SetChrPos(0x102, -15800, -5750, 15000, 180)
    SetChrPos(0xF8, -14800, -5750, 16000, 180)
    SetChrPos(0xF9, -15800, -5750, 16000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 26)
    Fade(500)
    OP_6D(-15280, -5720, 12800, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -15280, -5720, 12800, 180)
    SetChrPos(0x1, -15280, -5720, 12800, 180)
    SetChrPos(0x2, -15280, -5720, 12800, 180)
    SetChrPos(0x3, -15280, -5720, 12800, 180)
    EventEnd(0x0)
    Return()

    # Function_22_2EB4 end

    def Function_23_2FC1(): pass

    label("Function_23_2FC1")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-15300, -5750, 15500, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -15800, -5750, 16000, 0)
    SetChrPos(0x102, -14800, -5750, 16000, 0)
    SetChrPos(0xF8, -15800, -5750, 15000, 0)
    SetChrPos(0xF9, -14800, -5750, 15000, 0)
    OP_0D()
    Call(0, 25)
    Call(0, 27)
    NewScene("ED6_DT21/C0704   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_23_2FC1 end

    def Function_24_3042(): pass

    label("Function_24_3042")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_24_3042 end

    def Function_25_3135(): pass

    label("Function_25_3135")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_25_3135 end

    def Function_26_3228(): pass

    label("Function_26_3228")


    def lambda_322E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_322E)

    def lambda_3240():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3240)

    def lambda_3252():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3252)

    def lambda_3264():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3264)
    Sleep(2500)
    Return()

    # Function_26_3228 end

    def Function_27_3276(): pass

    label("Function_27_3276")


    def lambda_327C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_327C)

    def lambda_328E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_328E)

    def lambda_32A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_32A0)

    def lambda_32B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_32B2)
    Sleep(2000)
    Return()

    # Function_27_3276 end

    SaveToFile()

Try(main)
