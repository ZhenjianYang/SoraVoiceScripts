from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2131   ._SN',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Lechter',                              # 9
        'Spiridon',                             # 10
        'Primo',                                # 11
        'Target Camera',                        # 12
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
        'ED6_DT26/CH20777 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT26/CH20777P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 26000,
        Z                   = 0,
        Y                   = 27230,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5500,
        Z                   = 300,
        Y                   = 33800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
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


    DeclActor(
        TriggerX            = 28730,
        TriggerZ            = 0,
        TriggerY            = 37220,
        TriggerRange        = 800,
        ActorX              = 28730,
        ActorZ              = 1800,
        ActorY              = 37220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_166",          # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1A9",          # 02, 2
        "Function_3_8AB",          # 03, 3
        "Function_4_8DE",          # 04, 4
        "Function_5_E8E",          # 05, 5
    )


    def Function_0_166(): pass

    label("Function_0_166")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_188")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_19B")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_19B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_19B")

    Return()

    # Function_0_166 end

    def Function_1_19C(): pass

    label("Function_1_19C")

    OP_71(0x803, 0x0)
    ExitThread()
    OP_71(0x2003, 0x0)
    ExitThread()
    Return()

    # Function_1_19C end

    def Function_2_1A9(): pass

    label("Function_2_1A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-720, 250, 31660, 0)
    OP_67(0, 4059, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(322000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 27080, 500, 36860, 0)
    SetChrPos(0x105, 0, -500, 24500, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_23E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_23E)

    def lambda_250():
        OP_8E(0xFE, 0x0, 0xFA, 0x7850, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_250)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_8C(0x105, 90, 600)
    Sleep(500)
    OP_8C(0x105, 280, 600)
    Sleep(1000)

    def lambda_28D():
        OP_6D(4120, 750, 31660, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_28D)

    def lambda_2A5():
        OP_8E(0xFE, 0x1AF4, 0xFA, 0x7850, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A5)
    WaitChrThread(0x105, 0x1)

    def lambda_2C5():
        OP_8E(0xFE, 0x1AF4, 0x7D0, 0x9088, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C5)
    WaitChrThread(0x105, 0x1)

    def lambda_2E5():
        OP_8E(0xFE, 0x1194, 0xDAC, 0x9088, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E5)
    Sleep(600)
    Fade(1000)
    OP_6D(32759, -2000, 37520, 0)
    OP_67(0, 8080, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x105, 0xFF)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, 35500, -3250, 34500, 0)
    Sleep(1000)

    def lambda_36C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_36C)

    def lambda_37E():
        OP_8E(0xFE, 0x8AAC, 0xFFFFF830, 0x9150, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37E)
    WaitChrThread(0x105, 0x1)

    def lambda_39E():
        OP_8E(0xFE, 0x7BE8, 0x0, 0x9150, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_39E)
    WaitChrThread(0x105, 0x1)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3DA():
        OP_6D(26740, 0, 37440, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3DA)

    def lambda_3F2():
        OP_67(0, 5480, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3F2)

    def lambda_40A():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_40A)
    OP_62(0x10, 0x96, 1850, 0x8, 0x9, 0xC8, 0x0)
    WaitChrThread(0x13, 0x0)
    Sleep(1000)

    def lambda_436():
        OP_8E(0xFE, 0x7788, 0x0, 0x8DCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_436)
    WaitChrThread(0x105, 0x1)

    def lambda_456():
        OP_8E(0xFE, 0x6F54, 0x0, 0x8DCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_456)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 315, 400)
    Sleep(300)

    ChrTalk(    #0
        0x105,
        (
            "#047F#12PLechter.\x02\x03",

            "#046FWhat are you doing here?!\x02\x03",

            "We're students! Gambling is expressly forbidden!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#1772FI know.\x02\x03",

            "#1778FI mean, I'm the Student Council president!\x01",
            "Of course I know!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10)
    Sleep(300)
    OP_22(0x104, 0x0, 0x64)
    Sleep(300)
    OP_22(0x104, 0x0, 0x64)
    Sleep(300)
    OP_22(0x104, 0x0, 0x64)
    Sleep(500)
    OP_22(0x105, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x10, 0x96, 1850, 0xA, 0xB, 0xC8, 0x2)
    Sleep(1000)

    ChrTalk(    #2
        0x10,
        "#1771FYes! Come to Papa!\x02",
    )

    CloseMessageWindow()
    OP_22(0x108, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10, 0x96, 1850, 0x8, 0x9, 0xC8, 0x0)
    Sleep(1000)

    ChrTalk(    #3
        0x105,
        (
            "#047F#12P...\x02\x03",

            "#043F(I find myself doubting how he could be more\x01",
            "by the minute...)\x02\x03",

            "(Maybe I should ask the dean next time I see\x01",
            "him so I can make sure this isn't some kind of\x01",
            "elaborate ruse...)\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x3)
    Sleep(2000)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x105, 270, 500)
    Sleep(300)

    ChrTalk(    #4
        0x105,
        (
            "#044F(That sounds like the bridge coming down.)\x02\x03",

            "#047F(Finally! I can go visit the mayor now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 500)
    Sleep(500)

    ChrTalk(    #5
        0x105,
        (
            "#042F#12PI'll be leaving now. I need to go and take\x01",
            "care of your work for you.\x02\x03",

            "You stay right where you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#1773FRight...\x02\x03",

            "#1776FHmm... Right...\x02\x03",

            "Just a liiittle bit more...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        (
            "#042F#12PAre you even paying attention?!\x02\x03",

            "#047FJust stay here! Please!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 500)

    def lambda_841():
        OP_8E(0xFE, 0x7788, 0x0, 0x8DCC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_841)
    WaitChrThread(0x105, 0x1)

    def lambda_861():
        OP_8E(0xFE, 0x7BE8, 0x0, 0x9150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_861)
    WaitChrThread(0x105, 0x1)

    def lambda_881():
        OP_8E(0xFE, 0x8AAC, 0xFFFFF830, 0x9150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_881)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1A9 end

    def Function_3_8AB(): pass

    label("Function_3_8AB")

    OP_22(0x94, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x94, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x94, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x94, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x94, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_3_8AB end

    def Function_4_8DE(): pass

    label("Function_4_8DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(28260, 0, 38200, 0)
    OP_67(0, 6520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 26300, 250, 37100, 45)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, 35500, -3250, 34500, 0)
    FadeToBright(1000, 0)

    def lambda_968():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_968)

    def lambda_97A():
        OP_8E(0xFE, 0x8AAC, 0xFFFFF830, 0x9150, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_97A)
    WaitChrThread(0x105, 0x1)

    def lambda_99A():
        OP_8E(0xFE, 0x7BE8, 0x0, 0x9150, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_99A)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x105,
        "#042F#12P(I knew it!)\x02",
    )

    CloseMessageWindow()

    def lambda_9F6():
        OP_6D(26260, 0, 38200, 1800)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_9F6)

    def lambda_A0E():
        OP_67(0, 5520, -10000, 1800)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_A0E)

    def lambda_A26():
        OP_6B(2900, 1800)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A26)

    def lambda_A36():
        OP_8E(0xFE, 0x7850, 0x0, 0x8EF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A36)
    WaitChrThread(0x105, 0x1)

    def lambda_A56():
        OP_8E(0xFE, 0x6FB8, 0x0, 0x8EF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A56)
    WaitChrThread(0x105, 0x1)
    Sleep(300)

    ChrTalk(    #9
        0x105,
        (
            "#045F#12PUmm... Excuse me...\x02\x03",

            "You wouldn't happen to know where the\x01",
            "student who was sitting here has gone,\x01",
            "would you?\x02\x03",

            "I'm trying to find him.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 500)
    Sleep(300)

    ChrTalk(    #10
        0x11,
        "#5PAh, you must mean Master Lechter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x105,
        "#044F#12P('Master' Lechter?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "#5PA young lady came to collect him not long ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#5PShe did punch him before they departed,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x105,
        (
            "#045F#12P(Thank Aidios for Lucy.)\x02\x03",

            "#043FI'm so sorry for the trouble he's caused you.\x02\x03",

            "On behalf of the students of the academy,\x01",
            "I hope you won't think ill of us for the actions\x01",
            "of one of our students...\x02\x03",

            "#047FOur Student Council president, no less. I really\x01",
            "do apologize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#5POh, on the contrary! Master Lechter is a valued\x01",
            "customer of ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5PIncidentally, should you happen to have the\x01",
            "chance to speak to him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "#5P...we've placed the coins from the game he was\x01",
            "in the middle of in his pool as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#5PIf you could let him know that, it would be \x01",
            "greatly appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x105,
        "#542F#12PA-All right, then...\x02",
    )

    CloseMessageWindow()

    def lambda_E6C():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_E6C)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_8DE end

    def Function_5_E8E(): pass

    label("Function_5_E8E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x05Thrills and excitement await!\x01",
            "--Lavantar Casino & Bar\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_E8E end

    SaveToFile()

Try(main)
