from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0100.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60029",
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
        '虫',                                   # 9
        '目标用照相机',                         # 10
        '洛连特方向',                           # 11
        '布莱特家方向',                         # 12
        '格鲁纳门方向',                         # 13
        '',                                     # 14
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


    AddCharChip(
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT26/CH20789 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT26/CH20789P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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

    DeclNpc(
        X                   = -14030,
        Z                   = 1000,
        Y                   = 217340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -60890,
        Z                   = 1030,
        Y                   = 216800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39320,
        Z                   = 1000,
        Y                   = 90280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -36800,
        TriggerZ            = 1000,
        TriggerY            = 152300,
        TriggerRange        = 1500,
        ActorX              = -36800,
        ActorZ              = 2500,
        ActorY              = 152800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39100,
        TriggerZ            = 1000,
        TriggerY            = 153300,
        TriggerRange        = 1500,
        ActorX              = -39100,
        ActorZ              = 2200,
        ActorY              = 153300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1C1",          # 01, 1
        "Function_2_1C2",          # 02, 2
        "Function_3_49F",          # 03, 3
        "Function_4_4D5",          # 04, 4
        "Function_5_543",          # 05, 5
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C0")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1C0")

    Return()

    # Function_0_1A2 end

    def Function_1_1C1(): pass

    label("Function_1_1C1")

    Return()

    # Function_1_1C1 end

    def Function_2_1C2(): pass

    label("Function_2_1C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, -42840, 2210, 171630, 315)
    ClearParty()
    AddParty(0x54, 0xEE, 0xFF)
    SetChrPos(0x155, -41130, 1010, 173360, 315)
    OP_6D(-53050, 1000, 176590, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(344000, 0)
    OP_6E(262, 0)

    def lambda_274():
        OP_6D(-48850, 1230, 182000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_274)

    def lambda_28C():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_28C)
    FadeToBright(4000, 0)
    Sleep(2000)

    def lambda_2AA():
        OP_8E(0xFE, 0xFFFF412E, 0x8A2, 0x2C358, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AA)
    WaitChrThread(0x10, 0x1)

    def lambda_2CA():
        OP_8E(0xFE, 0xFFFF27AC, 0xDAC, 0x2DF5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CA)
    Sleep(700)

    def lambda_2EA():
        OP_8E(0xFE, 0xFFFF412E, 0x3F2, 0x2C358, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_2EA)
    WaitChrThread(0x155, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x155,
        (
            "#296F啊啊，逃走了……\x02\x03",

            "那家伙的脸好有趣……\x02\x03",

            "#292F这点小事不算什么！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x3)
    OP_8C(0x155, 135, 500)
    Sleep(500)

    ChrTalk(    #1
        0x155,
        (
            "#295F约修亚现在不能行动。\x01",
            "而且看起来还那么难过……\x02\x03",

            "#290F嗯，果然还是\x01",
            "得靠我抓到虫子，\x01",
            "让他打起精神来！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0x3)
    OP_62(0x155, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x155, 225, 500)

    ChrTalk(    #2
        0x155,
        (
            "#293F啊，是刚才的那只！\x02\x03",

            "#294F等一下～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_45D():
        OP_6B(3460, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_45D)

    def lambda_46D():
        OP_8E(0xFE, 0xFFFF12F8, 0x3F2, 0x29522, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x155, 1, lambda_46D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C2 end

    def Function_3_49F(): pass

    label("Function_3_49F")

    OP_44(0x10, 0x1)
    SetChrPos(0x10, -43240, 3210, 190470, 225)

    def lambda_4BA():
        OP_8E(0xFE, 0xFFFF0BBE, 0x5E6, 0x29CB6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4BA)
    Sleep(4000)
    Return()

    # Function_3_49F end

    def Function_4_4D5(): pass

    label("Function_4_4D5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x05北　洛连特市　　　４９塞尔矩\x01",
            "南　格鲁纳门　　２５９塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_4D5 end

    def Function_5_543(): pass

    label("Function_5_543")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        "\x07\x05西　布莱特家\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_543 end

    SaveToFile()

Try(main)
