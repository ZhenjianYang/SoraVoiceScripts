from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1401   ._SN',
        MapName             = 'Bose',
        Location            = 'C1401.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60022",
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
        '目标用照相机',                         # 9
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_FF",           # 01, 1
        "Function_2_106",          # 02, 2
        "Function_3_283",          # 03, 3
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6")

    label("loc_D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_FE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_FE")

    Return()

    # Function_0_CA end

    def Function_1_FF(): pass

    label("Function_1_FF")

    OP_71(0x401, 0x0)
    ExitThread()
    Return()

    # Function_1_FF end

    def Function_2_106(): pass

    label("Function_2_106")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_26D")

    label("loc_12B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_26D")

    label("loc_144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_26D")

    label("loc_15D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_26D")

    label("loc_176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_26D")

    label("loc_18F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_26D")

    label("loc_1A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_26D")

    label("loc_1C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_26D")

    label("loc_1DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_26D")

    label("loc_1F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_26D")

    label("loc_20C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_26D")

    label("loc_225")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_26D")

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_257")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_26D")

    label("loc_257")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_26D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_26D")

    label("loc_282")

    Return()

    # Function_2_106 end

    def Function_3_283(): pass

    label("Function_3_283")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x00#40W『不如也试着当游击士看看？』\x01",
            "#500W\x01",
            "#40W契机就是这么简单的一句话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00#40W迪恩、雷斯、洛克——\x01",
            "#500W\x01",
            "#40W聚集在卢安仓库的不良青年组织\x01",
            "『渡鸦帮』的头领三人组。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x00#40W在王国全土遭受前所未有危机的非常时期，\x01",
            "他们也重新审视了自身的价值……\x01",
            "#500W\x01",
            "#40W为将来而烦恼不已的结果，\x01",
            "就是最终选择了守护地区和平与民众安全的道路——\x01",
            "即游击士的道路。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x00#40W话虽如此，这三人——\x01",
            "倒也不是完全没有歪心。\x01",
            "#500W\x01",
            "#40W『能够让卡露娜大姐\x01",
            "　手把手地指导。』\x01",
            "#500W\x01",
            "#40W他们是怀着这种期待，\x01",
            "才叩响游击士协会卢安支部大门的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x00#40W可是由于支部接待员嘉恩的计策——\x01",
            "#500W\x01",
            "#40W他们的指导教官被定为『渡鸦帮』的原首领——\x01",
            "他们的天敌阿加特·科洛斯纳。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x00#40W就这样，在阿加特手下\x01",
            "接受直接指导的他们——\x01",
            "#500W\x01",
            "#40W经过大约三个月地狱般的特训，\x01",
            "以必死的决心突破重重难关——\x01",
            "#500W\x01",
            "#40W——今天，终于要挑战最终考试了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(-6340, 2000, 107480, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(450, 0)
    OP_1D(0x16)
    Sleep(500)
    FadeToBright(2000, 0)

    def lambda_663():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_663)

    def lambda_67B():
        OP_6E(356, 10000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_67B)
    WaitChrThread(0x10, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1410   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_283 end

    SaveToFile()

Try(main)
