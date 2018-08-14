from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P0311   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        TriggerX            = -2400,
        TriggerZ            = 0,
        TriggerY            = 53230,
        TriggerRange        = 1000,
        ActorX              = -2250,
        ActorZ              = 1000,
        ActorY              = 53930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3600,
        TriggerZ            = 0,
        TriggerY            = -38500,
        TriggerRange        = 1000,
        ActorX              = 3600,
        ActorZ              = 1000,
        ActorY              = -38500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_11C",          # 01, 1
        "Function_2_16C",          # 02, 2
        "Function_3_292",          # 03, 3
        "Function_4_388",          # 04, 4
        "Function_5_444",          # 05, 5
        "Function_6_5A0",          # 06, 6
        "Function_7_5D9",          # 07, 7
        "Function_8_609",          # 08, 8
        "Function_9_639",          # 09, 9
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_108")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_11B")

    label("loc_108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_11B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_11B")

    Return()

    # Function_0_F2 end

    def Function_1_11C(): pass

    label("Function_1_11C")

    OP_B1("P0311_2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139")
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x1007, 0x0)
    ExitThread()

    label("loc_139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B")
    OP_6F(0xC, 0)
    Jump("loc_152")

    label("loc_14B")

    OP_6F(0xC, 60)

    label("loc_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164")
    OP_6F(0xD, 0)
    Jump("loc_16B")

    label("loc_164")

    OP_6F(0xD, 60)

    label("loc_16B")

    Return()

    # Function_1_11C end

    def Function_2_16C(): pass

    label("Function_2_16C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x26B, 1)"), scpexpr(EXPR_END)), "loc_1E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x6B\x02\x07\x00。\x02",
    )

    Jump("loc_1C5")

    label("loc_1C5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2690)
    Jump("loc_24E")

    label("loc_1E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x6B\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6B\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_22F")

    label("loc_22F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_24E")

    Jump("loc_284")

    label("loc_251")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_284")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_16C end

    def Function_3_292(): pass

    label("Function_3_292")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_6F(0xD, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1)"), scpexpr(EXPR_END)), "loc_2E7")
    Jump("loc_2E7")

    label("loc_2E7")


    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02啪啪啦海鲜饭\x07\x00的食谱。\x02",
    )

    Jump("loc_318")

    label("loc_318")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x06\x07\x02啪啪啦海鲜饭\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_34A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2691)
    Jump("loc_376")

    label("loc_35C")


    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_376")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_292 end

    def Function_4_388(): pass

    label("Function_4_388")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(2870, 0, 3830, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_22(0x9C, 0x0, 0x64)
    OP_0D()
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_6F(0x7, 0)
    OP_70(0x7, 0xF)
    OP_73(0x7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1007, 0x0)
    ExitThread()
    OP_A2(0x2617)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_388 end

    def Function_5_444(): pass

    label("Function_5_444")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10E, -290, 150, -35430, 180)
    SetChrPos(0x109, -290, 150, -35430, 180)
    SetChrPos(0x10F, -290, 150, -35430, 180)
    SetChrPos(0x107, -290, 150, -35430, 180)
    OP_6D(1250, 0, -37400, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_6F(0x6, 0)
    OP_70(0x6, 0xF)
    OP_73(0x6)

    def lambda_4F8():
        OP_6D(1310, 0, -42970, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F8)

    def lambda_510():
        OP_67(0, 6060, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_510)

    def lambda_528():
        OP_6B(2880, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_528)

    def lambda_538():
        OP_6E(279, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_538)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    Sleep(800)
    OP_43(0x109, 0x0, 0x0, 0x7)
    Sleep(1000)
    OP_43(0x10F, 0x0, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0x9)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0313   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_444 end

    def Function_6_5A0(): pass

    label("Function_6_5A0")

    OP_8E(0xFE, 0xFFFFFE8E, 0x0, 0xFFFF5A56, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 135, 400)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Return()

    # Function_6_5A0 end

    def Function_7_5D9(): pass

    label("Function_7_5D9")

    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6BF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0x0, 0xFFFF6320, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_7_5D9 end

    def Function_8_609(): pass

    label("Function_8_609")

    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6BF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x578, 0x0, 0xFFFF6654, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_609 end

    def Function_9_639(): pass

    label("Function_9_639")

    OP_8E(0xFE, 0xFFFFFFA6, 0x0, 0xFFFF69BA, 0x7D0, 0x0)
    OP_6F(0x6, 15)
    OP_70(0x6, 0x0)
    OP_73(0x6)
    OP_71(0x1006, 0x0)
    ExitThread()
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_9_639 end

    SaveToFile()

Try(main)
