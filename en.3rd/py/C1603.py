from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1603   ._SN',
        MapName             = 'Bose',
        Location            = 'C1603.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Agate',                                # 9
        'Target Camera',                        # 10
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
        'ED6_DT06/CH20053 ._CH',             # 00
        'ED6_DT07/CH00050 ._CH',             # 01
        'ED6_DT07/CH00150 ._CH',             # 02
        'ED6_DT06/CH20137 ._CH',             # 03
        'ED6_DT07/CH00154 ._CH',             # 04
        'ED6_DT07/CH00151 ._CH',             # 05
        'ED6_DT07/CH00450 ._CH',             # 06
        'ED6_DT07/CH00460 ._CH',             # 07
        'ED6_DT07/CH00470 ._CH',             # 08
        'ED6_DT07/CH00454 ._CH',             # 09
        'ED6_DT07/CH00464 ._CH',             # 0A
        'ED6_DT07/CH00474 ._CH',             # 0B
        'ED6_DT07/CH00451 ._CH',             # 0C
        'ED6_DT07/CH00461 ._CH',             # 0D
        'ED6_DT07/CH00471 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT06/CH20053P._CP',             # 00
        'ED6_DT07/CH00050P._CP',             # 01
        'ED6_DT07/CH00150P._CP',             # 02
        'ED6_DT06/CH20137P._CP',             # 03
        'ED6_DT07/CH00154P._CP',             # 04
        'ED6_DT07/CH00151P._CP',             # 05
        'ED6_DT07/CH00450P._CP',             # 06
        'ED6_DT07/CH00460P._CP',             # 07
        'ED6_DT07/CH00470P._CP',             # 08
        'ED6_DT07/CH00454P._CP',             # 09
        'ED6_DT07/CH00464P._CP',             # 0A
        'ED6_DT07/CH00474P._CP',             # 0B
        'ED6_DT07/CH00451P._CP',             # 0C
        'ED6_DT07/CH00461P._CP',             # 0D
        'ED6_DT07/CH00471P._CP',             # 0E
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
        "Function_0_162",          # 00, 0
        "Function_1_178",          # 01, 1
        "Function_2_18B",          # 02, 2
        "Function_3_C6A",          # 03, 3
        "Function_4_23D8",         # 04, 4
    )


    def Function_0_162(): pass

    label("Function_0_162")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_177")

    Return()

    # Function_0_162 end

    def Function_1_178(): pass

    label("Function_1_178")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_72(0x203, 0x0)
    ExitThread()
    Return()

    # Function_1_178 end

    def Function_2_18B(): pass

    label("Function_2_18B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(2260, 0, -14860, 0)
    OP_67(0, 3660, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(332000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2600, 0, -31760, 30)
    SetChrPos(0x111, 2600, 0, -21000, 30)
    SetChrPos(0x113, 4260, 0, -21340, 30)
    SetChrPos(0x112, 940, 0, -20660, 30)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x111,
        (
            "#1743F#6PWhoa... This is way more roomy than\x01",
            "the other caves we've been in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x112,
        (
            "#1750F#6PYou think this is the end of the line?\x02\x03",

            "It sure looks that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x113,
        (
            "#1764F#6PI don't see anything here, though...\x01",
            "or anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x111,
        "#1742F#6PMaybe we haven't finished exploring?\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(500)
    OP_22(0x7B, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #4
        0x10,
        "Man's Voice",
        "#2PNah. You're done. Nice work, guys.\x02",
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_3E7():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_3E7)
    Sleep(50)

    def lambda_3FA():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_3FA)
    Sleep(50)

    def lambda_40D():
        OP_8C(0xFE, 200, 500)
        ExitThread()

    QueueWorkItem(0x113, 2, lambda_40D)
    Sleep(300)

    ChrTalk(    #5
        0x111,
        "#1743F#11PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x112,
        "#1753F#11PWhere'd YOU come from?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x113,
        "#1767F#11PYou were tailin' us the whole time, weren't you?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(4000, 0, -29800, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(180000, 0)
    OP_6E(262, 0)
    SetChrPos(0x10, 4000, 0, -32259, 0)
    SetChrPos(0x111, 4000, 0, -22880, 180)
    SetChrPos(0x112, 2500, 0, -22980, 180)
    SetChrPos(0x113, 5500, 0, -22980, 180)

    def lambda_526():
        OP_8E(0xFE, 0xFA0, 0x0, 0xFFFF900C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_526)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#051F#5PBingo. I've seen everything that's happened on\x01",
            "the way here.\x02\x03",

            "#053FI figured you wouldn't find it easy, but I wasn't\x01",
            "expecting you all to split up partway through.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #9
        0x111,
        (
            "#1747F#6PTh-That was your fault for picking this place!\x02\x03",

            "#1749FWe wouldn't've split up if you picked somewhere\x01",
            "less complicated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#051F#5PHeh. That's WHY I picked this place, numbnuts.\x02\x03",

            "#053FI wanted to see how you'd react when you found\x01",
            "yourselves in a complex situation.\x02\x03",

            "#050FAnd I got exactly what I wanted out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x112,
        "#1753F#6PHuh... Yeah, I can buy that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x113,
        "#1763F#6PThanks a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#053F#5PYou guys're already squared away in battle,\x01",
            "I'll give you that.\x02\x03",

            "On that front, you're already ahead of your\x01",
            "average junior bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x111,
        "#1743F#6PReally...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x112,
        "#1753F#6PYou really think so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x113,
        "#1762F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#551F#5PBut that's only in terms of strength.\x02\x03",

            "#051FUnfortunately, you need more than that to be\x01",
            "a good bracer, junior or senior.\x02\x03",

            "What I saw today really helped me make up my\x01",
            "mind on whether you're cut out for this line of\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x113,
        "#1763F#6PHmph. Good for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#053F#5PI still don't have enough to go on to make\x01",
            "the final call, though.\x02\x03",

            "If you want to prove to me that you've got\x01",
            "what it takes...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(100)
    Fade(500)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_A9C():
        OP_6B(3800, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_A9C)

    def lambda_AAC():
        OP_6D(4000, 0, -29300, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AAC)
    OP_22(0x1F9, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_21()
    OP_1D(0xC4)
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#054F#5P...then you're gonna have to prove it to my\x01",
            "heavy blade first!\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #21
        0x111,
        (
            "#1749F#6P*sigh* How did I know this is how it was gonna\x01",
            "go...?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x111, 6)
    SetChrSubChip(0x111, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x112,
        "#1756F#6PDuh! 'Cause it was obvious.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x112, 7)
    SetChrSubChip(0x112, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x113,
        (
            "#1761F#6PYou wanna see what we've got?\x01",
            "Then we'd be happy to show you!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x113, 8)
    SetChrSubChip(0x113, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x10,
        "#051F#5PCome at me!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    OP_20(0x0)
    Call(0, 3)
    Return()

    # Function_2_18B end

    def Function_3_C6A(): pass

    label("Function_3_C6A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2600, 0, -27040, 0)
    OP_67(0, 4460, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    SetChrPos(0x10, 4000, 0, -27500, 0)
    SetChrPos(0x111, 4000, 0, -24100, 180)
    SetChrPos(0x112, 3000, 0, -24000, 180)
    SetChrPos(0x113, 5000, 0, -24200, 180)

    def lambda_D2A():
        OP_6B(3400, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D2A)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x111,
        "#1743F#12PW-We did it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x112,
        "#1753F#12PNo joke? We seriously beat him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x113,
        "#1762F#6PNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "#053F#5PWell, well... I'm impressed.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10, 0x3, 0x1, 0x1F4)
    Fade(500)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #29
        0x111,
        "#1749F#12P...Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x112,
        "#1755F#12POf COURSE it was too good to be true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x113,
        "#1764F#6PFigures.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#051F#5PHeh. Don't go gettin' too down in the dumps.\x02\x03",

            "You managed to get one over me. You should\x01",
            "still feel proud of yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#053F#5P...Anyway, now I'm confident I've got a good \x01",
            "handle on what you're capable of.\x02\x03",

            "#051FSo let me break down how you did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x111,
        "#1742F#12PNow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x112,
        "#1753F#12PYou're gonna tell us our exam results, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x113,
        "#1763F#6PHere it comes...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #37
        0x10,
        "#050F#5PFirst up: Deen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x111,
        "#1743F#12PI-I'm first?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#051F#5PAs a plus, your judgment ain't anything\x01",
            "to sniff at.\x02\x03",

            "#053FOn the other hand, you have a tendency\x01",
            "to play it safe even when you don't have\x01",
            "to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x111,
        "#1745F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        "#050F#5PYou're next, Rais.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x112,
        "#1752F#12PLay it on me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#053F#5PYour forte is your intuition. In that department,\x01",
            "there's solid potential.\x02\x03",

            "#555FAs far as negatives go, it's hard to overlook\x01",
            "how careless you can be when a situation calls\x01",
            "for critical thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x112,
        "#1755F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#050F#5PFinally, there's you, Rocco.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x113,
        "#1764F#6PHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#053F#5PI'll give you credit for your determination and\x01",
            "unrelenting drive to get the job done...\x02\x03",

            "...but I really can't praise your inability to make\x01",
            "calm, rational decisions.\x02\x03",

            "#051FStick those two qualities together and you're\x01",
            "a walking accident waiting to happen on your\x01",
            "own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x113,
        "#1763F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#551F#5PSo as I'm sure you can already tell, the three\x01",
            "of you just aren't there yet. You're all missing\x01",
            "something before I could call you 'ready.'\x02\x03",

            "#555FWatching you all work, I was on tenterhooks\x01",
            "the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x111,
        "#1749F#12PI hate to admit it, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x112,
        "#1754F#12P...he's probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x113,
        "#1764F#6PGuess we're done, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#053F#5PThat's just if I rate the three of you as individuals.\x02\x03",

            "#051FIf I rate you as a team, then my verdict becomes\x01",
            "a little different.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x112, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x113, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #54
        0x111,
        "#1743F#12P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x112,
        "#1753F#12PWait...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x113,
        "#1762F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#051F#5PWatching you take on that last monster\x01",
            "on the way here was when I was finally\x01",
            "able to stake my confidence in you.\x02\x03",

            "Individually, none of you meet the mark...\x01",
            "but slap the three of you together,\x01",
            "and you just about squeeze over the line.\x02\x03",

            "#053FAnd that's why I'm gonna give you a passing\x01",
            "grade--on one condition.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #58
        0x112,
        "#1750F#12PW-We passed...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x111,
        "#1743F#12PWhat's the condition?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#053F#5PYou can be bracers, but you can only accept\x01",
            "jobs as a group of three. Not individually.\x02\x03",

            "#050FNot until you become senior bracers, anyway.\x01",
            "We'll see where you stand then.\x02\x03",

            "I'll be passing the news on to Jean, so once\x01",
            "that's done and over with, he can throw all\x01",
            "the work you can handle your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x113,
        "#1762F#6PTogether?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#053F#5PThat's right. I want you to build up experience\x01",
            "working together as a group, work on each of\x01",
            "your weaknesses...\x02\x03",

            "#051F...then by the time you hit senior level, you'll\x01",
            "hopefully be ready to take on the kind of solo\x01",
            "work that you can't do now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x113,
        "#1761F#6PHeh. I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x111,
        (
            "#1749F#12PI can't help but feel lame for only getting\x01",
            "a conditional pass...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x112,
        "#1751F#12PSure, but it beats flunking out completely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#053F#5PExactly. Well, I'll be expecting a lot\x01",
            "of improvement from you guys.\x02\x03",

            "#051FBy the way, you planning on stickin'\x01",
            "to stun rods as your main weapons?\x02\x03",

            "I'll buy you all new ones from the weapon\x01",
            "shop over in Bose in honor of you passing.\x01",
            "Just a little somethin' from me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x113, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x111,
        "#1747F#12PY-You're gonna buy us something?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x112,
        "#1753F#12PThat's awesome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x113,
        "#1764F#6P...I think I'm gonna be sick.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        (
            "#551F#5PFor cryin' out loud... My rep with you guys\x01",
            "is even worse than I thought.\x02\x03",

            "#555FI'm not some kinda evil monster that feeds\x01",
            "off of pain and suffering, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x113,
        "#1761F#6PHeh. Could've fooled me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x112,
        (
            "#1756F#12PHe might be right, though. I mean, he's always nice\x01",
            "to that little girl. He's gotta have a soft spot hidden\x01",
            "in there somewhere!\x02\x03",

            "#1751FWhat was her name? Tita?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x10,
        "#057F#5P#4SYou wanna run that by me again?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #74
        0x111,
        (
            "#1745F#6P(C-Crap... Why'd you have to go and bring\x01",
            "her up?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x112,
        "#1753F#11P(Oops.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#053F#5P...So that's how you guys wanna play this,\x01",
            "huh?\x02\x03",

            "#051FI should've known bein' nice wasn't gonna\x01",
            "get me anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x113,
        "#1764F#6P*sigh* Way to frickin' go, Rais...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #78
        0x10,
        (
            "#054F#5PNo more messin' around! Your asses're gonna be\x01",
            "running your way back to the entrance!\x02\x03",

            "Anyone who falls behind any more than I'm willing\x01",
            "to allow gets my blade chucked in the back of their\x01",
            "head!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x111, 0x113, 400)
    Sleep(300)

    ChrTalk(    #79
        0x111,
        (
            "#1747F#11PArgh... Right. You're the one with the most\x01",
            "stamina here, Rocco!\x02\x03",

            "You gotta lead the way so he doesn't catch\x01",
            "up with us!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x113, 0x111, 400)
    Sleep(300)

    ChrTalk(    #80
        0x113,
        "#1761F#6PHeh. That was the plan all along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x112,
        "#1751F*sigh* Exhausting right to the very end, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#054F#5PLess talking, more running!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x111, 180, 0)
    OP_8C(0x112, 180, 0)
    OP_8C(0x113, 180, 0)
    Sleep(300)

    ChrTalk(    #83
        0x111,
        "#1743F#5PY-Yes, sir!\x02",
    )


    ChrTalk(    #84
        0x112,
        "#1752F#4PO-Okay!\x02",
    )


    ChrTalk(    #85
        0x113,
        "#1762F#3PR-Right!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_225E():

        label("loc_225E")

        TurnDirection(0xFE, 0x111, 500)
        OP_48()
        Jump("loc_225E")

    QueueWorkItem2(0x10, 2, lambda_225E)
    OP_62(0x113, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x113, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_62(0x111, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x111, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_62(0x112, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x112, 0x3, 0x0, 0x4)
    Sleep(100)
    OP_C4(0x1, 0x20000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x10, 0xFF)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x6, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x00Side Story [Training, Agate-Style] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CB")
    Sleep(1000)
    OP_28(0xC, 0x4, 0x10)
    OP_28(0xC, 0x4, 0x20)
    OP_3E(0x148, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #87
        "\x07\x05Received \x1F\x48\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(100)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #88
        "\x07\x05Received \x07\x02100 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_23CB")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_C6A end

    def Function_4_23D8(): pass

    label("Function_4_23D8")

    OP_8C(0xFE, 90, 500)

    def lambda_23E5():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFFA114, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23E5)
    WaitChrThread(0xFE, 0x1)

    def lambda_2405():
        OP_8E(0xFE, 0x1770, 0x0, 0xFFFF667C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2405)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_23D8 end

    SaveToFile()

Try(main)
