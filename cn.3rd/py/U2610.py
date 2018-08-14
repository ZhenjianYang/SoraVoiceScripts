from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U2610   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U2610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '管家菲利普',                           # 9
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
        'ED6_DT07/CH02470 ._CH',             # 00
        'ED6_DT26/CH20714 ._CH',             # 01
        'ED6_DT27/CH04410 ._CH',             # 02
        'ED6_DT27/CH04411 ._CH',             # 03
        'ED6_DT27/CH04414 ._CH',             # 04
        'ED6_DT27/CH04419 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02470P._CP',             # 00
        'ED6_DT26/CH20714P._CP',             # 01
        'ED6_DT27/CH04410P._CP',             # 02
        'ED6_DT27/CH04411P._CP',             # 03
        'ED6_DT27/CH04414P._CP',             # 04
        'ED6_DT27/CH04419P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 300,
        TriggerY            = 32200,
        TriggerRange        = 1000,
        ActorX              = -80200,
        ActorZ              = 1300,
        ActorY              = 32200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_150",          # 01, 1
        "Function_2_16A",          # 02, 2
        "Function_3_2C1",          # 03, 3
        "Function_4_2CA",          # 04, 4
        "Function_5_1661",         # 05, 5
        "Function_6_1C99",         # 06, 6
        "Function_7_1D58",         # 07, 7
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_136")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 7)
    Jump("loc_14F")

    label("loc_136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_14F")

    Return()

    # Function_0_11E end

    def Function_1_150(): pass

    label("Function_1_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162")
    OP_6F(0xB, 0)
    Jump("loc_169")

    label("loc_162")

    OP_6F(0xB, 60)

    label("loc_169")

    Return()

    # Function_1_150 end

    def Function_2_16A(): pass

    label("Function_2_16A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x575, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x1E)
    OP_73(0xB)
    OP_6F(0xB, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0xC8)
    AddSepith(0x1, 0xC8)
    AddSepith(0x2, 0xC8)
    AddSepith(0x3, 0xC8)
    AddSepith(0x4, 0xC8)
    AddSepith(0x5, 0xC8)
    AddSepith(0x6, 0xC8)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×２００\x01",
            "\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x02#58I火之耀晶片×２００\x01",
            "\x07\x02#59I风之耀晶片×２００\x01",
            "\x07\x02#62I时之耀晶片×２００\x01",
            "\x07\x02#60I空之耀晶片×２００\x01",
            "\x07\x02#61I幻之耀晶片×２００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2BAB)
    Jump("loc_2AF")

    label("loc_293")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_2AF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_16A end

    def Function_3_2C1(): pass

    label("Function_3_2C1")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_2C1 end

    def Function_4_2CA(): pass

    label("Function_4_2CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_E0(238, 0x46, 0x2)
    OP_E0(238, 0x47, 0x3)
    OP_E0(239, 0x48, 0x2)
    OP_E0(239, 0x49, 0x3)
    OP_E0(240, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x3)
    OP_E0(241, 0x4C, 0x2)
    OP_E0(241, 0x4D, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 2000, 24770, 180)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -970, 0, 3040, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    SetChrPos(0xEF, 570, 0, 2840, 0)
    SetChrPos(0xF0, -1170, 0, 1320, 0)
    SetChrPos(0xF1, 590, 0, 1090, 0)
    Jump("loc_407")

    label("loc_382")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6")
    SetChrPos(0xF0, 570, 0, 2840, 0)
    SetChrPos(0xEF, -1170, 0, 1320, 0)
    SetChrPos(0xF1, 590, 0, 1090, 0)
    Jump("loc_407")

    label("loc_3C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407")
    SetChrPos(0xF1, 570, 0, 2840, 0)
    SetChrPos(0xEF, -1170, 0, 1320, 0)
    SetChrPos(0xF0, 590, 0, 1090, 0)

    label("loc_407")

    OP_6D(920, 0, 3200, 0)
    OP_67(0, 6880, -10000, 0)
    OP_6B(2340, 0)
    OP_6C(45000, 0)
    OP_6E(304, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #2
        0x10,
        "男性的声音",
        "#4P我一直在等着你们。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_526")

    label("loc_4BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_526")

    label("loc_4E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_526")

    label("loc_50F")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_526")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_553")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BA")

    label("loc_553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BA")

    label("loc_57B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5BA")

    label("loc_5A3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5BA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_64E")

    label("loc_5E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_64E")

    label("loc_60F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_637")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_64E")

    label("loc_637")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_64E")

    Sleep(1000)

    def lambda_659():
        OP_6D(860, 2000, 25480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_659)

    def lambda_671():
        OP_67(0, 5630, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_671)

    def lambda_689():
        OP_6B(2770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_689)

    def lambda_699():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_699)

    def lambda_6A9():
        OP_6E(256, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6A9)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #3
        0x109,
        "#1064F#1P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        "#1164F#1P菲，菲利普先生！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(1910, 50, 21210, 0)
    OP_67(0, 5890, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(395, 0)
    SetChrPos(0x109, -1210, 0, 8970, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79C")
    SetChrPos(0xEF, 550, 0, 8340, 0)
    SetChrPos(0xF0, -1530, 0, 7100, 0)
    SetChrPos(0xF1, 620, 0, 6370, 0)
    Jump("loc_821")

    label("loc_79C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E0")
    SetChrPos(0xF0, 550, 0, 8340, 0)
    SetChrPos(0xEF, -1530, 0, 7100, 0)
    SetChrPos(0xF1, 620, 0, 6370, 0)
    Jump("loc_821")

    label("loc_7E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_821")
    SetChrPos(0xF1, 550, 0, 8340, 0)
    SetChrPos(0xEF, -1530, 0, 7100, 0)
    SetChrPos(0xF0, 620, 0, 6370, 0)

    label("loc_821")


    def lambda_827():
        OP_8F(0xFE, 0xFFFFFD3A, 0x0, 0x4092, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_827)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AD")

    def lambda_855():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_855)
    Sleep(100)

    def lambda_875():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_875)
    Sleep(100)

    def lambda_895():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_895)
    Jump("loc_982")

    label("loc_8AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")

    def lambda_8C1():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8C1)
    Sleep(100)

    def lambda_8E1():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8E1)
    Sleep(100)

    def lambda_901():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_901)
    Jump("loc_982")

    label("loc_919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")

    def lambda_92D():
        OP_8F(0xFE, 0x2BC, 0x0, 0x4074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_92D)
    Sleep(100)

    def lambda_94D():
        OP_8F(0xFE, 0xFFFFFB28, 0x0, 0x39F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_94D)
    Sleep(100)

    def lambda_96D():
        OP_8F(0xFE, 0x3CA, 0x0, 0x3AE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_96D)

    label("loc_982")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #5
        0x10,
        (
            "#720F既然你们能来到这里，\x01",
            "就是说已经突破了那些年轻人的防守了。\x02\x03",

            "请恕我不自量力，\x01",
            "接下来就由我来做各位的对手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        (
            "#1063F#6P……看来，\x01",
            "你也是由『影之王』\x01",
            "所再现出来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#722F嗯，说的没错。\x02\x03",

            "虽然我知道用剑指向\x01",
            "王太女殿下罪该万死，\x01",
            "但也不得不这么做。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_AD5():
        OP_6D(1500, 500, 22210, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_AD5)

    def lambda_AED():
        OP_67(0, 5890, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_AED)

    def lambda_B05():
        OP_6B(2200, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_B05)

    def lambda_B15():
        OP_6E(395, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B15)
    WaitChrThread(0xEE, 0x0)
    OP_22(0x1F5, 0x0, 0x64)
    OP_99(0x10, 0x1, 0x7, 0x4B0)
    OP_22(0x1F8, 0x0, 0x64)
    OP_99(0x10, 0x7, 0x8, 0x4B0)
    Sleep(500)
    Fade(500)
    OP_6D(0, 1800, 22110, 0)
    OP_67(0, 2160, -10000, 0)
    OP_6B(6150, 0)
    OP_6C(0, 0)
    OP_6E(158, 0)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -630, 0, 17050, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF0")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xF0, -1230, 0, 14540, 0)
    SetChrPos(0xF1, 1270, 0, 14310, 0)
    Jump("loc_C75")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xEF, -1230, 0, 14540, 0)
    SetChrPos(0xF1, 1270, 0, 14310, 0)
    Jump("loc_C75")

    label("loc_C34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    SetChrPos(0x105, 650, 0, 16900, 0)
    SetChrPos(0xEF, -1230, 0, 14540, 0)
    SetChrPos(0xF0, 1270, 0, 14310, 0)

    label("loc_C75")

    OP_0D()
    OP_1D(0x99)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#721F#5P原王室亲卫队大队长，\x01",
            "『剑狐』菲利普·鲁纳尔。\x02\x03",

            "请允许我以第一『守护者』的身份\x01",
            "来当各位的对手。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 6)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 8)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 10)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(    #9
        0x107,
        "#065F#5P哇、哇……\x02",
    )

    CloseMessageWindow()

    label("loc_D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD6")

    ChrTalk(    #10
        0x10B,
        (
            "#216F#5P这老爷爷明明看起来这么拘礼，\x01",
            "却给人一股强烈的压迫感觉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1B")

    ChrTalk(    #11
        0x10A,
        (
            "#1317F#5P他的架势……\x01",
            "竟然没有一点破绽！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(    #12
        0x101,
        (
            "#1002F#5P没、没想到要和\x01",
            "菲利普先生战斗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#722F#5P要和大恩人\x01",
            "艾丝蒂尔兵戎相见\x01",
            "我本来也很不情愿……\x02\x03",

            "#721F不过这大概也是命运的安排。\x01",
            "希望您不要有多余的顾虑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006F#5P嗯……！\x02\x03",

            "那我就全力以赴\x01",
            "向您挑战了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1001")

    ChrTalk(    #15
        0x10E,
        (
            "#178F#5P呜……\x01",
            "这次竟然能够亲眼见识\x01",
            "『魔鬼大队长』的传说……\x02\x03",

            "#177F菲利普大人！\x01",
            "我将全力向您挑战！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#720F哈哈……\x01",
            "人老不中用了。\x02\x03",

            "我要拼上这一把老骨头\x01",
            "全力以赴才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1001")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D2")

    ChrTalk(    #17
        0x102,
        (
            "#1505F#5P能够独自与\x01",
            "四名『执行者』对峙的实力……\x02\x03",

            "#1502F我将全力向您挑战！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#720F哈哈……\x01",
            "这实在是有些太抬高我了。\x02\x03",

            "我才要拼上这一把老骨头\x01",
            "和各位切磋学习呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D4")

    ChrTalk(    #19
        0x10C,
        (
            "#115F#5P虽然之前在情报部\x01",
            "也曾经对您的经历进行过调查……\x02\x03",

            "#118F不过当现在面对面交锋的时候，\x01",
            "才真正感觉到您令人不寒而栗的剑气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#720F彼此彼此……\x01",
            "不愧是『剑圣』的后继者。\x02\x03",

            "可要让我亲眼见识一下\x01",
            "您的华丽剑技。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1339")

    ChrTalk(    #21
        0x110,
        (
            "#1306F#5P呵呵……\x01",
            "细眼睛的老爷爷，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#721F小姑娘……\x01",
            "我们以前在王城见过对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x110,
        (
            "#1305F#5P嘻嘻……\x01",
            "那时候老爷爷的剑，\x01",
            "可是十分厉害的呢。\x02\x03",

            "#266F不过，当时老爷爷\x01",
            "光和瓦鲁特和布卢布兰玩，\x01",
            "都没顾得上理我。\x02\x03",

            "#1306F嘻嘻……\x01",
            "这次就来陪我玩个尽兴吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#722F哎呀……\x01",
            "只要您乐意就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1339")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1383")

    ChrTalk(    #25
        0x10F,
        (
            "#1446F#5P……看来这是一场\x01",
            "无法避免的战斗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1495")

    label("loc_1383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C8")

    ChrTalk(    #26
        0x108,
        (
            "#074F#5P看来这是一场\x01",
            "无法避免的战斗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1495")

    label("loc_13C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140D")

    ChrTalk(    #27
        0x106,
        (
            "#053F#5P看来这是一场\x01",
            "无法避免的战斗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1495")

    label("loc_140D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1453")

    ChrTalk(    #28
        0x103,
        (
            "#1526F#5P看来这是一场\x01",
            "无法避免的战斗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1495")

    label("loc_1453")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1495")

    ChrTalk(    #29
        0x10D,
        (
            "#272F#5P看来这是一场\x01",
            "无法避免的战斗了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D2")

    ChrTalk(    #30
        0x104,
        (
            "#1541F#5P呼……\x01",
            "这也是命中注定吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D2")


    ChrTalk(    #31
        0x105,
        (
            "#1162F#5P……我知道了。\x01",
            "我们也不会手软的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1069F#5P第一『守护者』──\x01",
            "来光明正大地打一场吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_155C():
        OP_6D(0, 250, 22010, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_155C)

    def lambda_1574():
        OP_67(0, 3380, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1574)

    def lambda_158C():
        OP_6B(2700, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_158C)

    def lambda_159C():
        OP_6E(280, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_159C)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 7)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_15BB():
        OP_96(0xFE, 0x0, 0xFFFFFFCE, 0x4CF4, 0x1F4, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_15BB)

    def lambda_15D9():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_15D9)

    def lambda_15F4():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_15F4)

    def lambda_160F():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_160F)

    def lambda_162A():
        OP_91(0xFE, 0x0, 0x0, 0x1F40, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_162A)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x29F, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_2CA end

    def Function_5_1661(): pass

    label("Function_5_1661")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 20340, 180)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    OP_43(0x10, 0x3, 0x0, 0x6)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 600, 100, 0, 0, 0, 2200, 2300, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -830, -50, 17700, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")
    SetChrPos(0xEF, 470, 0, 17700, 0)
    SetChrPos(0xF0, -1190, 0, 16200, 0)
    SetChrPos(0xF1, 690, 0, 16200, 0)
    Jump("loc_17F0")

    label("loc_176B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AF")
    SetChrPos(0xF0, 470, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_17F0")

    label("loc_17AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    SetChrPos(0xF1, 470, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF0, 690, 0, 16620, 0)

    label("loc_17F0")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2029, -900, 20500, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(316, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#724F#5P哎呀哎呀，\x01",
            "我这把老骨头果然还是不够用吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1068F#6P说、说得倒轻松……\x02\x03",

            "完全是超强的实力嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1921")

    ChrTalk(    #35
        0x101,
        "#1007F#6P您、您太客气了……\x02",
    )

    CloseMessageWindow()

    label("loc_1921")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B2")

    ChrTalk(    #36
        0x10E,
        (
            "#176F#6P『魔鬼大队长』的传说……\x01",
            "我已经亲眼见识到了。\x02\x03",

            "#175F作为亲卫队的队员……\x01",
            "我再次深刻体会到了自己的不足。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19FE")

    ChrTalk(    #37
        0x10C,
        (
            "#111F#6P请恕我有眼无珠。\x01",
            "竟然不知道您这么厉害……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A49")

    ChrTalk(    #38
        0x102,
        (
            "#1514F#6P不愧是能够拖住\x01",
            "『执行者』们的人物啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A83")

    ChrTalk(    #39
        0x110,
        (
            "#261F#6P嘻嘻……\x01",
            "我今天很尽兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A83")


    ChrTalk(    #40
        0x10,
        (
            "#724F#5P哈哈……\x01",
            "客套话就不要再说了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #41
        0x10,
        (
            "#721F#5P在前方等待你们的\x01",
            "是比我更厉害的对手。\x02\x03",

            "你们要做好更大的觉悟，\x01",
            "迎接更困难的挑战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#1382F#6P明白了……\x01",
            "您的话我们会铭记在心的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#724F#5P那么，我这就告辞了……\x02\x03",

            "当我消失之后，\x01",
            "下一条道路也会打开吧。\x02\x03",

            "希望你们能够顺利通过试炼，\x01",
            "平安回到现实世界……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_23(0x146)
    OP_22(0x138, 0x0, 0x64)

    def lambda_1C03():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1C03)
    PlayEffect(0x1, 0x1, 0x10, -100, -700, 0, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_1C5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C5B)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1661 end

    def Function_6_1C99(): pass

    label("Function_6_1C99")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CBA")
    Sleep(100)
    Jump("loc_1D35")

    label("loc_1CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CCF")
    Sleep(200)
    Jump("loc_1D35")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE4")
    Sleep(300)
    Jump("loc_1D35")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF9")
    Sleep(400)
    Jump("loc_1D35")

    label("loc_1CF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0E")
    Sleep(500)
    Jump("loc_1D35")

    label("loc_1D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D23")
    Sleep(600)
    Jump("loc_1D35")

    label("loc_1D23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D35")
    Sleep(700)

    label("loc_1D35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D57")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_1D35")

    label("loc_1D57")

    Return()

    # Function_6_1C99 end

    def Function_7_1D58(): pass

    label("Function_7_1D58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -830, -50, 18010, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB9")
    SetChrPos(0xEF, 570, 0, 17980, 0)
    SetChrPos(0xF0, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_1E3E")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DFD")
    SetChrPos(0xF0, 570, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF1, 690, 0, 16620, 0)
    Jump("loc_1E3E")

    label("loc_1DFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3E")
    SetChrPos(0xF1, 570, 0, 17980, 0)
    SetChrPos(0xEF, -1190, 0, 16379, 0)
    SetChrPos(0xF0, 690, 0, 16620, 0)

    label("loc_1E3E")

    OP_6D(990, -50, 18490, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x109,
        (
            "#1840F#6P哎呀……\x01",
            "真是不得了的人物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        "#1165F#11P是啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F18")

    def lambda_1EEE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EEE)
    Sleep(100)

    def lambda_1F01():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1F01)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_1F91")

    label("loc_1F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F56")

    def lambda_1F2C():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F2C)
    Sleep(100)

    def lambda_1F3F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1F3F)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    Jump("loc_1F91")

    label("loc_1F56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F91")

    def lambda_1F6A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F6A)
    Sleep(100)

    def lambda_1F7D():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1F7D)
    Sleep(100)
    OP_8C(0x109, 90, 400)

    label("loc_1F91")

    Sleep(500)

    ChrTalk(    #46
        0x105,
        (
            "#1160F#5P不过，这样一来\x01",
            "通往下个领域的道路应该已经打开了。\x02\x03",

            "我们暂且回到周游道\x01",
            "调查一下其它的石碑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2041")

    ChrTalk(    #47
        0x10F,
        "#1448F……说的没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2041")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_206F")

    ChrTalk(    #48
        0x101,
        "#1006F嗯，明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_206F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209D")

    ChrTalk(    #49
        0x102,
        "#1500F嗯，好吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_209D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C8")

    ChrTalk(    #50
        0x10B,
        "#210FＯＫ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_20C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FE")

    ChrTalk(    #51
        0x110,
        (
            "#260F是啊。\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_20FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_212B")

    ChrTalk(    #52
        0x107,
        "#560F是！\x02",
    )

    Jump("loc_2127")

    label("loc_2127")

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_212B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2156")

    ChrTalk(    #53
        0x10A,
        "#816F明白了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2156")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2188")

    ChrTalk(    #54
        0x103,
        "#1536F嗯，就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2188")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21BB")

    ChrTalk(    #55
        0x106,
        "#051F是啊，就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_21BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EA")

    ChrTalk(    #56
        0x108,
        "#070F啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_21EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2217")

    ChrTalk(    #57
        0x10E,
        "#170F我知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2217")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224E")

    ChrTalk(    #58
        0x104,
        (
            "#1545F呵……\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_224E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(    #59
        0x10D,
        (
            "#277F嗯……\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2284")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(    #60
        0x10C,
        (
            "#111F嗯……\x01",
            "就这么办吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B7")

    OP_A2(0x2B08)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22CB")
    OP_A2(0x263E)

    label("loc_22CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22DC")
    OP_A2(0x263F)

    label("loc_22DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22ED")
    OP_A2(0x2640)

    label("loc_22ED")

    OP_28(0x38, 0x4, 0x4)
    OP_28(0x38, 0x4, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_1D58 end

    SaveToFile()

Try(main)
