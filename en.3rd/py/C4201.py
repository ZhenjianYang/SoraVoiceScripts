from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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


    DeclActor(
        TriggerX            = 123780,
        TriggerZ            = 0,
        TriggerY            = 19220,
        TriggerRange        = 1000,
        ActorX              = 122910,
        ActorZ              = 1500,
        ActorY              = 19200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103870,
        TriggerZ            = 0,
        TriggerY            = 24400,
        TriggerRange        = 1000,
        ActorX              = 103830,
        ActorZ              = 1500,
        ActorY              = 24960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 136410,
        TriggerZ            = 0,
        TriggerY            = -112150,
        TriggerRange        = 1000,
        ActorX              = 137180,
        ActorZ              = 1500,
        ActorY              = -112180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 128250,
        TriggerZ            = 0,
        TriggerY            = -152730,
        TriggerRange        = 1000,
        ActorX              = 127270,
        ActorZ              = 1500,
        ActorY              = -152920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 130400,
        TriggerZ            = 0,
        TriggerY            = -145890,
        TriggerRange        = 3000,
        ActorX              = 130400,
        ActorZ              = 3000,
        ActorY              = -145890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_15E",          # 00, 0
        "Function_1_15F",          # 01, 1
        "Function_2_208",          # 02, 2
        "Function_3_21E",          # 03, 3
        "Function_4_1A63",         # 04, 4
        "Function_5_1A92",         # 05, 5
        "Function_6_1A93",         # 06, 6
        "Function_7_1A94",         # 07, 7
        "Function_8_1AAB",         # 08, 8
        "Function_9_1BD8",         # 09, 9
        "Function_10_1D12",        # 0A, 10
        "Function_11_1E54",        # 0B, 11
        "Function_12_1F8D",        # 0C, 12
        "Function_13_1FF8",        # 0D, 13
        "Function_14_2232",        # 0E, 14
    )


    def Function_0_15E(): pass

    label("Function_0_15E")

    Return()

    # Function_0_15E end

    def Function_1_15F(): pass

    label("Function_1_15F")

    OP_6F(0x0, 0)
    OP_6F(0x3, 0)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E")
    OP_1B(0x0, 0x0, 0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_END)), "loc_19A")
    OP_6F(0x0, 240)
    OP_6F(0x3, 120)
    Jump("loc_19E")

    label("loc_19A")

    OP_65(0x4, 0x1)

    label("loc_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0")
    OP_6F(0x1, 0)
    Jump("loc_1B7")

    label("loc_1B0")

    OP_6F(0x1, 60)

    label("loc_1B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9")
    OP_6F(0x2, 0)
    Jump("loc_1D0")

    label("loc_1C9")

    OP_6F(0x2, 60)

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2")
    OP_6F(0x4, 0)
    Jump("loc_1E9")

    label("loc_1E2")

    OP_6F(0x4, 60)

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB")
    OP_6F(0x5, 0)
    Jump("loc_202")

    label("loc_1FB")

    OP_6F(0x5, 60)

    label("loc_202")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_15F end

    def Function_2_208(): pass

    label("Function_2_208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_208")

    label("loc_21D")

    Return()

    # Function_2_208 end

    def Function_3_21E(): pass

    label("Function_3_21E")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(129300, 0, -151840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 129199, 0, -152700, 270)
    SetChrPos(0x151, 129199, 0, -151240, 225)
    Sleep(1000)

    ChrTalk(    #0
        0x151,
        (
            "#1653FIs it not budging?\x02\x03",

            "#1656FHmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x151, 135, 400)
    Sleep(600)
    OP_8C(0x151, 315, 400)
    Sleep(600)

    ChrTalk(    #1
        0x103,
        "#1648FStay quiet for a minute. I'll handle this.\x02",
    )

    CloseMessageWindow()

    def lambda_30F():
        OP_8E(0xFE, 0x1F630, 0x0, 0xFFFDAB84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30F)

    def lambda_32A():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_32A)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Scherazard removed a rock from the bottom of the device and placed her\x01",
            "hand inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x64, 0x0, 0x64)
    OP_6F(0x3, 65)
    OP_70(0x3, 0x78)
    OP_73(0x3)
    OP_6F(0x3, 120)
    Sleep(500)
    OP_6D(128919, 0, -146150, 2000)
    OP_22(0xD0, 0x0, 0x64)
    OP_70(0x0, 0xF0)
    Sleep(200)

    def lambda_418():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_418)
    Sleep(100)

    def lambda_42B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_42B)
    OP_73(0x0)
    OP_6F(0x0, 240)
    OP_6D(129300, 0, -151840, 2000)

    ChrTalk(    #3
        0x151,
        (
            "#1653F#1PWow...\x02\x03",

            "#1651FHeehee. You really are amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#1646FBut not for this. This isn't all that different\x01",
            "from breaking into a safe, to be honest.\x02\x03",

            "#1648F...Really, though.\x02\x03",

            "You shouldn't be impressed by these kinds of\x01",
            "things. Or getting used to them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_55D():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_55D)
    Sleep(300)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    def lambda_58C():
        OP_6B(2600, 10000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_58C)

    ChrTalk(    #5
        0x151,
        "#1653FWhy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x103,
        (
            "#1648FThere are some things in life you're just better\x01",
            "off not knowing...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FB():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5FB)
    OP_20(0xFA0)
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(300)
    OP_24(0x1CD, 0x50)
    Sleep(300)
    OP_24(0x1CD, 0x46)
    Sleep(300)
    OP_24(0x1CD, 0x3C)
    Sleep(300)
    OP_24(0x1CD, 0x32)
    Sleep(300)
    OP_24(0x1CD, 0x28)
    Sleep(300)
    OP_24(0x1CD, 0x1E)
    Sleep(300)
    OP_24(0x1CD, 0x14)
    Sleep(300)
    OP_23(0x1CD)
    OP_21()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x18\x07\x0C#40W...and some things you're better off not being\x01",
            "able to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_21()
    OP_22(0x173, 0x0, 0x64)
    Sleep(4000)
    OP_1D(0x1A)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x18\x07\x0C#40WThe entire town smelled like a rotting open drain\x01",
            "and was reviled even for a slum.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x18\x07\x0C#40WThe people who ended up there were largely\x01",
            "those who couldn't be accommodated in a prison,\x01",
            "those who had been driven out of the cities...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x18\x07\x0C#40W...or children who had been abandoned there like\x01",
            "yesterday's garbage.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x18\x07\x0C#40WI did whatever I had to in order to survive and \x01",
            "to live to see another day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1200)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x18\x07\x0C#40W\x01",
            "Picking pockets at every opportunity was a habit\x01",
            "I picked up from a very young age; anything that\x01",
            "caught my eye, I took. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x18\x07\x0C#40WBut even then, I didn't end up with enough to live\x01",
            "on. There were always men there who made their\x01",
            "living by taking from people like me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x18\x07\x0C#40WThe surest way to make money was stealing from\x01",
            "the safes of the rich when they were out of their\x01",
            "mansions.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x18\x07\x0C#40WThe residential area full of wealthy people on the\x01",
            "other side of the river, accessible through an\x01",
            "underground sewer, was a perfect target for this.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x18\x07\x0C#40WEvery time I felt hungry, I sneaked inside one of\x01",
            "the mansions and made use of the skills I felt like\x01",
            "I'd known since the day I was born.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x18\x07\x0C#40WThe most important thing to remember when doing\x01",
            "this was not to take everything in one go.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x18\x07\x0C#40WInstead, the key was to take only a small amount\x01",
            "each time--enough to get by, but not enough for\x01",
            "the mansion's owner to notice anything was gone.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x18\x07\x0C#40WWith a simple piece of wire, I had access to enough\x01",
            "mira to live for a couple more weeks.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x18\x07\x0C#40WBefore I knew it, I was doing it every day, building up\x01",
            "a stockpile of money instead of simply taking what\x01",
            "I needed in the short term.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x18\x07\x0C#40W...And boy, I paid the price for it. I had it all taken\x01",
            "from me by the men of the slums and ended up being\x01",
            "kicked and stomped on until I coughed up blood.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x18\x07\x0C#40WEveryone did what they did--or they said they did as\x01",
            "much, anyway--so that they could keep living on.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1C9, 0x1, 0xA)
    Sleep(300)
    OP_24(0x1C9, 0x14)
    Sleep(300)
    OP_24(0x1C9, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    OP_C5(0x0, 0xFE00, 0xFE00, 0x200, 0x200, 0x140, 0xF0, 0x400, 0x400, 0x0, 0x0, 0x400, 0x400, 0xFFFFFF, 0x0, "C_VIS353._CH")
    OP_C6(0x0, 0x1, 800, 800, 0)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_43(0x103, 0x3, 0x0, 0x4)
    Sleep(4500)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x18\x07\x0C#40WAlways pretending to be desperate as an excuse to\x01",
            "live by any means, but always taking the easiest road\x01",
            "they could find.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x18\x07\x0C#40WThe town I lived in was devoid of energy, but full of\x01",
            "filthy humans like them...and like me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x18\x07\x0C#40WAgain and again, I thought about giving it up.\x01",
            "Again and again, I said to myself that I wanted\x01",
            "to stop...but I couldn't do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x18\x07\x0C#40WI hated myself for what I was doing.\x01",
            "I hated the fact that I couldn't stop.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 8947848, 2000, 0)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x14)
    Sleep(200)
    OP_23(0x1C9)
    OP_C7(0x0, 0x0, 0x3)
    OP_44(0x103, 0x3)
    OP_C7(0x1, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(    #27
        (
            "\x18\x07\x0C#40WIt was because I didn't want to return to that life\x01",
            "that I ended up becoming a bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "\x18\x07\x0C#40W...Because if I didn't, I was scared I would end up\x01",
            "right back where I was.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #29
        (
            "\x18\x07\x0C#40WThe troupe had saved me from that place and had\x01",
            "made me into a respectable human being...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x18\x07\x0C#40W...but when I lost them, I was afraid. One thought\x01",
            "stood out above all the rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x18\x07\x0C#40WNo matter how much I tried to forget,\x01",
            "no matter how used I became to my new life,\x01",
            "no matter how much I tried to deny it...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x18\x07\x0C#40W...I was yesterday's garbage from the slums,\x01",
            "and nothing I could do would change that.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #33
        "\x18\x07\x0C#40WAnd that's it, really.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #34
        "\x18\x07\x0C#40WOne day, I'm sure I'll end up returning there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #35
        "\x18\x07\x0C#40WThat's why I need to be strong. To STAY strong.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x18\x07\x0C#40WWhat job I do doesn't even matter. Anything I can\x01",
            "pour my heart into that'll let me live an honest life\x01",
            "is fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x18\x07\x0C#40WAnything that keeps my mind off the past...\x01",
            "Anything that lets me keep the ugliness in my heart\x01",
            "at bay...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x18\x07\x0C#40WIf it makes me strong without relying on others,\x01",
            "then it's fine. It's fine...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x18\x07\x0C#40WI need to be strong. Stronger than anyone.\x01",
            "Stronger than anyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #40
        "\x18\x07\x0C#40W...But am I?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "\x18\x07\x0C#40WAm I really doing all right in my new life?\x01",
            "Am I really getting stronger?\x02\x01",

            "...Am I, Luci?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(127220, 0, -150380, 0)
    OP_67(0, 7100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 126600, 0, -151000, 270)
    SetChrPos(0x151, 128639, 0, -151000, 270)
    OP_C4(0x1, 0x800)
    OP_20(0x1388)

    def lambda_171B():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_171B)
    FadeToBright(5000, 0)
    Sleep(300)
    OP_22(0x1CD, 0x1, 0xA)
    Sleep(300)
    OP_24(0x1CD, 0x14)
    Sleep(300)
    OP_24(0x1CD, 0x1E)
    Sleep(300)
    OP_24(0x1CD, 0x28)
    Sleep(300)
    OP_24(0x1CD, 0x32)
    Sleep(300)
    OP_24(0x1CD, 0x3C)
    Sleep(300)
    OP_24(0x1CD, 0x46)
    Sleep(300)
    OP_24(0x1CD, 0x50)
    Sleep(300)
    OP_24(0x1CD, 0x5A)
    Sleep(300)
    OP_24(0x1CD, 0x64)
    OP_0D()
    WaitChrThread(0x103, 0x2)
    Sleep(300)

    ChrTalk(    #42
        0x151,
        (
            "#1653F#2PMiss Scherazard...?\x02\x03",

            "Are you all right? You're looking very gloomy\x01",
            "all of a sudden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x103,
        (
            "#1648F...It's nothing. I'm fine.\x02\x03",

            "#1646F(As soon as I finish this job, Kurt will give me\x01",
            "the last recommendation I need.)\x02\x03",

            "(I can finally become a real bracer.)\x02\x03",

            "(Then no one will be able to tell me I'm not\x01",
            "strong. I won't let them! I WILL be strong!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    Sleep(300)

    ChrTalk(    #44
        0x103,
        "#1648FAnyway, we're leaving.\x02",
    )

    CloseMessageWindow()

    def lambda_192D():
        OP_8E(0xFE, 0x225C4, 0x0, 0xFFFDB228, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_192D)

    def lambda_1948():

        label("loc_1948")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_1948")

    QueueWorkItem2(0x151, 2, lambda_1948)

    def lambda_1959():
        OP_8F(0xFE, 0x1F67F, 0x0, 0xFFFDAD78, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1959)
    WaitChrThread(0x151, 0x1)
    Sleep(1000)

    ChrTalk(    #45
        0x151,
        (
            "#1653F#3PW-Wait a second!\x02\x03",

            "Miss Scherazard!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x151, 0x2)

    def lambda_19B3():
        OP_8E(0xFE, 0x1FB6C, 0x0, 0xFFFDB228, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_19B3)
    WaitChrThread(0x151, 0x1)

    def lambda_19D3():
        OP_8E(0xFE, 0x225C4, 0x0, 0xFFFDB228, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_19D3)
    WaitChrThread(0x151, 0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        "\x18\x07\x0C#40WAs soon as I finish this job...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_64(0x5, 0x1)
    OP_64(0x4, 0x1)
    OP_C4(0x1, 0x800)
    OP_A2(0x2F4E)
    NewScene("ED6_DT21/C4203   ._SN", 115, 0, 0)
    IdleLoop()
    Return()

    # Function_3_21E end

    def Function_4_1A63(): pass

    label("Function_4_1A63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A91")
    OP_C6(0x0, 0x2, -360000, 250000, 0)
    OP_C7(0x0, 0x0, 0x2)
    OP_C6(0x0, 0x2, 0, 0, 0)
    Jump("Function_4_1A63")

    label("loc_1A91")

    Return()

    # Function_4_1A63 end

    def Function_5_1A92(): pass

    label("Function_5_1A92")

    Return()

    # Function_5_1A92 end

    def Function_6_1A93(): pass

    label("Function_6_1A93")

    Return()

    # Function_6_1A93 end

    def Function_7_1A94(): pass

    label("Function_7_1A94")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (112, "loc_1AA4"),
        (114, "loc_1AA7"),
        (SWITCH_DEFAULT, "loc_1AAA"),
    )


    label("loc_1AA4")

    Jump("loc_1AAA")

    label("loc_1AA7")

    Jump("loc_1AAA")

    label("loc_1AAA")

    Return()

    # Function_7_1A94 end

    def Function_8_1AAB(): pass

    label("Function_8_1AAB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B84")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_1B19")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF0)
    Jump("loc_1B81")

    label("loc_1B19")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_1B81")

    Jump("loc_1BCA")

    label("loc_1B84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05Estelle used Thief! But it failed!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xC, 0x0)

    label("loc_1BCA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1AAB end

    def Function_9_1BD8(): pass

    label("Function_9_1BD8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_1C46")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF1)
    Jump("loc_1CAE")

    label("loc_1C46")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #51
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_1CAE")

    Jump("loc_1D04")

    label("loc_1CB1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05Do you take joy in yanking out others' insides?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xD, 0x0)

    label("loc_1D04")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1BD8 end

    def Function_10_1D12(): pass

    label("Function_10_1D12")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_1D80")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF2)
    Jump("loc_1DE8")

    label("loc_1D80")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #54
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1DE8")

    Jump("loc_1E46")

    label("loc_1DEB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05Sorry, but the legendary item drop is in another chest.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xE, 0x0)

    label("loc_1E46")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1D12 end

    def Function_11_1E54(): pass

    label("Function_11_1E54")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5FE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x203, 1)"), scpexpr(EXPR_END)), "loc_1EC2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x05Found \x1F\x03\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2FF3)
    Jump("loc_1F2A")

    label("loc_1EC2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #57
        (
            "\x07\x05Found \x1F\x03\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x03\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1F2A")

    Jump("loc_1F7F")

    label("loc_1F2D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #58
        "\x07\x05If you want it that badly, you could've asked.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xF, 0x0)

    label("loc_1F7F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1E54 end

    def Function_12_1F8D(): pass

    label("Function_12_1F8D")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05The lever won't move.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF7")
    Call(0, 3)

    label("loc_1FF7")

    Return()

    # Function_12_1F8D end

    def Function_13_1FF8(): pass

    label("Function_13_1FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2055")

    ChrTalk(    #60
        0x103,
        (
            "#1640FThere should be some way to open this door nearby.\x01",
            "Let's start looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222E")

    label("loc_2055")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x103, 132300, 0, -145380, 255)
    SetChrPos(0x151, 133360, 0, -145880, 255)
    OP_0D()

    def lambda_2085():
        OP_6D(133140, 0, -144700, 2000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2085)

    def lambda_209D():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_209D)

    def lambda_20B5():
        OP_6C(18000, 2000)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_20B5)
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #61
        0x151,
        (
            "#1650FI'm guessing we'll need to find some way through\x01",
            "this door to get to the west block.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x103,
        (
            "#1646F#1PThere should be some way to open it nearby.\x02\x03",

            "Let's start looking...and stick close to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x151,
        (
            "#1650FOh, my. That's kind of...#3700W #20 \x01\x03",
            "#1651F...romantic, don't you think? ㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #64
        0x103,
        "#1644F#1PIn what way is anything in this situation romantic?!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x0)
    EventEnd(0x5)

    label("loc_222E")

    TalkEnd(0xFF)
    Return()

    # Function_13_1FF8 end

    def Function_14_2232(): pass

    label("Function_14_2232")

    EventBegin(0x1)
    NewScene("ED6_DT21/C4200   ._SN", 114, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2232 end

    SaveToFile()

Try(main)
