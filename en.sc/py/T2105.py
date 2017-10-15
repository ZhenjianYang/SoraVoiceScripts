from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2105   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Bleublanc',                            # 9
        'Lorence?',                             # 10
        'Deen',                                 # 11
        'Rais',                                 # 12
        'Rocco',                                # 13
        'Kevin',                                # 14
        'Gospel',                               # 15
        'Aurian Causeway',                      # 16
        'Ruan - North Block',                   # 17
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
        'ED6_DT27/CH03530 ._CH',             # 00
        'ED6_DT07/CH02040 ._CH',             # 01
        'ED6_DT27/CH04530 ._CH',             # 02
        'ED6_DT27/CH04540 ._CH',             # 03
        'ED6_DT07/CH02510 ._CH',             # 04
        'ED6_DT07/CH02520 ._CH',             # 05
        'ED6_DT07/CH02530 ._CH',             # 06
        'ED6_DT27/CH03080 ._CH',             # 07
        'ED6_DT27/CH04087 ._CH',             # 08
        'ED6_DT26/CH20243 ._CH',             # 09
        'ED6_DT26/CH20273 ._CH',             # 0A
        'ED6_DT26/CH20283 ._CH',             # 0B
        'ED6_DT26/CH20278 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT27/CH03530P._CP',             # 00
        'ED6_DT07/CH02040P._CP',             # 01
        'ED6_DT27/CH04530P._CP',             # 02
        'ED6_DT27/CH04540P._CP',             # 03
        'ED6_DT07/CH02510P._CP',             # 04
        'ED6_DT07/CH02520P._CP',             # 05
        'ED6_DT07/CH02530P._CP',             # 06
        'ED6_DT27/CH03080P._CP',             # 07
        'ED6_DT27/CH04087P._CP',             # 08
        'ED6_DT26/CH20243P._CP',             # 09
        'ED6_DT26/CH20273P._CP',             # 0A
        'ED6_DT26/CH20283P._CP',             # 0B
        'ED6_DT26/CH20278P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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


    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_272",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2C0",          # 02, 2
        "Function_3_16DB",         # 03, 3
        "Function_4_1764",         # 04, 4
        "Function_5_17F2",         # 05, 5
        "Function_6_1808",         # 06, 6
        "Function_7_180C",         # 07, 7
    )


    def Function_0_272(): pass

    label("Function_0_272")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Return()

    # Function_0_272 end

    def Function_1_280(): pass

    label("Function_1_280")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x0, 0x64)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    Return()

    # Function_1_280 end

    def Function_2_2C0(): pass

    label("Function_2_2C0")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, 23440, 7780, 1910, 0)
    SetChrPos(0x1, 23440, 7780, 1910, 0)
    SetChrPos(0x2, 23440, 7780, 1910, 0)
    SetChrPos(0x3, 23440, 7780, 1910, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 23460, 8800, 3630, 0)
    OP_6D(47110, 7780, 30010, 0)
    OP_67(0, 8050, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(31000, 0)
    OP_6E(505, 0)

    def lambda_37D():
        OP_6D(25710, 8800, 4920, 9000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37D)

    def lambda_395():
        OP_67(0, 14180, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_395)

    def lambda_3AD():
        OP_6C(142000, 9000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3AD)

    def lambda_3BD():
        OP_6E(241, 9000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BD)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(8000)
    OP_44(0x0, 0x1)
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    OP_44(0x1, 0x1)
    Fade(1000)
    OP_6D(24530, 6120, 8189, 0)
    OP_67(0, 6940, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(487, 0)
    OP_0D()
    SetChrPos(0x9, 31670, 7800, 110, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#231FAnd so the fete comes to an end, but the passion\x01",
            "it left in my heart still burns within me!\x02\x03",

            "Ah, my only solace is to wait in the\x01",
            "pale moonlight for the cool breeze\x01",
            "of the sea to still my heated blood...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x9,
        "Man's Voice",
        "#1P...Sorry to make you wait.\x02",
    )

    CloseMessageWindow()

    def lambda_559():
        OP_6D(28050, 7800, 2290, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_559)

    def lambda_571():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_571)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #2
        0x8,
        (
            "#231F#6PAhh! Perfect timing.\x02\x03",

            "You really are perfectly punctual,\x01",
            "my friend.\x02\x03",

            "It would not hurt you to learn to\x01",
            "be fashionably late, you know.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62A():

        label("loc_62A")

        TurnDirection(0x8, 0x9, 400)
        OP_48()
        Jump("loc_62A")

    QueueWorkItem2(0x8, 3, lambda_62A)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 1)
    OP_99(0x9, 0x1, 0x2, 0x5DC)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_65B():
        OP_6D(23740, 7800, 1150, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_65B)

    def lambda_673():
        OP_67(0, 7500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_673)

    def lambda_68B():
        OP_96(0x9, 0x5B5E, 0x1E78, 0xFFFFFDDA, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_68B)
    WaitChrThread(0x9, 0x1)
    OP_7D(0x1, 0x9, 0x0, 0x0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    TurnDirection(0x9, 0x8, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x3)

    ChrTalk(    #3
        0x9,
        (
            "#124FSorry, but 'punctual' is what I am.\x02\x03",

            "#120FNow. What is your report?\x02",
        )
    )

    CloseMessageWindow()
    OP_96(0x8, 0x5B90, 0x1E78, 0x8AC, 0x64, 0x1388)
    Sleep(500)

    ChrTalk(    #4
        0x8,
        (
            "#230F#6POh, let us not be boorish\x01",
            "and hurry so, yes?\x02\x03",

            "This has been a grand evening.\x01",
            "Allow me to savor it a little longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        (
            "#123FReally... I'll take that as a report\x01",
            "of 'I really like them,' then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#231F#6PLike? Hah! The lovely princess has\x01",
            "stolen even more of my heart. It's\x01",
            "a miracle I yet live, I tell you!\x02\x03",

            "What's more, I met a rival in the arena\x01",
            "of beauty and aesthetics. A rival! Me!\x02\x03",

            "#230FHahaha... I shall be QUITE busy\x01",
            "these next few weeks, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        (
            "#124FYou really are hopeless.\x02\x03",

            "#120FYou're welcome to pursue your 'hobbies,'\x01",
            "but do not let it interfere with the plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#230F#6PYou need not worry on\x01",
            "that score, my friend.\x02\x03",

            "On that note... Here, take it.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0x9, 0x3E8, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x8, 8)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 23740, 7500, 400, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 7)
    SetChrFlags(0xE, 0x80)
    OP_0D()
    OP_8F(0x8, 0x5B90, 0x1E78, 0x76C, 0x7D0, 0x0)

    ChrTalk(    #9
        0x9,
        (
            "#124FVery good.\x02\x03",

            "#120FSo. How DID your experiments go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#232F#6PYes... Call it a ninety-percent\x01",
            "success rate or so.\x02\x03",

            "The hologram projector can accurately\x01",
            "project for many hundreds of selge.\x02\x03",

            "The first two or so projections were\x01",
            "miserable failures, I'm afraid...\x02\x03",

            "After the third, however, the\x01",
            "device worked flawlessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#123FSo some cause for concern,\x01",
            "but not much. It does function.\x02\x03",

            "I'll report to the professor at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#230F#6PThat 'Gospel'...\x02\x03",

            "Truly, it is far beyond contemporary\x01",
            "technology, and I don't simply mean\x01",
            "its ability to negate orbments.\x02\x03",

            "I know it was made by the Thirteen Factories...\x01",
            "but how, exactly, does it work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#124FI'm not sure... I'm not privy to the details.\x02\x03",

            "#120FAccording to the professor,\x01",
            "these phenomena are just the\x01",
            "'tip of a miracle.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#233F#6POoooh, so it's the stuff of miracles, is it?\x02\x03",

            "#230FHm. Miracles are the providence\x01",
            "of She Who Dwells Above alone.\x02\x03",

            "What does he mean, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#123FRegardless, a few more experiments should\x01",
            "make the potential of the Gospels clear.\x02\x03",

            "With that...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_EA7():
        OP_8C(0x9, 250, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EA7)
    WaitChrThread(0x9, 0x1)
    Fade(1000)
    OP_6D(22960, 7800, 30, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(1870, 0)
    OP_6C(306000, 0)
    OP_6E(487, 0)
    OP_0D()

    ChrTalk(    #16
        0x9,
        "#121F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#233FHm?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 250, 400)
    Sleep(500)

    ChrTalk(    #18
        0x8,
        (
            "#231FOho, we've had a number of unexpected\x01",
            "actors coming onto the stage this night.\x02\x03",

            "How shall this cameo end, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "#124F#6PHeh...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrFlags(0x9, 0x800)
    SetChrChipByIndex(0x9, 3)
    SetChrSubChip(0x9, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x9,
        "#123F#6PThat's up to how our hidden mouse responds.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#231FHah, indeed.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 2)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x8,
        "#231FCome now, mouse! Cry for us!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 29570, 0, 20890, 180)
    SetChrPos(0xB, 30570, 0, 21930, 180)
    SetChrPos(0xC, 28570, 0, 21930, 180)

    NpcTalk(    #23
        0xA,
        "Drunken Voice",
        "#1P#1S...Waheeeeeey...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_10FF():
        OP_6D(23740, 7800, 2150, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_10FF)

    def lambda_1117():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1117)

    def lambda_112F():
        OP_6C(35000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_112F)
    OP_8C(0x9, 0, 400)
    Sleep(200)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    WaitChrThread(0xA, 0x0)

    ChrTalk(    #24
        0x8,
        "#230F#6PHm...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x8, 250, 400)
    Sleep(300)

    ChrTalk(    #25
        0x8,
        (
            "#231F#6PI'm not sure who that little mouse is,\x01",
            "but your life is spared, it seems.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(300)
    OP_8C(0x9, 250, 400)

    ChrTalk(    #26
        0x9,
        "#121F#2PThank Aidios for your life, rodent.\x02",
    )

    CloseMessageWindow()

    def lambda_124D():
        OP_6D(23020, 7800, -6000, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_124D)

    def lambda_1265():
        OP_6C(75000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1265)
    Sleep(500)
    OP_43(0x9, 0x0, 0x0, 0x3)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x9, 0x0)
    OP_43(0x8, 0x0, 0x0, 0x4)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x2)
    Sleep(500)

    def lambda_12A3():
        OP_6D(29380, 0, 7350, 5000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_12A3)

    def lambda_12BB():
        OP_6C(108000, 5000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12BB)

    def lambda_12CB():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_12CB)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_12F2():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12F2)
    Sleep(50)

    def lambda_1312():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC950, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1312)
    Sleep(50)
    OP_90(0xC, 0x0, 0x0, 0xFFFFC75C, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x2)
    OP_8C(0xB, 46, 400)
    Sleep(500)

    ChrTalk(    #27
        0xB,
        "#1751F#6PBwahaha! Bring on th'beer!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 135, 400)
    Sleep(500)

    ChrTalk(    #28
        0xA,
        "#1745FUrp... Can't drink no mo'...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 300, 400)
    Sleep(500)

    ChrTalk(    #29
        0xC,
        "#1764FDamn it... I coulda... I coulda...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_13F3():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_13F3)
    OP_8C(0xA, 90, 400)

    def lambda_1415():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1415)
    OP_8C(0xC, 90, 400)

    def lambda_1437():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1437)
    Sleep(1000)
    SetChrPos(0xD, 9100, 0, 1600, 268)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 8)
    SetChrSubChip(0xD, 1)

    def lambda_147C():
        OP_6D(9700, 0, 1630, 4000)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_147C)

    def lambda_1494():
        OP_67(0, 8000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1494)

    def lambda_14AC():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_14AC)
    WaitChrThread(0xD, 0x0)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xD, 0x2)
    Sleep(500)

    ChrTalk(    #30
        0xD,
        (
            "#1068F#6POooooh-ho-hooooo-kaaaaaaaaaay...\x01",
            "Thank you, Aidios, saints, and anyone else\x01",
            "I'm forgetting for saving your humble servant!\x02\x03",

            "#1067FHeh... Like I need to be told to\x01",
            "give praise to the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0xD, 0x1, 0x9, 0x5DC)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)

    def lambda_15BF():
        OP_6D(10100, 0, 2440, 3500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_15BF)

    def lambda_15D7():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15D7)
    OP_8C(0xD, 0, 400)
    SetChrFlags(0xD, 0x4)
    OP_8E(0xD, 0x23FA, 0x0, 0x9C4, 0x3E8, 0x0)
    OP_8E(0xD, 0x297C, 0x0, 0xB54, 0x3E8, 0x0)
    WaitChrThread(0xD, 0x0)
    WaitChrThread(0xD, 0x2)

    ChrTalk(    #31
        0xD,
        (
            "#1063F#6P...What monsters, though.\x02\x03",

            "#1065FSo those are the Enforcers\x01",
            "of Ouroboros, huh...?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400A5, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_A2(0x1400)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2C0 end

    def Function_3_16DB(): pass

    label("Function_3_16DB")

    OP_8C(0x9, 180, 400)
    OP_8E(0x9, 0x5B04, 0x1E78, 0xFFFFF722, 0x1770, 0x0)
    SetChrChipByIndex(0x9, 9)
    SetChrSubChip(0x9, 1)
    OP_96(0x9, 0x5BAE, 0x2260, 0xFFFFF0B0, 0x3E8, 0x1770)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x9, 0x32, 0x1F4)
    SetChrSubChip(0x9, 2)

    def lambda_172F():
        OP_96(0x9, 0x5A14, 0x1F40, 0xFFFFCD38, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_172F)
    Sleep(200)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1757():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1757)
    Return()

    # Function_3_16DB end

    def Function_4_1764(): pass

    label("Function_4_1764")

    OP_8E(0x8, 0x5B04, 0x1E78, 0xFFFFF722, 0x1770, 0x0)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    OP_96(0x8, 0x5BAE, 0x2260, 0xFFFFF0B0, 0x3E8, 0x1770)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x8, 0x32, 0x1F4)

    def lambda_17AC():
        OP_96(0x8, 0x5A14, 0x1F40, 0xFFFFCD38, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17AC)
    OP_43(0x8, 0x3, 0x0, 0x5)
    Sleep(200)
    OP_22(0x99, 0x0, 0x64)

    def lambda_17DB():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_17DB)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    Return()

    # Function_4_1764 end

    def Function_5_17F2(): pass

    label("Function_5_17F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1807")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_5_17F2")

    label("loc_1807")

    Return()

    # Function_5_17F2 end

    def Function_6_1808(): pass

    label("Function_6_1808")

    SetPlaceName(0x69)
    Return()

    # Function_6_1808 end

    def Function_7_180C(): pass

    label("Function_7_180C")

    SetPlaceName(0x52)
    Return()

    # Function_7_180C end

    SaveToFile()

Try(main)
