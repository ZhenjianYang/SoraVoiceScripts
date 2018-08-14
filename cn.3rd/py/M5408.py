from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5408   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5408.x',
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
        TriggerX            = 4670,
        TriggerZ            = 0,
        TriggerY            = -64739,
        TriggerRange        = 1000,
        ActorX              = 4670,
        ActorZ              = 2000,
        ActorY              = -64739,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_10A",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_D66",          # 03, 3
        "Function_4_D8B",          # 04, 4
        "Function_5_DB0",          # 05, 5
        "Function_6_DD5",          # 06, 6
        "Function_7_DFA",          # 07, 7
        "Function_8_FF8",          # 08, 8
        "Function_9_1290",         # 09, 9
        "Function_10_141E",        # 0A, 10
        "Function_11_1579",        # 0B, 11
        "Function_12_168F",        # 0C, 12
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_E6"),
        (SWITCH_DEFAULT, "loc_ED"),
    )


    label("loc_E6")

    Event(0, 9)
    Jump("loc_ED")

    label("loc_ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_109")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_109")

    Return()

    # Function_0_CE end

    def Function_1_10A(): pass

    label("Function_1_10A")

    OP_1B(0x3, 0x0, 0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_12D")
    OP_71(0x404, 0x0)
    ExitThread()

    label("loc_12D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E")

    Return()

    # Function_1_10A end

    def Function_2_13F(): pass

    label("Function_2_13F")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -160, 0, -34200, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4")
    SetChrPos(0xEF, 870, 0, -34950, 180)
    SetChrPos(0xF0, 1720, 0, -34090, 180)
    SetChrPos(0xF1, 810, 0, -33230, 180)
    Jump("loc_229")

    label("loc_1A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E8")
    SetChrPos(0xF0, 870, 0, -34950, 180)
    SetChrPos(0xEF, 1720, 0, -34090, 180)
    SetChrPos(0xF1, 810, 0, -33230, 180)
    Jump("loc_229")

    label("loc_1E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229")
    SetChrPos(0xF1, 870, 0, -34950, 180)
    SetChrPos(0xEF, 1720, 0, -34090, 180)
    SetChrPos(0xF0, 810, 0, -33230, 180)

    label("loc_229")

    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(1120, 400, -34000, 0)
    OP_67(0, 6660, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(32000, 0)
    OP_6E(332, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_398():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_398)

    def lambda_3AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3AA)

    def lambda_3BC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3BC)

    def lambda_3CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3CE)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_423")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_44B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_48A")

    label("loc_473")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_48A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_4B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_4DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_507")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51E")

    label("loc_507")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_51E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_54B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_573")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5B2")

    label("loc_59B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5B2")

    Sleep(1000)

    ChrTalk(    #0
        0x102,
        "#1506F#5P这是……！\x02",
    )

    CloseMessageWindow()
    OP_1D(0xEA)
    Sleep(300)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(1510, 0, -33570, 0)
    OP_67(0, 8440, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(466, 0)

    def lambda_62B():
        OP_6D(8039, -23200, -45530, 10000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_62B)

    def lambda_643():
        OP_67(0, 9560, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_643)

    def lambda_65B():
        OP_6B(12760, 10000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_65B)

    def lambda_66B():
        OP_6E(583, 10000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_66B)
    OP_C8(0x200, 0x46, "C_PLAC36._CH", 0x0, 0xDAC)
    Sleep(2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71B")

    def lambda_6A3():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_6A3)
    Sleep(150)

    def lambda_6C3():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C3)
    Sleep(250)

    def lambda_6E3():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6E3)
    Sleep(150)

    def lambda_703():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_703)
    Jump("loc_830")

    label("loc_71B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A7")

    def lambda_72F():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_72F)
    Sleep(150)

    def lambda_74F():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74F)
    Sleep(250)

    def lambda_76F():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_76F)
    Sleep(150)

    def lambda_78F():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_78F)
    Jump("loc_830")

    label("loc_7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_830")

    def lambda_7BB():
        OP_8F(0xFE, 0x514, 0x0, 0xFFFF5D8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7BB)
    Sleep(150)

    def lambda_7DB():
        OP_8F(0xFE, 0xFFFFFF4C, 0x0, 0xFFFF5D94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7DB)
    Sleep(250)

    def lambda_7FB():
        OP_8F(0xFE, 0x60E, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7FB)
    Sleep(150)

    def lambda_81B():
        OP_8F(0xFE, 0xFFFFFF74, 0x0, 0xFFFF6316, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_81B)

    label("loc_830")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_43(0xEE, 0x0, 0x0, 0x3)
    OP_43(0xEF, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    WaitChrThread(0xEE, 0x1)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    SetMapFlags(0x10)
    OP_6D(1500, 0, -40100, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_956")

    ChrTalk(    #1
        0x110,
        (
            "#1306F#5P『红色方舟』古罗力亚斯……\x02\x03",

            "可船身的颜色\x01",
            "就像乌鸦一样漆黑。\x02\x03",

            "#261F嘻嘻，\x01",
            "是不是吃了什么烧焦的东西了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE")

    label("loc_956")


    ChrTalk(    #2
        0x109,
        (
            "#1065F#5P『红色方舟』古罗力亚斯……\x02\x03",

            "#1063F可是这好像是\x01",
            "黑色的船体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A68")

    ChrTalk(    #3
        0x101,
        "#1002F#5P的、的确是『黑色方舟』呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1505F#5P以眼前所见，\x01",
            "船体的大小形状和原型都是一样的。\x02\x03",

            "#1502F看来要进船舱里面，\x01",
            "调查一下情况才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1D")

    ChrTalk(    #5
        0x10B,
        "#212F#5P的确是『黑色方舟』呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1505F#5P以眼前所见，\x01",
            "船体的大小形状和原型都是一样的。\x02\x03",

            "#1502F看来要进船舱里面，\x01",
            "调查一下情况才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_B1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCB")

    ChrTalk(    #7
        0x102,
        (
            "#1505F#5P嗯……\x01",
            "的确是『黑色方舟』啊。\x02\x03",

            "#1502F以眼前所见，\x01",
            "船体的大小形状和原型都是一样的。\x02\x03",

            "看来要进船舱里面，\x01",
            "调查一下情况才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C78")

    ChrTalk(    #8
        0x102,
        (
            "#1505F#5P嗯嗯……\x01",
            "的确是『黑色方舟』啊。\x02\x03",

            "#1502F以眼前所见，\x01",
            "船体的大小形状和原型都是一样的。\x02\x03",

            "看来要进船舱里面，\x01",
            "调查一下情况才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78")


    ChrTalk(    #9
        0x109,
        (
            "#1841F#5P是啊，不愧是最后的领域……\x01",
            "看来这里并不是一个容易对付的地方。\x02\x03",

            "#1063F和研究所一样，\x01",
            "这里很可能有结社的人形兵器在游荡。\x02\x03",

            "前进的时候要多加留意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1500F#5P嗯……明白。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B23)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x3A, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_13F end

    def Function_3_D66(): pass

    label("Function_3_D66")

    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_D66 end

    def Function_4_D8B(): pass

    label("Function_4_D8B")

    Sleep(200)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 15, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_D8B end

    def Function_5_DB0(): pass

    label("Function_5_DB0")

    Sleep(600)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_DB0 end

    def Function_6_DD5(): pass

    label("Function_6_DD5")

    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_DD5 end

    def Function_7_DFA(): pass

    label("Function_7_DFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(1000, 2650, -37750, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(0, 0)
    OP_6E(341, 0)

    def lambda_E5D():
        OP_6D(1000, 4550, -23050, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E5D)

    def lambda_E75():
        OP_67(0, 3810, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_E75)

    def lambda_E8D():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_E8D)

    def lambda_E9D():
        OP_6C(0, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_E9D)

    def lambda_EAD():
        OP_6E(350, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_EAD)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    Fade(1000)

    def lambda_ED6():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_ED6)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_35(0xA, 0x113)
    OP_BB(0xA, 0x6, 0x113)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F55")

    AnonymousTalk(    #11
        (
            "\x07\x05乔丝特学会了Ｓ战技\x01",
            "\x07\x02『山猫号Ⅱ』\x07\x05。\x02",
        )
    )

    Jump("loc_F51")

    label("loc_F51")

    CloseMessageWindow()
    Jump("loc_F86")

    label("loc_F55")


    AnonymousTalk(    #12
        (
            "\x07\x05乔丝特的Ｓ战技\x01",
            "\x07\x02『山猫号』\x07\x05得到了强化。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F86")

    OP_22(0x21E, 0x0, 0x64)

    AnonymousTalk(    #13
        (
            "\x07\x05由于多伦和吉尔也参与援助，\x01",
            "附加了格林机枪的攻击，\x01",
            "并可以发出强力的导弹。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5406   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_DFA end

    def Function_8_FF8(): pass

    label("Function_8_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C7")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(7168)
    Sleep(500)
    Jump("loc_10CA")

    label("loc_10C7")

    TalkBegin(0xFF)

    label("loc_10CA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #14
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_10F4")

    label("loc_10F4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1107")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125F")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_1159")

    label("loc_1159")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1176"),
        (1, "loc_11F1"),
        (2, "loc_1220"),
        (SWITCH_DEFAULT, "loc_124F"),
    )


    label("loc_1176")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xEA)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_125C")

    label("loc_11F1")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #15
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_121D")

    label("loc_121D")

    Jump("loc_125C")

    label("loc_1220")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_124C")

    label("loc_124C")

    Jump("loc_125C")

    label("loc_124F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_125C")

    label("loc_125C")

    Jump("loc_1107")

    label("loc_125F")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128C")
    OP_A2(0x259E)
    EventEnd(0x1)
    Jump("loc_128F")

    label("loc_128C")

    TalkEnd(0xFF)

    label("loc_128F")

    Return()

    # Function_8_FF8 end

    def Function_9_1290(): pass

    label("Function_9_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A1")
    Call(0, 2)
    Return()

    label("loc_12A1")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 850, 0, -34850, 180)
    SetChrPos(0x1, 10, 0, -34040, 180)
    SetChrPos(0x2, 1640, 0, -34010, 180)
    SetChrPos(0x3, 810, 0, -33180, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 11)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1290 end

    def Function_10_141E(): pass

    label("Function_10_141E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 850, 0, -34850, 0)
    SetChrPos(0x2, 10, 0, -34040, 0)
    SetChrPos(0x1, 1640, 0, -34010, 0)
    SetChrPos(0x0, 810, 0, -33180, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xEE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xEF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xF1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 12)
    NewScene("ED6_DT21/M4110   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_10_141E end

    def Function_11_1579(): pass

    label("Function_11_1579")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1596():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1596)

    label("loc_15A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_15BF)

    label("loc_15CB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F4")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_15E8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_15E8)

    label("loc_15F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_161D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1611():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1611)

    label("loc_161D")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1649")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1649")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1660")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1660")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1677")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_1677")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_168E")

    Return()

    # Function_11_1579 end

    def Function_12_168F(): pass

    label("Function_12_168F")


    def lambda_1695():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1695)

    def lambda_16A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_16A7)

    def lambda_16B9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_16B9)

    def lambda_16CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_16CB)
    Sleep(1000)
    Return()

    # Function_12_168F end

    SaveToFile()

Try(main)
