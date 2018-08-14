from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3102   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3102.x',
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
        '警备艇',                               # 9
        '警备艇的影子',                         # 10
        '探照灯用',                             # 11
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9240,
        TriggerZ            = 0,
        TriggerY            = 18600,
        TriggerRange        = 1000,
        ActorX              = 9430,
        ActorZ              = 1000,
        ActorY              = 18590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1450,
        TriggerZ            = 0,
        TriggerY            = 45310,
        TriggerRange        = 1000,
        ActorX              = -1450,
        ActorZ              = 1000,
        ActorY              = 45510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_152",          # 00, 0
        "Function_1_17E",          # 01, 1
        "Function_2_1B1",          # 02, 2
        "Function_3_2D7",          # 03, 3
        "Function_4_3FD",          # 04, 4
        "Function_5_152D",         # 05, 5
        "Function_6_189E",         # 06, 6
        "Function_7_18EC",         # 07, 7
        "Function_8_1B0F",         # 08, 8
        "Function_9_1D1A",         # 09, 9
        "Function_10_1E98",        # 0A, 10
        "Function_11_214E",        # 0B, 11
        "Function_12_2408",        # 0C, 12
    )


    def Function_0_152(): pass

    label("Function_0_152")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_168")
    Jump("loc_17D")

    label("loc_168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_17D")

    Return()

    # Function_0_152 end

    def Function_1_17E(): pass

    label("Function_1_17E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190")
    OP_6F(0x11, 0)
    Jump("loc_197")

    label("loc_190")

    OP_6F(0x11, 60)

    label("loc_197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9")
    OP_6F(0x12, 0)
    Jump("loc_1B0")

    label("loc_1A9")

    OP_6F(0x12, 60)

    label("loc_1B0")

    Return()

    # Function_1_17E end

    def Function_2_1B1(): pass

    label("Function_2_1B1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_296")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x11, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x148, 1)"), scpexpr(EXPR_END)), "loc_225")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x48\x01\x07\x00。\x02",
    )

    Jump("loc_20A")

    label("loc_20A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFD)
    Jump("loc_293")

    label("loc_225")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x48\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x48\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_274")

    label("loc_274")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x11, 60)
    OP_70(0x11, 0x0)

    label("loc_293")

    Jump("loc_2C9")

    label("loc_296")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2C9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1B1 end

    def Function_3_2D7(): pass

    label("Function_3_2D7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x57F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x12, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x149, 1)"), scpexpr(EXPR_END)), "loc_34B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x49\x01\x07\x00。\x02",
    )

    Jump("loc_330")

    label("loc_330")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BFE)
    Jump("loc_3B9")

    label("loc_34B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x49\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x49\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_39A")

    label("loc_39A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x12, 60)
    OP_70(0x12, 0x0)

    label("loc_3B9")

    Jump("loc_3EF")

    label("loc_3BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2D7 end

    def Function_4_3FD(): pass

    label("Function_4_3FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp078_00.eff")
    LoadEffect(0x1, "map\\mp003_00.eff")
    LoadEffect(0x2, "map\\mp280_00.eff")
    LoadEffect(0x3, "map\\mp301_00.eff")
    OP_E0(238, 0x40, 0x2)
    OP_E0(238, 0x41, 0x3)
    OP_E0(238, 0x42, 0x4)
    OP_E0(239, 0x43, 0x2)
    OP_E0(239, 0x44, 0x3)
    OP_E0(239, 0x45, 0x4)
    OP_E0(240, 0x46, 0x2)
    OP_E0(240, 0x47, 0x3)
    OP_E0(240, 0x48, 0x4)
    OP_E0(241, 0x49, 0x2)
    OP_E0(241, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 98690, 30000, 32540, 60)
    OP_A1(0x10, 0x0)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x3E8)
    PlayEffect(0x3, 0x6, 0xFF, 96000, 30000, 31000, 50, -70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2390, 100, 22000, 90)
    OP_A1(0x11, 0x10)
    OP_71(0x410, 0x0)
    ExitThread()
    SetChrPos(0x109, -18450, 0, 20650, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    SetChrPos(0xEF, -18850, 0, 22010, 90)
    SetChrPos(0xF0, -20210, 0, 20210, 90)
    SetChrPos(0xF1, -20500, 0, 21990, 90)
    Jump("loc_5F4")

    label("loc_56F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3")
    SetChrPos(0xF0, -18850, 0, 22010, 90)
    SetChrPos(0xEF, -20210, 0, 20210, 90)
    SetChrPos(0xF1, -20500, 0, 21990, 90)
    Jump("loc_5F4")

    label("loc_5B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F4")
    SetChrPos(0xF1, -18850, 0, 22010, 90)
    SetChrPos(0xEF, -20210, 0, 20210, 90)
    SetChrPos(0xF0, -20500, 0, 21990, 90)

    label("loc_5F4")

    StopSound(0x9470, 0x30D40, 0x0)
    OP_6D(5310, 0, 22200, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(6180, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)

    def lambda_644():
        OP_6D(-5220, 0, 23370, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_644)

    def lambda_65C():
        OP_8F(0xFE, 0xFFFFE4BC, 0x0, 0x4F42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_65C)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2")

    def lambda_68A():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_68A)
    Sleep(100)

    def lambda_6AA():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6AA)
    Sleep(100)

    def lambda_6CA():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6CA)
    Jump("loc_7B7")

    label("loc_6E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")

    def lambda_6F6():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6F6)
    Sleep(100)

    def lambda_716():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_716)
    Sleep(100)

    def lambda_736():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_736)
    Jump("loc_7B7")

    label("loc_74E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B7")

    def lambda_762():
        OP_8F(0xFE, 0xFFFFE516, 0x0, 0x5564, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_762)
    Sleep(100)

    def lambda_782():
        OP_8F(0xFE, 0xFFFFDE40, 0x0, 0x4DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_782)
    Sleep(100)

    def lambda_7A2():
        OP_8F(0xFE, 0xFFFFDDD2, 0x0, 0x54BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_7A2)

    label("loc_7B7")

    FadeToBright(2000, 0)
    WaitChrThread(0xEE, 0x3)
    Fade(500)
    StopSound(0x9470, 0x1FBD0, 0x0)
    ClearMapFlags(0x10)
    OP_6D(-6500, 0, 22060, 0)
    OP_67(0, 6910, -10000, 0)
    OP_6B(3390, 0)
    OP_6C(45000, 0)
    OP_6E(220, 0)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x10C,
        "#112F#5P嗯……？\x02",
    )

    CloseMessageWindow()
    OP_22(0x79, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C2")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_929")

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_929")

    label("loc_8EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_929")

    label("loc_912")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_929")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_956")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9BD")

    label("loc_956")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9BD")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A6")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9BD")

    label("loc_9A6")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9BD")

    Sleep(1000)
    Jump("loc_C34")

    label("loc_9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FB")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A62")

    label("loc_9FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A23")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A62")

    label("loc_A23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A62")

    label("loc_A4B")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A62")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AF6")

    label("loc_A8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AF6")

    label("loc_AB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AF6")

    label("loc_ADF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AF6")

    Sleep(1000)
    Jump("loc_C34")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B34")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B9B")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B5C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B9B")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B9B")

    label("loc_B84")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B9B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC8")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C2F")

    label("loc_BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C2F")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C18")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_C2F")

    label("loc_C18")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_C2F")

    Sleep(1000)

    label("loc_C34")


    ChrTalk(    #7
        0x109,
        "#1079F#6P不、不会吧……\x02",
    )

    CloseMessageWindow()
    OP_22(0x64, 0x0, 0x64)
    SetChrPos(0x12, -8000, 0, 21000, 90)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x12, 0x80)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_22(0x35A, 0x1, 0x64)
    Sleep(500)

    ChrTalk(    #8
        0x10C,
        "#114F#5P#3S快撤退……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D06():
        OP_6D(-7100, 0, 22060, 500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_D06)

    def lambda_D1E():
        OP_67(0, 6070, -10000, 500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_D1E)

    def lambda_D36():
        OP_6B(3100, 500)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_D36)

    def lambda_D46():
        OP_6E(243, 500)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_D46)
    OP_22(0x235, 0x0, 0x64)
    Sleep(70)
    OP_43(0xEE, 0x0, 0x0, 0x6)
    OP_43(0xEF, 0x0, 0x0, 0x7)
    Sleep(30)
    OP_43(0x10, 0x0, 0x0, 0x8)
    OP_43(0x10, 0x1, 0x0, 0x9)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xEE, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x35A)

    def lambda_D9C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_D9C)
    Sleep(100)

    def lambda_DAF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DAF)
    Sleep(100)

    def lambda_DC2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_DC2)
    Sleep(100)
    OP_8C(0xF1, 90, 400)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    OP_6D(95240, 30000, 29870, 0)
    OP_67(0, -9470, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(45000, 0)
    OP_6E(659, 0)
    OP_72(0x400, 0x0)
    ExitThread()

    def lambda_E2E():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_E2E)
    OP_22(0x35A, 0x1, 0x64)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x3AD)
    OP_73(0x0)
    OP_23(0x35A)
    OP_6F(0x0, 940)
    OP_70(0x0, 0x385)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 701)
    OP_70(0x0, 0x384)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC7")
    SetMessageWindowPos(200, 400, -1, -1)
    SetChrName("莉丝")

    AnonymousTalk(    #9
        "\x07\x00#1802F啊……\x02",
    )

    Jump("loc_EC1")

    label("loc_EC1")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_F0A")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0A")
    SetMessageWindowPos(200, 400, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #10
        "\x07\x00#1164F啊……\x02",
    )

    Jump("loc_F07")

    label("loc_F07")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F55")
    SetMessageWindowPos(230, 400, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #11
        "\x07\x00#1020F什……\x02",
    )

    Jump("loc_F4F")

    label("loc_F4F")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_F97")

    label("loc_F55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F97")
    SetMessageWindowPos(230, 400, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #12
        "\x07\x00#216F什……\x02",
    )

    Jump("loc_F94")

    label("loc_F94")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDD")
    SetMessageWindowPos(180, 400, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #13
        "\x07\x00#1506F呜……\x02",
    )

    Jump("loc_FD7")

    label("loc_FD7")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1025")

    label("loc_FDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1025")
    SetMessageWindowPos(180, 400, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #14
        "\x07\x00#1524F呜……\x02",
    )

    Jump("loc_1022")

    label("loc_1022")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1025")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1064")
    SetMessageWindowPos(190, 400, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #15
        "\x07\x00#065F哇哇……\x02",
    )

    Jump("loc_1061")

    label("loc_1061")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1064")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AE")
    SetMessageWindowPos(220, 400, -1, -1)
    SetChrName("亚妮拉丝")

    AnonymousTalk(    #16
        "\x07\x00#1317F呜哇……\x02",
    )

    Jump("loc_10AB")

    label("loc_10AB")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_10AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F3")
    SetMessageWindowPos(250, 400, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #17
        "\x07\x00#057F嘁……\x02",
    )

    Jump("loc_10ED")

    label("loc_10ED")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1130")

    label("loc_10F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1130")
    SetMessageWindowPos(250, 400, -1, -1)
    SetChrName("穆拉")

    AnonymousTalk(    #18
        "\x07\x00#271F嘁……\x02",
    )

    Jump("loc_112D")

    label("loc_112D")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117A")
    SetMessageWindowPos(210, 400, -1, -1)
    SetChrName("尤莉亚　　　　　　　")

    AnonymousTalk(    #19
        "\x07\x00#177F呜……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_11B2")

    label("loc_117A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B2")
    SetMessageWindowPos(210, 400, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #20
        "\x07\x00#077F唔……\x02",
    )

    Jump("loc_11AF")

    label("loc_11AF")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_11B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FC")
    SetMessageWindowPos(170, 400, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #21
        "\x07\x00#1542F唔唔……\x02",
    )

    Jump("loc_11F9")

    label("loc_11F9")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_11FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1235")
    SetMessageWindowPos(240, 400, -1, -1)
    SetChrName("玲")

    AnonymousTalk(    #22
        "\x07\x00#1305F哼……\x02",
    )

    Jump("loc_1232")

    label("loc_1232")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1235")

    Sleep(300)
    Fade(500)
    OP_6D(-4720, 0, 22090, 0)
    OP_67(0, 5670, -10000, 0)
    OP_6B(4059, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x410, 0x0)
    ExitThread()
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x109,
        (
            "#1069F#5P呜……\x01",
            "这真是太没道理了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10C,
        (
            "#117F#5P这可是就算认真应战\x01",
            "也没办法战胜的对手啊！\x02\x03",

            "大家别勉强了，先撤退吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_131C():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_131C)
    Sleep(100)

    def lambda_132F():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_132F)
    Sleep(100)

    def lambda_1342():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1342)
    Sleep(100)

    def lambda_1355():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1355)
    Sleep(100)
    OP_22(0x35A, 0x1, 0x64)

    def lambda_136D():
        OP_6D(-14870, 2300, 20910, 4500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_136D)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EB")

    def lambda_1393():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1393)
    Sleep(100)

    def lambda_13B3():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_13B3)
    Sleep(100)

    def lambda_13D3():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_13D3)
    Jump("loc_14C0")

    label("loc_13EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1457")

    def lambda_13FF():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_13FF)
    Sleep(100)

    def lambda_141F():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_141F)
    Sleep(100)

    def lambda_143F():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_143F)
    Jump("loc_14C0")

    label("loc_1457")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14C0")

    def lambda_146B():
        OP_8F(0xFE, 0xFFFF8A8A, 0x190, 0x5D48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_146B)
    Sleep(100)

    def lambda_148B():
        OP_8F(0xFE, 0xFFFF8C38, 0x190, 0x56D6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_148B)
    Sleep(100)

    def lambda_14AB():
        OP_8F(0xFE, 0xFFFF925A, 0x190, 0x5CE4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_14AB)

    label("loc_14C0")


    def lambda_14C6():
        OP_8F(0xFE, 0xFFFF934A, 0x190, 0x5708, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14C6)
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x5)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xC)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x10, 0x1, 0x0, 0xB)
    OP_23(0x35A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x10)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M3101   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_4_3FD end

    def Function_5_152D(): pass

    label("Function_5_152D")


    def lambda_1533():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1533)

    def lambda_154E():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_154E)
    Sleep(300)

    def lambda_156E():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_156E)

    def lambda_1589():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1589)
    Sleep(300)

    def lambda_15A9():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_15A9)

    def lambda_15C4():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_15C4)
    Sleep(300)

    def lambda_15E4():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_15E4)

    def lambda_15FF():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_15FF)
    Sleep(200)

    def lambda_161F():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_161F)

    def lambda_163A():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_163A)
    Sleep(200)

    def lambda_165A():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_165A)

    def lambda_1675():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1675)
    Sleep(200)

    def lambda_1695():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1695)

    def lambda_16B0():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_16B0)
    Sleep(100)

    def lambda_16D0():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_16D0)

    def lambda_16EB():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_16EB)
    Sleep(100)

    def lambda_170B():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_170B)

    def lambda_1726():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1726)
    Sleep(100)

    def lambda_1746():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1746)

    def lambda_1761():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1761)
    Sleep(100)

    def lambda_1781():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1781)

    def lambda_179C():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_179C)
    Sleep(100)

    def lambda_17BC():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_17BC)

    def lambda_17D7():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_17D7)
    Sleep(100)

    def lambda_17F7():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_17F7)

    def lambda_1812():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1812)
    Sleep(100)

    def lambda_1832():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1832)

    def lambda_184D():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_184D)
    Sleep(100)

    def lambda_186D():
        OP_8F(0xFE, 0xFFFF7748, 0x0, 0x5208, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_186D)

    def lambda_1888():
        OP_8F(0xFE, 0xFFFF8AD0, 0x64, 0x55F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_1888)
    Return()

    # Function_5_152D end

    def Function_6_189E(): pass

    label("Function_6_189E")

    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 2)
    SetChrSubChip(0xEE, 0)
    OP_8C(0xFE, 45, 0)

    def lambda_18BA():
        OP_96(0xFE, 0xFFFFE1E2, 0x0, 0x4876, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18BA)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 0)
    SetChrSubChip(0xEE, 0)
    Return()

    # Function_6_189E end

    def Function_7_18EC(): pass

    label("Function_7_18EC")

    SetChrChipByIndex(0xEF, 5)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 8)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 11)
    SetChrSubChip(0xF1, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A3")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 135, 0)

    def lambda_192A():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_192A)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 45, 0)

    def lambda_1959():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1959)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_1988():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1988)
    Jump("loc_1AD2")

    label("loc_19A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3C")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 135, 0)

    def lambda_19C3():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_19C3)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 45, 0)

    def lambda_19F2():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_19F2)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_1A21():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1A21)
    Jump("loc_1AD2")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD2")
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF1, 135, 0)

    def lambda_1A5C():
        OP_96(0xFE, 0xFFFFE264, 0x0, 0x5A82, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1A5C)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xEF, 45, 0)

    def lambda_1A8B():
        OP_96(0xFE, 0xFFFFD9B8, 0x0, 0x47CC, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A8B)
    Sleep(30)
    OP_22(0xA3, 0x0, 0x64)
    OP_8C(0xF0, 135, 0)

    def lambda_1ABA():
        OP_96(0xFE, 0xFFFFD97C, 0x0, 0x5938, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1ABA)

    label("loc_1AD2")

    WaitChrThread(0xEF, 0x1)
    WaitChrThread(0xF0, 0x1)
    WaitChrThread(0xF1, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 3)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 6)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 9)
    SetChrSubChip(0xF1, 0)
    Return()

    # Function_7_18EC end

    def Function_8_1B0F(): pass

    label("Function_8_1B0F")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -4300, 0, 19850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1B4F():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1B4F)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -6300, 0, 19650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BA6():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BA6)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 19450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BFD():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BFD)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 19250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1C54():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C54)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 19050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1CAB():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1CAB)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 18850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1D02():
        OP_7C(0x64, 0x0, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D02)
    Sleep(100)
    Return()

    # Function_8_1B0F end

    def Function_9_1D1A(): pass

    label("Function_9_1D1A")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -4300, 0, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -6300, 0, 21150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 20950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 20750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 20550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_23(0x235)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 20350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_9_1D1A end

    def Function_10_1E98(): pass

    label("Function_10_1E98")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -16300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -18300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -20300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -22300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -24300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -26300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -28300, 0, 19000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Return()

    # Function_10_1E98 end

    def Function_11_214E(): pass

    label("Function_11_214E")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -8300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -10300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -12300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -14300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -16300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -18300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -20300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -22300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -24300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -26300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, -28300, 0, 22000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_44(0x10, 0x3)
    Return()

    # Function_11_214E end

    def Function_12_2408(): pass

    label("Function_12_2408")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_243B")
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    OP_22(0x235, 0x0, 0x64)
    Sleep(1500)
    OP_23(0x235)
    Jump("Function_12_2408")

    label("loc_243B")

    Return()

    # Function_12_2408 end

    SaveToFile()

Try(main)
