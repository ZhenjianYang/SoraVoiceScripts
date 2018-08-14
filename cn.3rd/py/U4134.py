from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4134   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4134.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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


    DeclActor(
        TriggerX            = 2900,
        TriggerZ            = 1000,
        TriggerY            = 20280,
        TriggerRange        = 1000,
        ActorX              = 2750,
        ActorZ              = 2000,
        ActorY              = 21270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72040,
        TriggerZ            = 4000,
        TriggerY            = 4910,
        TriggerRange        = 1000,
        ActorX              = 71980,
        ActorZ              = 5000,
        ActorY              = 5610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -77000,
        TriggerZ            = 0,
        TriggerY            = 7000,
        TriggerRange        = 1000,
        ActorX              = -77000,
        ActorZ              = 1000,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -131880,
        TriggerZ            = 0,
        TriggerY            = 6130,
        TriggerRange        = 1000,
        ActorX              = -132000,
        ActorZ              = 3000,
        ActorY              = 7000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74960,
        TriggerZ            = 0,
        TriggerY            = 65920,
        TriggerRange        = 800,
        ActorX              = -74960,
        ActorZ              = 1000,
        ActorY              = 65920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_17B",          # 01, 1
        "Function_2_1DD",          # 02, 2
        "Function_3_303",          # 03, 3
        "Function_4_429",          # 04, 4
        "Function_5_54F",          # 05, 5
        "Function_6_5C3",          # 06, 6
        "Function_7_79B",          # 07, 7
        "Function_8_851",          # 08, 8
        "Function_9_8FC",          # 09, 9
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_17A")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 8)
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17A")

    Return()

    # Function_0_15E end

    def Function_1_17B(): pass

    label("Function_1_17B")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_18E")
    OP_82(0x81, 0x0)
    Jump("loc_191")

    label("loc_18E")

    OP_82(0x82, 0x0)

    label("loc_191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3")
    OP_6F(0x11, 0)
    Jump("loc_1AA")

    label("loc_1A3")

    OP_6F(0x11, 60)

    label("loc_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC")
    OP_6F(0x12, 0)
    Jump("loc_1C3")

    label("loc_1BC")

    OP_6F(0x12, 60)

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5")
    OP_6F(0x13, 0)
    Jump("loc_1DC")

    label("loc_1D5")

    OP_6F(0x13, 60)

    label("loc_1DC")

    Return()

    # Function_1_17B end

    def Function_2_1DD(): pass

    label("Function_2_1DD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_251")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_236")

    label("loc_236")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278B)
    Jump("loc_2BF")

    label("loc_251")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_2A0")

    label("loc_2A0")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_2BF")

    Jump("loc_2F5")

    label("loc_2C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2F5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1DD end

    def Function_3_303(): pass

    label("Function_3_303")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_377")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_35C")

    label("loc_35C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278C)
    Jump("loc_3E5")

    label("loc_377")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_3C6")

    label("loc_3C6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_3E5")

    Jump("loc_41B")

    label("loc_3E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_41B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_303 end

    def Function_4_429(): pass

    label("Function_4_429")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4FA, 1)"), scpexpr(EXPR_END)), "loc_49D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFA\x04\x07\x00。\x02",
    )

    Jump("loc_482")

    label("loc_482")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278D)
    Jump("loc_50B")

    label("loc_49D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFA\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFA\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4EC")

    label("loc_4EC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_50B")

    Jump("loc_541")

    label("loc_50E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_541")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_429 end

    def Function_5_54F(): pass

    label("Function_5_54F")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
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

    Jump("loc_5AC")

    label("loc_5AC")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_5_54F end

    def Function_6_5C3(): pass

    label("Function_6_5C3")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -132630, 0, 4570, 0)
    SetChrPos(0x1, -130870, 0, 4490, 0)
    SetChrPos(0x2, -132550, 0, 2760, 0)
    SetChrPos(0x3, -130530, 0, 2570, 0)
    OP_6D(-131590, 0, 5430, 0)
    OP_67(0, 3910, -10000, 0)
    OP_6B(4220, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699")
    OP_28(0x13, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_699")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #10
        (
            "\x07\x05#40W　　　无『武勋』者，\x01",
            " 毫无穿越此『门』之价值……\x01",
            "#500W\x01",
            "#40W若欲获得认可，请历经百战……\x01",
            "　当汝等获得１００场胜利之时，\x01",
            "　则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x18), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_78F")
    Call(0, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78C")
    Call(0, 7)

    label("loc_78C")

    Jump("loc_78F")

    label("loc_78F")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_6_5C3 end

    def Function_7_79B(): pass

    label("Function_7_79B")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x15)
    Sleep(500)

    def lambda_804():
        OP_6B(3400, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_804)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x1E, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_79B end

    def Function_8_851(): pass

    label("Function_8_851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -132630, 0, 4570, 0)
    SetChrPos(0x1, -130870, 0, 4490, 0)
    SetChrPos(0x2, -132550, 0, 2760, 0)
    SetChrPos(0x3, -130530, 0, 2570, 0)
    OP_6D(-131590, 0, 5430, 0)
    OP_67(0, 3910, -10000, 0)
    OP_6B(4220, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_8_851 end

    def Function_9_8FC(): pass

    label("Function_9_8FC")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_8FC end

    SaveToFile()

Try(main)
