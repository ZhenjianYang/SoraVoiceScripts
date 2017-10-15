from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4310   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Lt. Colonel Cid',                      # 9
        'Warrant Officer Belc',                 # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
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
        'ED6_DT27/CH03590 ._CH',             # 00
        'ED6_DT07/CH01600 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT27/CH03590P._CP',             # 00
        'ED6_DT07/CH01600P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_162",          # 00, 0
        "Function_1_176",          # 01, 1
        "Function_2_177",          # 02, 2
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_175")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_175")

    Return()

    # Function_0_162 end

    def Function_1_176(): pass

    label("Function_1_176")

    Return()

    # Function_1_176 end

    def Function_2_177(): pass

    label("Function_2_177")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, -80, 250, 68550, 180)
    SetChrPos(0x9, -1060, 250, 69080, 180)
    SetChrPos(0xA, 700, 0, 66610, 0)
    SetChrPos(0xB, -700, 0, 66610, 0)
    OP_6D(-50, 250, 68390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xA,
        (
            "#2PSquads one and two are moving along the\x01",
            "western scenic route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "#2PThey should have the enemy surrounded\x01",
            "shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "#6PIn the eastern division, several Intelligence\x01",
            "Division units are fleeing to beyond Romal\x01",
            "Pond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        "#6PSquads three and four are in pursuit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#703FGood work.\x02\x03",

            "#700FProceed until both groups are neutralized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        "#2P#1KSir!\x02",
    )


    ChrTalk(    #6
        0xB,
        "#6P#1KSir!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_39C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_39C)
    Sleep(100)

    def lambda_3AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3AF)
    Sleep(500)

    def lambda_3C2():
        OP_6D(-50, 250, 65390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C2)

    def lambda_3DA():
        OP_8E(0xFE, 0x2BC, 0x0, 0xCDD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DA)
    Sleep(50)

    def lambda_3FA():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0xCDD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3FA)
    Sleep(3000)
    WaitChrThread(0x101, 0x1)

    def lambda_41F():
        OP_6D(-50, 250, 69390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41F)
    WaitChrThread(0x101, 0x1)

    def lambda_43C():
        OP_8C(0x9, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_43C)
    Sleep(400)

    ChrTalk(    #7
        0x9,
        (
            "#8PI must admit, sir...\x01",
            "I don't understand their thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "#8PDo you think this could be a diversion?\x02",
    )

    CloseMessageWindow()

    def lambda_4BF():
        OP_8C(0x8, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BF)
    Sleep(400)

    ChrTalk(    #9
        0x8,
        (
            "#703F#4PI've a full company stationed at Grancel Castle.\x02\x03",

            "Even if they box us in here, they won't shut\x01",
            "us down completely.\x02\x03",

            "#702FUnless... Does Amalthea have some ace\x01",
            "up her sleeve we don't know about...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#8PAn ace?\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 0, 0, 60000, 0)

    ChrTalk(    #11
        0xC,
        "#1PExcuse me, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_5EC():
        OP_6D(-50, 250, 68390, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EC)

    def lambda_604():
        OP_8C(0x9, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_604)
    Sleep(100)

    def lambda_617():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_617)
    OP_8E(0xC, 0x0, 0x0, 0x10432, 0xFA0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #12
        0x8,
        "#700FWhat is it, soldier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xC,
        "We've received word from headquarters.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "However, when we attempted to contact the\x01",
            "capital branch of the Bracer Guild...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "The phones returned a disconnection signal.\x01",
            "We could not raise them by any means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "#702FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        "Orders, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#700FHm.\x02\x03",

            "#703FI think it's best I call in a little\x01",
            "extra insurance.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #19
        0x8,
        (
            "#700F#4PBelc, you're in charge.\x02\x03",

            "I'll be in the transmitter room for a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #20
        0x9,
        "#8PYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#8PMay I ask who you are contacting?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#701F#4PA certain...someone at Leiston.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T4150   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_177 end

    SaveToFile()

Try(main)
