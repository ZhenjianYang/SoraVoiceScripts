from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4142   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4142.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Cready',                               # 9
        'Spencer',                              # 10
        'Kurt',                                 # 11
        'Glass',                                # 12
        'Glass',                                # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH02060 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT07/CH01143 ._CH',             # 05
        'ED6_DT07/CH01620 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT06/CH20021 ._CH',             # 08
        'ED6_DT27/CH03233 ._CH',             # 09
        'ED6_DT26/CH20692 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH02060P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT07/CH01143P._CP',             # 05
        'ED6_DT07/CH01620P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT06/CH20021P._CP',             # 08
        'ED6_DT27/CH03233P._CP',             # 09
        'ED6_DT26/CH20692P._CP',             # 0A
    )

    DeclNpc(
        X                   = 4560,
        Z                   = 0,
        Y                   = 2500,
        Direction           = 186,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 100,
        Y                   = -3850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5080,
        Z                   = 4700,
        Y                   = 1340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327688,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 4700,
        Y                   = 440,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327688,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4530,
        TriggerZ            = 0,
        TriggerY            = 590,
        TriggerRange        = 400,
        ActorX              = 4560,
        ActorZ              = 1500,
        ActorY              = 2500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_229",          # 01, 1
        "Function_2_22A",          # 02, 2
        "Function_3_22F",          # 03, 3
        "Function_4_230",          # 04, 4
        "Function_5_235",          # 05, 5
        "Function_6_236",          # 06, 6
        "Function_7_280E",         # 07, 7
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_228")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)

    label("loc_228")

    Return()

    # Function_0_20A end

    def Function_1_229(): pass

    label("Function_1_229")

    Return()

    # Function_1_229 end

    def Function_2_22A(): pass

    label("Function_2_22A")

    Call(0, 3)
    Return()

    # Function_2_22A end

    def Function_3_22F(): pass

    label("Function_3_22F")

    Return()

    # Function_3_22F end

    def Function_4_230(): pass

    label("Function_4_230")

    Call(0, 5)
    Return()

    # Function_4_230 end

    def Function_5_235(): pass

    label("Function_5_235")

    Return()

    # Function_5_235 end

    def Function_6_236(): pass

    label("Function_6_236")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(1320, 0, -2340, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(25000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x151, 0x4)
    SetChrFlags(0x151, 0x40)
    SetChrPos(0x103, 5300, 4100, -400, 0)
    SetChrPos(0x151, 5200, 4100, 2320, 180)
    SetChrChipByIndex(0x103, 9)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x151, 10)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_2DE():
        OP_6D(6420, 4000, 1900, 5000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2DE)

    def lambda_2F6():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2F6)

    def lambda_306():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_306)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x15, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x103,
        "#1641F#3SCheers!#2S\x02",
    )


    ChrTalk(    #1
        0x151,
        "#1651F#3S#1PCheers!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    OP_22(0xB2, 0x0, 0x64)

    ChrTalk(    #2
        0x151,
        "#1654F#1P*gulp* *gulp*\x02",
    )

    CloseMessageWindow()
    OP_22(0xB2, 0x0, 0x64)

    ChrTalk(    #3
        0x103,
        (
            "#1646F*gulp* *gulp*\x02\x03",

            "#1641F#3SAhhhh!#2S\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x13, 1)
    SetChrSubChip(0x14, 1)
    OP_0D()

    ChrTalk(    #4
        0x103,
        (
            "#1640FI still can't believe you gave ALL of that money\x01",
            "away.\x02\x03",

            "Okay, maybe you don't need all of it...but you'll\x01",
            "still need some to live, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x151,
        (
            "#1650F#1PI suppose you're right. What I did was a little\x01",
            "strange.\x02\x03",

            "#1654FBut I made up my mind to do this from the very\x01",
            "beginning as a matter of principle.\x02\x03",

            "When I said I didn't do any of this for the money,\x01",
            "I meant it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #6
        0x151,
        (
            "#1651F#1PStill, congratulations on becoming a senior bracer.\x02\x03",

            "I'm not sure what the difference between a senior\x01",
            "and junior bracer is, but it's clear this is something\x01",
            "you really worked for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#1640FIt means I have a lot more authority, but I've got\x01",
            "a lot more responsibility to go with it.\x02\x03",

            "It also means I get a nice new badge, but I wasn't\x01",
            "ever interested in that, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x151,
        "#1653F#1POh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#1641FYup.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8)
    SetChrPos(0x12, 2820, 4000, 4780, 90)

    NpcTalk(    #10
        0x12,
        "Young Man's Voice",
        "#2P...I'm relieved to hear that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x12, 0x8)
    SetChrPos(0x12, -4220, 2000, 4780, 90)
    OP_43(0x12, 0x3, 0x0, 0x7)

    def lambda_7BB():
        OP_6D(3420, 4000, 4900, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7BB)
    WaitChrThread(0x15, 0x0)
    Sleep(2000)

    def lambda_7DD():
        OP_6D(6420, 4000, 1900, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_7DD)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #11
        0x12,
        (
            "#840FI see you're finally beginning to understand the\x01",
            "necessary mindset to be a bracer, Scherazard.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #12
        0x103,
        (
            "#1643FCrap... It's Kurt.\x02\x03",

            "#1646FUmm... This... This might LOOK like alcohol to you,\x01",
            "but it's actually...water...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x12,
        (
            "#840FAs today is admittedly a cause for celebration,\x01",
            "I will turn a blind eye to your drinking tonight.\x02\x03",

            "Just don't go drinking so much that it interferes\x01",
            "with your ability to do your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x103,
        "#1645FFiiiiiine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        "#843F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        "#1641FWh-What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x12,
        (
            "#843FAs you're fully aware, Scherazard, you are now a\x01",
            "senior bracer, which means you must behave with\x01",
            "more responsibility.\x02\x03",

            "That means I expect to see an end to you drinking \x01",
            "in every free moment between jobs, day or night, \x01",
            "and sneaking out at night for it, too.\x02\x03",

            "I also expect to no longer discover that you've\x01",
            "been taking advantage of the busiest times in my\x01",
            "schedule to behave like a drunken lunatic.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8A():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B8A)

    ChrTalk(    #18
        0x103,
        "#1645FI... Uhhh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 0)
    Sleep(100)

    ChrTalk(    #19
        0x151,
        (
            "#1653F#1PIs that really what you usually do, Scherazard?\x02\x03",

            "You sound like a tried and true troublemaker...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        "#1645FDon't say anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x12,
        "#843FAre we clear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        "#1643F#3SY-Yes, sir!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#840FHaha. There's no need for the sir, of course.\x02\x03",

            "We're both senior bracers now, which means\x01",
            "we're both on equal standing.\x02\x03",

            "#841FWhy, I'm hardly even a veteran. I'm still very\x01",
            "much a rookie.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 1)
    Sleep(1000)

    ChrTalk(    #24
        0x103,
        "#1648FSays who?\x02",
    )


    ChrTalk(    #25
        0x151,
        "#1653F#1PAre you, now?\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #26
        0x12,
        (
            "#843FRegardless, this isn't what I'm here to discuss.\x02\x03",

            "#842FThe matter I came for concerns your uncle,\x01",
            "Aina.\x02\x03",

            "I came to make you aware of the fact that the\x01",
            "Bracer Guild is capable of asking for leniency\x01",
            "in his punishment.\x02\x03",

            "#844FHiring a jaeger corps for personal use carries\x01",
            "a very grave punishment, you see...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x151, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x103,
        "#1643F#3SA-A jaeger corps?!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        "#1653F#1PAre you referring to those men dressed in black?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#842FYes. They're one of many corps that are known\x01",
            "to be active here in Liberl.\x02\x03",

            "Recently, there have been many such corps\x01",
            "making their way into the country...and they've\x01",
            "been successful in finding work, too.\x02\x03",

            "Hiring them is, of course, very illegal, but with \x01",
            "the army as slow to act as they currently are...\x02\x03",

            "#843FI've taken this chance to take care of them,\x01",
            "though, so we shouldn't see any sign of any \x01",
            "in the near future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#1643FT-Take care of them? All of them?\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #31
        0x103,
        (
            "#1642F(Now it makes sense. So it wasn't a coincidence\x01",
            "that he showed up when he did...)\x02\x03",

            "(He's been investigating all of the jaeger corps in\x01",
            "Liberl so that he could start an operation to wipe\x01",
            "them all out?)\x02\x03",

            "(#1645FNo wonder he's seemed so swamped...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103)

    ChrTalk(    #32
        0x12,
        (
            "#843FThe jaegers in the country have been targeting\x01",
            "wealthy individuals in hopes of getting them to\x01",
            "sign contracts.\x02\x03",

            "#842FThere have been countless cases like this all\x01",
            "around the country of late, with civilians getting\x01",
            "caught up in it at a worrying frequently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x151,
        "#1654F#1PG-Goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#843FI believe the case we're dealing with here was no\x01",
            "exception, in that it was the jaegers who came to\x01",
            "your uncle rather than the other way round.\x02\x03",

            "It's hard to feel too much sympathy under these\x01",
            "circumstances, but in a sense, your uncle was a\x01",
            "victim in all of this as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x151, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x151,
        "#1653F#1P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        "#1642FWh-What are you trying to pull?!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #37
        0x103,
        (
            "#1644FJust because the jaegers approached him and\x01",
            "not the other way around, he's a victim? That\x01",
            "he deserves to get off with a slap on the wrist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#1644F#3SAnd Aina's supposed to be OKAY with that?!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #39
        0x103,
        "#1647F#3SHe tried to kill her!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #40
        0x12,
        (
            "#843FSchera, please calm down.\x02\x03",

            "#842FThere's no need to shout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        "#1647FI-I'm sorry. But still!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        (
            "#843FNo one is saying he doesn't deserve to\x01",
            "be punished for his actions.\x02\x03",

            "#845FAll I'm here to say is that if--and only if--\x01",
            "Aina wishes, the guild is able to request\x01",
            "leniency in his sentencing. That is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        "#1643FO-Oh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)

    ChrTalk(    #44
        0x103,
        "#1645FWh-Whew... You scared me for a minute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x151,
        "#1654F#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#843FYou needn't make your decision immediately.\x02\x03",

            "Questioning him will take roughly a week as\x01",
            "it is, based on what I've heard.\x02\x03",

            "#840FYou bear no responsibility to even make any\x01",
            "choice at all, so please don't feel as though\x01",
            "you have to think long and hard about this.\x02\x03",

            "Just please be aware that the possibility to \x01",
            "forgive him exists. That is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x151,
        "#1652F#1PAll right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x12,
        (
            "#840FIncidentally, should you ever find yourself in\x01",
            "need of assistance with anything in the future,\x01",
            "the Bracer Guild is always available to aid you.\x02\x03",

            "We're certainly not omnipotent or infallible,\x01",
            "but we'll at least strive to do what we can to\x01",
            "aid those who want our help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x151,
        (
            "#1650F#1PThank you.\x02\x03",

            "I'm really sorry for not telling you the whole\x01",
            "story from the start, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x12,
        (
            "#843FPlease, don't be. With the situation you were in,\x01",
            "your reluctance is quite understandable.\x02\x03",

            "Furthermore...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x103, 500)
    Sleep(200)

    ChrTalk(    #51
        0x12,
        (
            "#842F...one who is worthy of being a full-fledged bracer\x01",
            "should be able to tell roughly what a client wants\x01",
            "just from looking at them.\x02\x03",

            "They should also not, under any circumstances,\x01",
            "try to chase away a potential client in genuine\x01",
            "need. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#1642FOuch...\x02\x03",

            "#1645FI've still got a long way to go, then, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#841FCertainly, but don't we all?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 0, 500)
    Sleep(200)

    ChrTalk(    #54
        0x12,
        (
            "#840FAll right. I've said what I came to say,\x01",
            "so I'll be excusing myself now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D5D():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D5D)
    Sleep(300)
    SetChrSubChip(0x103, 0)
    Sleep(300)

    ChrTalk(    #55
        0x103,
        (
            "#1643FAww. Really?\x02\x03",

            "You could stand to join us for one drink!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #56
        0x12,
        (
            "#843F#3PI'm afraid not. I still have my duties as guild\x01",
            "receptionist remaining, after all.\x02\x03",

            "#845FAs for you, Schera...be careful you don't have\x01",
            "too much 'water.'\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x12, 315, 500)

    def lambda_1E7E():
        OP_8E(0xFE, 0x16F8, 0xFA0, 0x1194, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E7E)
    WaitChrThread(0x12, 0x1)

    def lambda_1E9E():
        OP_8E(0xFE, 0xFFFFFB3C, 0xFA0, 0x1194, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1E9E)
    Sleep(500)
    SetChrSubChip(0x151, 0)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #57
        0x103,
        (
            "#1645FCrud... Why's he always gotta be so serious?\x02\x03",

            "#1640FOh! Actually!\x02\x03",

            "How 'bout you, Aina? Can you handle your liquor?\x01",
            "If you can, you should join me for a few drinks. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x151,
        "#1650F#1PW-Well...all right, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x103,
        "#1643FU-Umm... You're sure? Really, really sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x151,
        (
            "#1650F#1POf course! You've done so much for me,\x01",
            "so how could I refuse?\x02\x03",

            "#1651FJoining you for a few drinks is the least\x01",
            "I can do. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x103,
        (
            "#1640FHeehee! Then let's get to boozin'! Tonight's\x01",
            "gonna be fuuun...\x02\x03",

            "#1641F(I can't wait to see what a prim and proper\x01",
            "girl like her looks like when she's drunk out\x01",
            "of her mind...)\x02\x03",

            "#3S(This is going to be AWESOME!)#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x151, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_22(0xF9, 0x0, 0x64)
    Fade(1000)
    SetChrSubChip(0x13, 5)
    SetChrSubChip(0x14, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #62
        0x103,
        "#1641F#3SWell, cheeeeers! #2S\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x18\x07\x0C#40WI'd seen girls just like her on the other side of\x01",
            "that river.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #64
        (
            "\x18\x07\x0C#40WSilky blonde hair, beautiful blue eyes, smooth\x01",
            "skin...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x18\x07\x0C#40WThe blessed, blissful children on the other side\x01",
            "dressed like royalty and smiling like angels.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x18\x07\x0C#40WSeeing them, I asked myself the same question\x01",
            "over and over again...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #67
        "\x18\x07\x0C#40W'Why aren't I on that side?'\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #68
        (
            "\x18\x07\x0C#40WI envied them. I hated them. I both longed to be \x01",
            "one of them and rejected their very existence. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "\x18\x07\x0C#40WI knew the answer to my question from the very\x01",
            "beginning.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #70
        (
            "\x18\x07\x0C#40WI despaired in myself. I always tried to avoid others\x01",
            "getting too close, believing that to be what I needed\x01",
            "to do in order to live...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #71
        (
            "\x18\x07\x0C#40W...but I could never completely get rid of the tiny,\x01",
            "lingering hope deep within my heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #72
        (
            "\x18\x07\x0C#40WThat eventually, no matter how long it took, the day\x01",
            "would finally come when I could smile from the heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #73
        (
            "\x18\x07\x0C#40WThat the day would come when I would finally be able\x01",
            "to accept and forgive myself for how I was.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #74
        (
            "\x18\x07\x0C#40WThe next day, Aina visited the Bracer Guild and\x01",
            "registered her desire for her uncle to be shown\x01",
            "leniency in his sentencing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "\x18\x07\x0C#40W...Unfortunately, I wasn't able to accompany her,\x01",
            "having been drunk under the table by her the night\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0xFA0)
    OP_21()
    OP_C4(0x1, 0x20000000)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_F7(0xA, 0x2, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #76
        "\x07\x00Side Story [Client] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_C2(0x1, 0x0)
    ClearParty()
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EE")
    Sleep(1000)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x20)
    OP_3E(0x2D6, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05Received \x1F\xD6\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x05Received \x07\x024,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_27EE")

    OP_A2(0x2504)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_2804")
    NewScene("ED6_DT21/U4123   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_280D")

    label("loc_2804")

    NewScene("ED6_DT21/U4121   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_280D")

    Return()

    # Function_6_236 end

    def Function_7_280E(): pass

    label("Function_7_280E")


    def lambda_2814():
        OP_8E(0xFE, 0x16F8, 0xFA0, 0x12AC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2814)
    WaitChrThread(0x12, 0x1)

    def lambda_2834():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0xEC4, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2834)
    WaitChrThread(0x12, 0x1)

    def lambda_2854():
        OP_8E(0xFE, 0x1AE0, 0xFA0, 0x488, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2854)
    Sleep(800)
    SetChrSubChip(0x103, 2)
    Sleep(100)
    SetChrSubChip(0x151, 1)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x103, 400)
    Sleep(300)
    Return()

    # Function_7_280E end

    SaveToFile()

Try(main)
